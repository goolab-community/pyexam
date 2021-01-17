import subprocess
import sys
import os

if 'pyexam' not in os.listdir():
    p = subprocess.run(['git', 'clone','https://github.com/goolab-community/pyexam.git'])

sys.path.append('./pyexam')

subprocess.Popen(["py.test", "./pyexam/test.py"])
