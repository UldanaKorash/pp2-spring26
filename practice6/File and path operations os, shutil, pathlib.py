import os
files = [f for f in os.listdir(".") if os.path.isfile(f)]
print(files)


import os
os.mkdir("test_dir")
os.rmdir("test_dir")


import shutil
shutil.copy("a.txt", "b.txt")
shutil.move("b.txt", "folder/b.txt")


from pathlib import Path
p = Path("example.txt")
p.write_text("hello")
print(p.read_text())