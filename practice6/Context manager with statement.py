with open("a.txt", "r") as f1, open("b.txt", "w") as f2:
    f2.write(f1.read())



try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("error")



class Manager:
    def __enter__(self):
        print("start")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("end")

with Manager():
    print("inside")