# /mnt/data/compileWin.py

import subprocess

def compile_to_executable(ir_filename, output_filename, filetype='obj'):
    if filetype not in ['obj', 'asm']:
        print(f"Unsupported file type: {filetype}")
        return False

    llc_command = ['llc', f'-filetype={filetype}', ir_filename]
    try:
        subprocess.run(llc_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LLVM IR to {filetype} file: {e}")
        return False

    if filetype == 'obj':
        obj_filename = f"{ir_filename.replace('.ll', '.o')}"
        gcc_command = ['gcc', obj_filename, '-o', output_filename]
        try:
            subprocess.run(gcc_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error linking object file to executable: {e}")
            return False
    else:
        print(f"{output_filename}.s file generated successfully.")
    
    return True

if __name__ == "__main__":
    ir_filename = "ngob.ll"
    output_filename = "ngob"
    filetype = input("Enter the file type to generate (obj/asm): ").strip().lower()
    success = compile_to_executable(ir_filename, output_filename, filetype)

    if not success:
        print("Compilation failed.")
