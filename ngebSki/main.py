import warnings
import sys
from lexx import Lexx
from parser import Parser  # type: ignore
from CodeGen import CodeGen
import io

# Suppress specific warnings
warnings.filterwarnings("ignore")

# Redirect stderr to suppress warnings
stderr = sys.stderr
sys.stderr = io.StringIO()

# Read the input file
fname = input("Please enter the input file name: ") + ".ngeb"
with open(fname) as f:
    text_input = f.read()

# Lexical analysis
lexx = Lexx().get_lexer()
tokens = lexx.lex(text_input)

token_list = []
try:
    for token in tokens:
        token_list.append(token)
except Exception as e:
    print(f"Error: {e}")

# Code generation
codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

# Parsing
pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parsed_program = parser.parse(iter(token_list))

# Evaluate all statements in the parsed program
for statement in parsed_program:
    statement.eval()

# Create and save the IR code
codegen.create_ir()
codegen.save_ir("ngob.ll")

# Ensure the target triple is set correctly
print(f"Target triple: {codegen.module.triple}")

# Restore stderr
sys.stderr = stderr
