import sys

def run(c):
    if c.startWidth("text"):
        print("Executing code 2 command")
        # Add your command logic here
    else:
        print(f'{c} error code')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(" ".join(sys.argv[1:]))
    else:
        edit = input("text input: ")
        run(edit)
