import os, subprocess, sys

if len(sys.argv) != 2: 
    sys.exit("Usage: python judge.py <folder_name>")

tc_folder = os.path.join(os.getcwd(), 'tc', sys.argv[1]) # you can change 'tc'
exe = os.path.join(os.getcwd(), "a.exe" if sys.platform == 'win32' else "./a.out")
if not os.path.exists(tc_folder): 
    sys.exit(f"Directory {tc_folder} not found!")
if not os.path.exists(exe):
    sys.exit("Executable not found! Compile your C++ file.")

t, p = 1, 0  # Test number, passed count
while os.path.exists(os.path.join(tc_folder, str(t) + '.in')) and os.path.exists(os.path.join(tc_folder, str(t) + '.ans')):
    print(f"Running Test {t}...")
    with open(os.path.join(tc_folder, str(t) + '.in')) as fin, open(os.path.join(tc_folder, str(t) + '.ans')) as fans:
        input_content = fin.read().strip()
        expected = fans.read().strip()
        proc = subprocess.run([exe], input=input_content, text=True, capture_output=True)
        output = proc.stdout.strip()
        if output == expected: 
            print(f"Input:\n{input_content}\nExpected:\n{expected}\nTest {t} PASSED!\n")
            p += 1
        else: 
            print(f"Input:\n{input_content}\nExpected:\n{expected}\nGot:\n{output}\nTest {t} FAILED!\n")
    t += 1
print(f"{p} test(s) passed, {t-p-1} test(s) failed!")
