# 🖥️ Ngebski Programming Language and Compiler🌟  

**_"Ngeb"_** is an Indonesian slang word for addressing friends, and that's what the Ngebski language aims to be: your friendly, user-focused programming language. Blending elements of **C** and **Python**. 

---

## ✨ Goals of the Ngebski Compiler  

The **Ngebski Compiler Project** build:  

- **Efficient Compilation:** For the custom-designed Ngebski programming language.  
- **Core Objectives:**  
  - Break down source code into **tokens** (lexer).  
  - Construct **parse trees** and **ASTs** (parser).  
  - Perform **semantic checks** to enforce language rules.  
  - Generate **intermediate code** and optimized machine code using **LLVM**.  
- **Language Features:**  
  - Variable declarations, arithmetic and boolean operations, `if-then-else`, and `while` loops.  
- **Testing:** Build a robust suite of test cases to ensure the compiler handles various constructs.  

---

## 🌟 Why Ngebski?  

- **Simple:** Intuitive syntax for beginners.  
- **Efficient:** Built with optimization in mind using LLVM.  
- **Cross-Platform:** Supports macOS and Windows.  
- **Fun:** A project to learn, grow, and enjoy!  

---

## 🛠️ Features  

**Language Constructs:**  
- Assignments, arithmetic expressions, conditional statements, and loops.  
- Boolean operations and string output.  

**Data Types:**  
- Supports **integers** and **floats**.  

**Code Generation:**  
- Generates LLVM IR for optimized machine code.  

**Test Cases:**  
Includes sample programs like:  
- `string.ngeb`  
- `arithmetic1.ngeb`, `arithmetic2.ngeb`  
- `boolean.ngeb`  
- `conditional.ngeb`, `IfThenElse.ngeb`  
- `integration.ngeb`, `variable.ngeb`, `while.ngeb`  

---

## 💻 Prerequisites  

**Environment:**  
- Python 3.12  
- Visual Studio Code  

**For Windows Users:**  
- Add `___chkstk_ms` to the OS standard library.  

**Libraries:**  
- `rply`  
- `llvm`
- `llc`  

---

## 🛠️ How to Build and Run  

1. Clone this repo:  
   ```bash  
   git clone https://github.com/HelloRheina/NgebskiCompiler

2. Navigate to the project directory:  
   ```bash
   cd NgebskiCompiler
3. Set up virtual environment and Install the requirements
   ```bash
   conda create --name ngebski python=3.12
   conda activate ngebski
   pip install -r requirements.txt
4. Compile and run your first Ngebski program:
   ```bash
   Sample: (terminal entry by line)
   cd ngebSki
   python main.py
   ./test/arithmetic1
   #ngob.ll generated
   python compileWin.py
   #There are two files with different OS, choose the compile file based on your OS
   obj
   #We provide assembly code generator (asm) and object generator (obj)
   ./ngob
   #Run the executable
   #For one click compile and run, execution[OS].py is provided
   
   

## 🧪 Test Cases  

The Ngebski compiler comes with built-in test cases to ensure reliability and handle different language constructs. Here’s what you can test:  

- **String Output:** `string.ngeb`  
- **Arithmetic Operations:** `arithmetic1.ngeb`, `arithmetic2.ngeb`  
- **Boolean Logic:** `boolean.ngeb`  
- **Conditionals:** `conditional.ngeb`, `IfThenElse.ngeb`  
- **Variable Operations:** `variable.ngeb`  
- **Loops:** `while.ngeb`  
- **Integrated Programs:** `integration.ngeb`  

## 🤔 FAQs
** What does "Ngebski" mean? **
It’s inspired by the Indonesian slang word "ngeb", meaning friendly or approachable. 
This language is designed to feel as natural as talking to friends!

** Which operating systems are supported? **
- **Windows 10/11** 
- **macOS** (requires adding ___chkstk_ms to the OS standard library)

Yes, we support both Windows and macOS !!

## ✨ Language description and test cases
- Please check **ngebBuild.txt** for more information. We use BNF notation to define the grammar and lexical model to describe the control flow. The build also describe the parser, lexer, AST, intermediate code generator, compile and execution.
- Please check **testCases.pdf** for information regarding test cases usage.
- Please check **performanceAnalysis.pdf** for information surrounding performance analysis and error handling.

## Compiler architecture
![compiler_architecture](https://github.com/user-attachments/assets/e27de7f0-6a69-47ae-a1b0-28ef55de3c73)
![flow](https://github.com/user-attachments/assets/0b41db58-ad62-4125-bf5e-19a103becb6b)

1. main.py is used as the body of the compiler for lexer, parser, AST and code generator for intermediate representation (IR file).
2. compile.py is used for object and assembly file generators.
3. ngob.exe is the executable of the machine code.
4. ./ngob is used to execute the file into human readable output.

## 🎉 Happy Coding with Ngebski! 🎉

Let us know if there is anything you would like to add or enhance ！

## References
We mainly refer to [A Python Compiler Created By marcelogdeandreade ](https://github.com/marcelogdeandrade/PythonCompiler), [Python RPLY Documentation](https://rply.readthedocs.io/en/latest/) and [LLVM Documentation](https://llvm.org/docs/)

