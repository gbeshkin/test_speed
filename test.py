import subprocess

user_input = "ls"
x = eval(user_input)
subprocess.run("ls", shell=True)
