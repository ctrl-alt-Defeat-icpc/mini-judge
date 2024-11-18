# Mini Judge Program
Mini Judge is a lightweight program designed to test the correctness of a compiled executable (`a.out` or `a.exe`) against a set of predefined test cases. This program works on both **Windows** and **Linux/Ubuntu** platforms.

## Features
* Executes a compiled C++ program (`a.out` or `a.exe`) with input files.
* Compares the output with the expected results stored in `.ans` files.
* Supports test case organization for easy management.

## Prerequisites
1. Python 3.x: Ensure Python is installed and added to your system's PATH.
2. C++ Compiler: To compile your C++ program:
  * On Linux/Ubuntu: Use g++ or clang++.
  * On Windows: Use MinGW or Visual Studio.

## Folder Structure
The program expects the following folder structure:
```bash
mini-judge/
├── judge.py        # Main Python script to run the tests
├── a.out           # Compiled C++ program (output) maybe a.exe
├── tc/             # Test case folder
│   ├── a/          # Test case subfolder (e.g., "a" is the problem name)
│   │   ├── 1.in    # Input file for test case 1
│   │   ├── 1.ans   # Expected output for test case 1
│   │   ├── 2.in    # Input file for test case 2
│   │   ├── 2.ans   # Expected output for test case 2
│   └── ...         # Additional problem folders (b/, c/, etc.)
```

<details><summary><strong>Test Case Structure</strong></summary>

Each test case should have:
**Input file (`.in`)**: Contains the input data for the test case.
**Answer file (`.ans`)**: Contains the expected output.

For example:
- `1.in`:
    ```bash
    5 10
    ```
- `1.ans`:
    ```bash
    15
    ```
</details>

## How to use
### 1. Compile the C++ Program
Compile your C++ program into an executable file
```bash
g++ a.cpp
```

### 2. Run the Judge Script
Run the `judge.py` script and specify the problem name (e.g., `a`):
```bash
python judge.py a
```
***hint: maybe you should use `python3` instead `python`.***

The script will:
1. Look for test cases in `tc/a/`.
2. Run the executable (`a.out` or `a.exe`) for each `.in` file.
3. Compare the program's output with the corresponding `.ans` file.
4. Print whether each test case **passed** or **failed**.

## Cross-Platform Notes
The script automatically detects the operating system and selects `a.out` (Linux/Ubuntu) or `a.exe` (Windows).
Ensure the `a.out` or `a.exe` executable is in the same directory as `judge.py`.

## Troubleshooting
1. **Executable not found**: Ensure `a.out` or `a.exe` is in the correct directory.
2. **Mismatched outputs**: Verify your program logic and ensure `.ans` files are correct.
3. **File naming issues**: Ensure .in and `.ans` file names match the required format (e.g., `1.in` and `1.ans`).

## License
This project is licensed under the [MIT License](./LICENSE).

## Advanced Version
Looking for a more complex and feature-rich version of this project? **check this [repo +](https://github.com/EnAnsari/cph)**