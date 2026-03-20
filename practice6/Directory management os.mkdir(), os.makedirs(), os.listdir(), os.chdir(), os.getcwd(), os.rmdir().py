import os
os.mkdir("mydir")
print(os.listdir("."))


import os
print(os.getcwd())
os.chdir("..")
print(os.getcwd())


import os
os.mkdir("temp")
os.rmdir("temp")