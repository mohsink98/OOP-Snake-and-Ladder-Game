import os, time

os.system("cls")
filenames = ["animation1.txt", "animation2.txt"]
frames = []

for name in filenames:
    with open(name, 'r', encoding="utf8") as f:
        frames.append(f.readlines())

def command_input():
    print('''
                                        Press 'S' to start    -       Press 'E' to exit
    ''')
    command = input("\t\t\t\t\tEnter your choice - ")
    return command

def main_func():
    os.system("cls")
    while True:
        for i in range(4):
            for frame in frames:
                print("".join(frame))
                time.sleep(0.15)
                os.system('cls')
        f = open("animation2.txt", 'r', encoding="utf8")
        file_content = f.read()
        print(file_content)
        command = command_input()
        return command

