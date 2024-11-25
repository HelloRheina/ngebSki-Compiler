import subprocess
import os

def run_main():
    try:
        subprocess.run(['python', 'main.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running main.py: {e}")
        return False
    return True

def run_compile():
    try:
        subprocess.run(['python', 'compileMac.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running compile.py: {e}")
        return False
    return True

def run_executable(output_filename):
    executable_path = f"./{output_filename}"
    if not os.path.isfile(executable_path):
        print(f"Error: {executable_path} does not exist.")
        return False
    
    try:
        subprocess.run([executable_path], check=True)
    except subprocess.CalledProcessError as e:
        return False
    return True

if __name__ == "__main__":
    ir_filename = "ngob.ll"
    output_filename = "ngob"

    if run_main():
        if os.path.isfile(ir_filename):
            if run_compile():
                run_executable(output_filename)
            else:
                print("Compilation failed.")
        else:
            print(f"Error: {ir_filename} not created.")
    else:
        print("Main script failed.")
