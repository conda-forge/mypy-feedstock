from pathlib import Path
import subprocess
import sys

# from https://mypyc.readthedocs.io/en/latest/getting_started.html#example-program

Path("fib.py").write_text("""
import time

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

t0 = time.time()
fib(32)
print(time.time() - t0)
""", encoding="utf-8")

subprocess.check_call(["mypyc", "fib.py"])

subprocess.check_call([sys.executable, "-c", "import fib"])
