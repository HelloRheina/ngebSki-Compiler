# 🖥️ Ngebski Programming Language Compiler 🌟  

**_"Ngeb"_** is an Indonesian slang word for addressing friends, and that's what the Ngebski language aims to be: your friendly, user-focused programming language. Blending elements of **C** and **Python**, Ngebski makes programming as fun as chatting with friends.  

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

---

## 🛠️ How to Build and Run  

1. Clone this repo:  
   ```bash  
   git clone https://github.com/your-username/NgebskiCompiler.git

2. Navigate to the project directory:  
   ```bash
   cd NgebskiCompiler
3. Install the requirements
   ```bash
   pip install -r requirements.txt
4. Compile and run your first Ngebski program:
   ```bash
   python ngebski_compiler.py path/to/your_program.ngeb

## 🧪 Test Cases  

The Ngebski compiler comes with built-in test cases to ensure reliability and handle different language constructs. Here’s what you can test:  

- **String Output:** `string.ngeb`  
- **Arithmetic Operations:** `arithmetic1.ngeb`, `arithmetic2.ngeb`  
- **Boolean Logic:** `boolean.ngeb`  
- **Conditionals:** `conditional.ngeb`, `IfThenElse.ngeb`  
- **Variable Operations:** `variable.ngeb`  
- **Loops:** `while.ngeb`  
- **Integrated Programs:** `integration.ngeb`  

Run test cases like this:  
```bash
python ngebski_compiler.py test_cases/arithmetic1.ngeb
```

## 🤔 FAQs
** What does "Ngebski" mean? **
It’s inspired by the Indonesian slang word "ngeb", meaning friendly or approachable. 
This language is designed to feel as natural as talking to friends!

** Which operating systems are supported? **
- **Windows 10/11** 
- **macOS** (requires adding ___chkstk_ms to the OS standard library)




