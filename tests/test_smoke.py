import subprocess, sys

def run(*args):
    return subprocess.run([sys.executable, "main.py", *args], capture_output=True, text=True)

def test_runs():
    res = run()
    assert res.returncode == 0
