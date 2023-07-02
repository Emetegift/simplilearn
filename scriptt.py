"""
Python Scripting: scripting is the process of writing programs 
to automate tasks, and python itself is a script.
Lirary that demonstrates scripting behaviour include;
OPperating System (OS) Library
"""
import os 
# extract the current working directory
def current_directory():
    cwd = os.getcwd()
    print(cwd)
current_directory()