import subprocess


def execute_commands(command):
    try:
        subprocess.run(command.split())
    except Exception:
        print("psh: command not found: {}".format(command))


def main():
    while True:
        command = input("$ ")
        if command.lower() == "exit":
            break
        elif command.startswith('add'):
            vars = command.split()
            try:
                print(int(vars[1]) + int(vars[2]))
            except:
                print("ERROR: You can only ADD numbers")
        elif command == 'list':
            execute_commands('ls')
        elif command == "help":
            print("LIST - lists the files in the current directory")
            print('ADD - adds the two numbers that follow the command')
            print("HELP - lists the commands available in this shell")
            print('EXIT - exits the shell')
        else:
            execute_commands(command)


if __name__ == '__main__':
    main()
