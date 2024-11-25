import itertools
from llvmlite import ir

class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        if '.' in str(self.value):
            return ir.Constant(ir.FloatType(), float(self.value))
        else:
            return ir.Constant(ir.IntType(32), int(self.value))

class StringLiteral():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value.strip('"') 

    def eval(self):
        str_value = self.value.replace("\\n", "\n")
        str_value += "\0"
        str_bytes = bytearray(str_value.encode("utf8"))
        str_len = len(str_bytes)
        str_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), str_len), str_bytes)
        
        global_str = ir.GlobalVariable(self.module, str_fmt.type, name="str")
        global_str.linkage = 'internal'
        global_str.global_constant = True
        global_str.initializer = str_fmt
        
        voidptr_ty = ir.IntType(8).as_pointer()
        return self.builder.bitcast(global_str, voidptr_ty)

class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right

    def _convert_to_same_type(self, left_val, right_val):
        if isinstance(left_val.type, ir.IntType) and isinstance(right_val.type, ir.FloatType):
            left_val = self.builder.sitofp(left_val, ir.FloatType())
        elif isinstance(left_val.type, ir.FloatType) and isinstance(right_val.type, ir.IntType):
            right_val = self.builder.sitofp(right_val, ir.FloatType())
        return left_val, right_val

class Sum(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        
        left_val, right_val = self._convert_to_same_type(left_val, right_val)
        
        if isinstance(left_val.type, ir.FloatType):
            result = self.builder.fadd(left_val, right_val, name="sumtmp")
        else:
            result = self.builder.add(left_val, right_val, name="sumtmp")
        
        return result

class Sub(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        
        left_val, right_val = self._convert_to_same_type(left_val, right_val)
        
        if isinstance(left_val.type, ir.FloatType):
            result = self.builder.fsub(left_val, right_val, name="subtmp")
        else:
            result = self.builder.sub(left_val, right_val, name="subtmp")
        
        return result

class Mul(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        
        left_val, right_val = self._convert_to_same_type(left_val, right_val)
        
        if isinstance(left_val.type, ir.FloatType):
            result = self.builder.fmul(left_val, right_val, name="multmp")
        else:
            result = self.builder.mul(left_val, right_val, name="multmp")
        
        return result

class Div(BinaryOp):
    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        
        left_val, right_val = self._convert_to_same_type(left_val, right_val)
        
        if isinstance(left_val.type, ir.FloatType):
            result = self.builder.fdiv(left_val, right_val, name="divtmp")
        else:
            result = self.builder.sdiv(left_val, right_val, name="divtmp")
        
        return result

class UnaryOp():
    def __init__(self, builder, module, operand, variable=None):
        self.builder = builder
        self.module = module
        self.operand = operand
        self.variable = variable

class Inc(UnaryOp):
    def eval(self):
        var = self.operand.eval()
        inc_value = self.builder.add(var, ir.Constant(ir.IntType(32), 1))
        if self.variable:
            self.variable.store(inc_value)
        return inc_value

class Dec(UnaryOp):
    def eval(self):
        var = self.operand.eval()
        dec_value = self.builder.sub(var, ir.Constant(ir.IntType(32), 1))
        if self.variable:
            self.variable.store(dec_value)
        return dec_value

class Variable():
    def __init__(self, builder, module, name):
        self.builder = builder
        self.module = module
        self.name = name
        self.pointer = None

    def allocate(self, value):
        if isinstance(value, ir.Constant):
            if value.type == ir.IntType(1):
                self.pointer = self.builder.alloca(ir.IntType(1), name=self.name)
            elif value.type == ir.FloatType():
                self.pointer = self.builder.alloca(ir.FloatType(), name=self.name)
            elif isinstance(value.type, ir.ArrayType) and value.type.element == ir.IntType(8):
                self.pointer = self.builder.alloca(value.type, name=self.name)
            else:
                self.pointer = self.builder.alloca(ir.IntType(32), name=self.name)
        elif isinstance(value, (Boolean, BooleanNot, BooleanOp)):
            self.pointer = self.builder.alloca(ir.IntType(1), name=self.name)
        elif isinstance(value, ir.instructions.Instruction):
            if value.type == ir.IntType(1):
                self.pointer = self.builder.alloca(ir.IntType(1), name=self.name)
            elif value.type == ir.FloatType():
                self.pointer = self.builder.alloca(ir.FloatType(), name=self.name)
            elif isinstance(value.type, ir.PointerType) and value.type.pointee == ir.IntType(8):
                self.pointer = self.builder.alloca(value.type, name=self.name)
            else:
                self.pointer = self.builder.alloca(ir.IntType(32), name=self.name)
        else:
            raise ValueError(f"Unsupported type for variable {self.name}")

    def store(self, value):
        if self.pointer is None:
            self.allocate(value)
        self.builder.store(value, self.pointer)

    def load(self):
        if self.pointer is None:
            raise ValueError(f"Variable {self.name} has not been initialized")
        return self.builder.load(self.pointer, name=f"{self.name}.load")

    def eval(self):
        return self.load()

class Assign():
    def __init__(self, builder, module, variable, value):
        self.builder = builder
        self.module = module
        self.variable = variable
        self.value = value

    def eval(self):
        value_to_store = self.value.eval()
        self.variable.store(value_to_store)

class Print():
    counter = itertools.count()

    def __init__(self, builder, module, printf_func, value):
        self.builder = builder
        self.module = module
        self.printf_func = printf_func
        self.value = value
        self.fstr_name = f"fstr_{next(self.counter)}"

    def eval(self):
        voidptr_ty = ir.IntType(8).as_pointer()

        if isinstance(self.value, StringLiteral):
            str_value = self.value.value
            str_value = str_value.replace("\\n", "\n")
            str_value += "\0"
            str_bytes = bytearray(str_value.encode("utf8"))
            str_len = len(str_bytes)
            str_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), str_len), str_bytes)
            
            global_str = ir.GlobalVariable(self.module, str_fmt.type, name=self.fstr_name)
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = str_fmt
            
            fmt_str = "%s\n\0"
            fmt_arg = self.builder.bitcast(global_str, voidptr_ty)
            self.builder.call(self.printf_func, [fmt_arg, fmt_arg])
        
        else:
            value_to_print = self.value.eval()
            fmt_str = ""
            fmt_arg = None

            if isinstance(value_to_print.type, ir.IntType):
                fmt_str = "%i\n\0"
                if value_to_print.type.width == 1:
                    value_to_print = self.builder.zext(value_to_print, ir.IntType(32))
                fmt_arg = value_to_print
            elif isinstance(value_to_print.type, ir.FloatType):
                fmt_str = "%f\n\0"
                value_to_print = self.builder.fpext(value_to_print, ir.DoubleType())
                fmt_arg = value_to_print
            elif isinstance(value_to_print.type, ir.PointerType) and value_to_print.type.pointee == ir.IntType(8):
                fmt_str = "%s\n\0"
                fmt_arg = value_to_print

            if fmt_str:
                c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str)), bytearray(fmt_str.encode("utf8")))
                global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=self.fstr_name)
                global_fmt.linkage = 'internal'
                global_fmt.global_constant = True
                global_fmt.initializer = c_fmt
                fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
                self.builder.call(self.printf_func, [fmt_arg, value_to_print])

