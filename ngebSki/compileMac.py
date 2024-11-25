# /mnt/data/compileMac.py

import subprocess
import os

def compile_to_executable(ir_filename, output_filename, filetype='obj'):
    if not os.path.exists(ir_filename):
        print(f"Error: {ir_filename} not found.")
        return False

    if filetype not in ['obj', 'asm']:
        print(f"Unsupported file type: {filetype}")
        return False

    # Determine the output file extension based on filetype
    output_extension = 'o' if filetype == 'obj' else 's'
    target_triple = 'x86_64-apple-macosx10.15.0'  # Use macOS target triple with version
    llc_command = [
        '/opt/local/libexec/llvm-11/bin/llc', 
        f'-mtriple={target_triple}', 
        f'-filetype={filetype}', 
        ir_filename, 
        '-o', 
        f'ngob.{output_extension}'
    ]

    try:
        print(f"Running LLC command: {' '.join(llc_command)}")
        subprocess.run(llc_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LLVM IR to {filetype} file: {e}")
        return False

    if filetype == 'obj':
        # Run gcc to link the object file and create the executable
        gcc_command = [
            'gcc', 
            '-target', target_triple, 
            f'ngob.{output_extension}', 
            '-o', 
            output_filename,
            '-Wl,-platform_version,macos,10.15,10.15'  # Explicitly set the platform version
        ]
        try:
            print(f"Running GCC command: {' '.join(gcc_command)}")
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
