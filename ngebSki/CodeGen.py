
from llvmlite import ir, binding
class CodeGen():
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_all_targets()
        self.binding.initialize_all_asmprinters()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_function()

    def _config_llvm(self):
        self.module = ir.Module(name=__file__)
        self.module.triple = binding.get_default_triple()  # Get the default triple
        if "arm64" in self.module.triple:
            self.module.triple = "arm64-apple-macosx11.0.0"
        func_type = ir.FunctionType(ir.VoidType(), [], False)
        base_func = ir.Function(self.module, func_type, name="main")
        block = base_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def _create_execution_engine(self):
        target = self.binding.Target.from_triple(self.module.triple)
        target_machine = target.create_target_machine()
        backing_mod = self.binding.parse_assembly("")
        self.engine = self.binding.create_mcjit_compiler(backing_mod, target_machine)

    def _declare_print_function(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")
        self.printf = printf

    def _compile_ir(self):
        self.builder.ret_void()
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod

    def create_ir(self):
        self._compile_ir()

    def save_ir(self, filename):
        with open(filename, 'w') as output_file:
            output_file.write(str(self.module))

    def _declare_global_string(self, name, value):
        str_val = bytearray(value.encode('utf8'))
        str_const = ir.Constant(ir.ArrayType(ir.IntType(8), len(str_val)), str_val)
        global_var = ir.GlobalVariable(self.module, str_const.type, name=name)
        global_var.linkage = 'internal'
        global_var.global_constant = True
        global_var.initializer = str_const
        return global_var