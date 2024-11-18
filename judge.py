import os
import subprocess
import sys

def run_test(input_file, expected_output_file):
    executable = 'a.exe' if sys.platform == 'win32' else 'a.out'
    with open(input_file, 'r') as f_in:
        process = subprocess.Popen([os.path.join(os.getcwd(), executable)], stdin=f_in, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
    
    with open(expected_output_file, "r") as f_out:
        expected_output = f_out.read()

    return stdout.decode().strip() == expected_output.strip()

def main():
    if len(sys.argv) != 2:
        print("Usage: python judge.py <folder_name>")
        sys.exit(1)
    
    test_folder = os.path.join(os.getcwd(), 'tc', sys.argv[1])
    if not os.path.exists(test_folder):
        print(f"Test folder tc/{sys.argv[1]} does not exist!")
        sys.exit(1)
    
    testNum = 1
    passNum = 0
    faildNum = 0
    while True:
        input_file = os.path.join(test_folder, str(testNum) + '.in')
        expected_output_file = os.path.join(test_folder, str(testNum) + '.ans')
        if not os.path.exists(input_file) or not os.path.exists(expected_output_file):
            break
       
        if run_test(input_file, expected_output_file):
            print(f"Test {testNum} passed!")
            passNum += 1
        else:
            print(f"Test {testNum} failed!")
            faildNum += 1
        
        testNum += 1
    print(f'\n{passNum} test passed and {faildNum} test failed!')
                
if __name__ == '__main__':
    main()
