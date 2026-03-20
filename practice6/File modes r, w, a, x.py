with open("text.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Сөз саны:", len(words))



name = input("Атыңды енгіз: ")
with open("user.txt", "w") as f:
    f.write(f"Пайдаланушы: {name}")
print("Файлға жазылды!")




import datetime
with open("log.txt", "a") as f:
    now = datetime.datetime.now()
    f.write(f"Кіру уақыты: {now}\n")
print("Лог сақталды")



try:
    with open("newfile.txt", "x") as f:
        f.write("Бұл жаңа файл!")
    print("Файл құрылды")
except FileExistsError:
    print("Файл бұрыннан бар!")