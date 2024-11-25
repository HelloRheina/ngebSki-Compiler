from rply import ParserGenerator
from astree import Number, Sum, Sub, Mul, Div, Print, Assign, Variable, Condition, IfThenElse, While, Boolean, BooleanOp, BooleanNot, Inc, Dec, StringLiteral

class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            ['INTEGER', 'FLOAT', 'LONG', 'SHORT', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'EQUALS', 'ID',
             'IF', 'THEN', 'ELSE', 'END', 'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ',
             'WHILE', 'DO', 'TRUE', 'FALSE', 'AND', 'OR', 'NOT', 'INCREMENT', 'DECREMENT', 'STRING_LITERAL'],
            precedence=[
                ('left', ['AND', 'OR']),
                ('left', ['EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ']),
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV']),
                ('right', ['NOT'])
            ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf
        self.variables = {}

    def parse(self):
        @self.pg.production('program : statement_list')
        def program(p):
            return p[0]

        @self.pg.production('statement_list : statement_list statement')
        @self.pg.production('statement_list : statement')
        def statement_list(p):
            if len(p) == 1:
                return [p[0]]
            else:
                p[0].append(p[1])
                return p[0]

        @self.pg.production('statement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def statement_print(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('statement : assign')
        @self.pg.production('statement : if_statement')
        @self.pg.production('statement : while_statement')
        @self.pg.production('statement : expression SEMI_COLON')
        def statement(p):
            return p[0]

        @self.pg.production('assign : ID EQUALS expression SEMI_COLON')
        @self.pg.production('assign : ID EQUALS boolean_expression SEMI_COLON')
        @self.pg.production('assign : ID EQUALS ID INCREMENT SEMI_COLON')
        @self.pg.production('assign : ID EQUALS ID DECREMENT SEMI_COLON')
        def assign(p):
            var_name = p[0].getstr()
            if var_name not in self.variables:
                self.variables[var_name] = Variable(self.builder, self.module, var_name)
            variable = self.variables[var_name]
            if len(p) == 4:
                value = p[2]
            else:
                id_name = p[2].getstr()
                if id_name not in self.variables:
                    raise ValueError(f"Undefined variable {id_name}")
                id_variable = self.variables[id_name]
                if p[3].gettokentype() == 'INCREMENT':
                    value = Inc(self.builder, self.module, id_variable)
                else:
                    value = Dec(self.builder, self.module, id_variable)
            return Assign(self.builder, self.module, variable, value)

        @self.pg.production('if_statement : IF condition THEN statement_list optional_else END')
        def if_statement(p):
            condition = p[1]
            then_body = p[3]
            else_body = p[4]
            return IfThenElse(self.builder, self.module, condition, then_body, else_body)

        @self.pg.production('optional_else : ELSE statement_list')
        @self.pg.production('optional_else : ')
        def optional_else(p):
            if len(p) == 0:
                return []
            return p[1]

        @self.pg.production('while_statement : WHILE condition DO statement_list END')
        def while_statement(p):
            condition = p[1]
            body = p[3]
            return While(self.builder, self.module, condition, body)

        @self.pg.production('condition : boolean_expression')
        def condition(p):
            return p[0]

        @self.pg.production('boolean_expression : boolean_expression AND boolean_expression')
        @self.pg.production('boolean_expression : boolean_expression OR boolean_expression')
        @self.pg.production('boolean_expression : comparison')
        @self.pg.production('boolean_expression : term')
        def boolean_expression(p):
            if len(p) == 3:
                left = p[0]
                operator = p[1].gettokentype()
                right = p[2]
                return BooleanOp(self.builder, self.module, left, right, operator)
            else:
                return p[0]

        @self.pg.production('comparison : expression EQ expression')
        @self.pg.production('comparison : expression NEQ expression')
        @self.pg.production('comparison : expression LT expression')
        @self.pg.production('comparison : expression GT expression')
        @self.pg.production('comparison : expression LEQ expression')
        @self.pg.production('comparison : expression GEQ expression')
        def comparison(p):
            left = p[0]
            operator = p[1].gettokentype()
            right = p[2]
            return Condition(self.builder, self.module, left, right, operator)

        @self.pg.production('expression : expression SUM term')
        @self.pg.production('expression : expression SUB term')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)

        @self.pg.production('expression : term')
        @self.pg.production('expression : boolean_expression')
        @self.pg.production('expression : NOT expression')
        @self.pg.production('expression : SUB term')
        @self.pg.production('expression : SUM term')
        def expression_single_term(p):
            if len(p) == 2:
                if p[0].gettokentype() == 'SUB':
                    return Sub(self.builder, self.module, Number(self.builder, self.module, '0'), p[1])
                if p[0].gettokentype() == 'SUM':
                    return Sum(self.builder, self.module, Number(self.builder, self.module, '0'), p[1])
                elif p[0].gettokentype() == 'NOT':
                    return BooleanNot(self.builder, self.module, p[1])
            return p[0]

        @self.pg.production('term : term MUL factor')
        @self.pg.production('term : term DIV factor')
        def term(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)

        @self.pg.production('term : factor')
        def term_factor(p):
            return p[0]

        @self.pg.production('factor : INTEGER')
        @self.pg.production('factor : FLOAT')
        @self.pg.production('factor : LONG')
        @self.pg.production('factor : SHORT')
        @self.pg.production('factor : ID')
        @self.pg.production('factor : OPEN_PAREN expression CLOSE_PAREN')
        @self.pg.production('factor : TRUE')
        @self.pg.production('factor : FALSE')
        @self.pg.production('factor : STRING_LITERAL')
        def factor(p):
            if len(p) == 1:
                token_type = p[0].gettokentype()
                if token_type == 'INTEGER':
                    return Number(self.builder, self.module, p[0].getstr())
                elif token_type == 'FLOAT':
                    return Number(self.builder, self.module, p[0].getstr())
                elif token_type == 'LONG':
                    return Number(self.builder, self.module, p[0].getstr())
                elif token_type  == 'SHORT':
                    return Number(self.builder, self.module, p[0].getstr())
                elif token_type == 'ID':
                    var_name = p[0].getstr()
                    if var_name in self.variables:
                        return self.variables[var_name]
                    else:
                        raise ValueError(f"Undefined variable {var_name}")
                elif token_type == 'TRUE':
                    return Boolean(self.builder, self.module, 1)
                elif token_type == 'FALSE':
                    return Boolean(self.builder, self.module, 0)
                elif token_type == 'STRING_LITERAL':
                    return StringLiteral(self.builder, self.module, p[0].getstr())
            elif len(p) == 3:
                return p[1]

        @self.pg.error
        def error_handle(token):
            if token is None:
                raise ValueError('Unexpected end of input')
            raise ValueError(f'Syntax Error at token {token.gettokentype()} ({token.getstr()}) at line {token.getsourcepos().lineno}.')

    def get_parser(self):
        return self.pg.build()
 # type: ignore