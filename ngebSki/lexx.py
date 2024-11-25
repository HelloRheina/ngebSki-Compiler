# /mnt/data/lexx.py

from rply import LexerGenerator

class Lexx():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # If-Then-Else
        self.lexer.add('IF', r'if')
        self.lexer.add('THEN', r'then')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('END', r'end')
        # Number types
        self.lexer.add('FLOAT', r'-?\d+\.\d+')
        self.lexer.add('LONG', r'-?\d{10,}')
        self.lexer.add('INTEGER', r'-?\d+')
        self.lexer.add('SHORT', r'-?\d{1,4}')
        # Boolean literals (prioritized over ID)
        self.lexer.add('TRUE', r'true')
        self.lexer.add('FALSE', r'false')
        # Boolean operators
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')
        self.lexer.add('NOT', r'not')
        # Print
        self.lexer.add('PRINT', r'ngeb')
        # While loop
        self.lexer.add('WHILE', r'while')
        self.lexer.add('DO', r'do')
        # Comparison operators
        self.lexer.add('EQ', r'==')
        self.lexer.add('NEQ', r'!=')
        self.lexer.add('LEQ', r'<=')
        self.lexer.add('GEQ', r'>=')
        self.lexer.add('LT', r'<')
        self.lexer.add('GT', r'>')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'ski')
        self.lexer.add('SEMI_COLON', r';')
        # Increment and decrement
        self.lexer.add('INCREMENT', r'\+\+')
        self.lexer.add('DECREMENT', r'\-\-')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        # Identifier (variable name)
        self.lexer.add('ID', r'[a-zA-Z_][a-zA-Z0-9_]*')
        # Assignment
        self.lexer.add('EQUALS', r'\=')
        # String literal
        self.lexer.add('STRING_LITERAL', r'"[^"]*"')
        # Ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
