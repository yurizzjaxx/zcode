import sys

def run(c):
    if c == "code 2":
        print("Executing code 2 command")
        # Add your command logic here
    else:
        print(c)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(" ".join(sys.argv[1:]))
    else:
        edit = input("code(##)")
        run(edit)