class Condition():
    def __init__(self, builder, module, left, right, operator):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right
        self.operator = operator

    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        if self.operator == 'EQ':
            return self.builder.icmp_unsigned('==', left_val, right_val)
        elif self.operator == 'NEQ':
            return self.builder.icmp_unsigned('!=', left_val, right_val)
        elif self.operator == 'LT':
            return self.builder.icmp_unsigned('<', left_val, right_val)
        elif self.operator == 'GT':
            return self.builder.icmp_unsigned('>', left_val, right_val)
        elif self.operator == 'LEQ':
            return self.builder.icmp_unsigned('<=', left_val, right_val)
        elif self.operator == 'GEQ':
            return self.builder.icmp_unsigned('>=', left_val, right_val)

class IfThenElse():
    def __init__(self, builder, module, condition, then_body, else_body):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body

    def eval(self):
        cond_val = self.condition.eval()
        then_block = self.builder.append_basic_block('then')
        else_block = self.builder.append_basic_block('else')
        merge_block = self.builder.append_basic_block('ifcont')
        self.builder.cbranch(cond_val, then_block, else_block)
        
        self.builder.position_at_start(then_block)
        for stmt in self.then_body:
            stmt.eval()
        self.builder.branch(merge_block)
        then_block = self.builder.block

        self.builder.position_at_start(else_block)
        for stmt in self.else_body:
            stmt.eval()
        self.builder.branch(merge_block)
        else_block = self.builder.block

        self.builder.position_at_start(merge_block)

class Boolean():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        return ir.Constant(ir.IntType(1), int(self.value))

class BooleanOp(BinaryOp):
    def __init__(self, builder, module, left, right, operator):
        super().__init__(builder, module, left, right)
        self.operator = operator

    def eval(self):
        left_val = self.left.eval()
        right_val = self.right.eval()
        if self.operator == 'AND':
            return self.builder.and_(left_val, right_val)
        elif self.operator == 'OR':
            return self.builder.or_(left_val, right_val)

class BooleanNot():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        val = self.value.eval()
        return self.builder.not_(val)

class While():
    def __init__(self, builder, module, condition, body):
        self.builder = builder
        self.module = module
        self.condition = condition
        self.body = body

    def eval(self):
        loop_cond_block = self.builder.append_basic_block('loop_cond')
        loop_body_block = self.builder.append_basic_block('loop_body')
        loop_end_block = self.builder.append_basic_block('loop_end')

        self.builder.branch(loop_cond_block)

        self.builder.position_at_start(loop_cond_block)
        cond_val = self.condition.eval()
        self.builder.cbranch(cond_val, loop_body_block, loop_end_block)

        self.builder.position_at_start(loop_body_block)
        for stmt in self.body:
            stmt.eval()
        self.builder.branch(loop_cond_block)

        self.builder.position_at_start(loop_end_block)
