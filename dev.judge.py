import os
import subprocess
import sys

# Constants
TESTCASE_FOLDER = 'tc'

def show_test(input_data, expected_output, your_output=None):
    """Displays the test case results."""
    print(f"Input:\n{input_data}")
    print(f"Expected Output:\n{expected_output}")
    if your_output is not None:
        print(f"Your Output:\n{your_output}")

def run_test(input_file, expected_output_file, executable):
    """Runs a single test case."""
    # Read input file
    with open(input_file, 'r') as f_in:
        input_data = f_in.read().strip()

    # Execute the program with the input file
    process = subprocess.Popen(
        [executable],
        stdin=open(input_file, 'r'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    # Handle potential errors during execution
    if process.returncode != 0:
        print(f"Error: {stderr.decode().strip()}")
        return False

    # Decode and strip outputs
    program_output = stdout.decode().strip()

    # Read expected output
    with open(expected_output_file, 'r') as f_out:
        expected_output = f_out.read().strip()

    # Compare outputs and show results
    if program_output == expected_output:
        show_test(input_data, expected_output)
        return True
    else:
        show_test(input_data, expected_output, program_output)
        return False

def check_files():
    """Validates the required files and directories."""
    if len(sys.argv) != 2:
        print("Usage: python judge.py <folder_name>")
        sys.exit(1)

    # Validate test folder
    test_folder = os.path.join(os.getcwd(), TESTCASE_FOLDER, sys.argv[1])
    if not os.path.exists(test_folder):
        print(f"Test folder '{TESTCASE_FOLDER}/{sys.argv[1]}' does not exist!")
        sys.exit(1)

    # Validate executable
    executable = os.path.join(os.getcwd(), 'a.exe' if sys.platform == 'win32' else 'a.out')
    if not os.path.exists(executable):
        print("Executable file does not exist! Please compile the C++ file first.")
        sys.exit(1)

    return test_folder, executable

def main():
    """Main function to run all test cases."""
    test_folder, executable = check_files()
    test_number, passed_count, failed_count = 1, 0, 0

    while True:
        input_file = os.path.join(test_folder, f"{test_number}.in")
        expected_output_file = os.path.join(test_folder, f"{test_number}.ans")

        # Stop if test case files do not exist
        if not os.path.exists(input_file) or not os.path.exists(expected_output_file):
            break

        print(f"Running Test Case {test_number}:")
        if run_test(input_file, expected_output_file, executable):
            print(f"Test Case {test_number} PASSED!\n")
            passed_count += 1
        else:
            print(f"Test Case {test_number} FAILED!\n")
            failed_count += 1

        test_number += 1

    # Summary of results
    print(f"{passed_count} test(s) passed and {failed_count} test(s) failed.")

if __name__ == '__main__':
    main()
