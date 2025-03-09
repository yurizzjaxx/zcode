import sys
import pyfiglet as p

def run(c):
    if c.startWidth("text"):
        out = p.figlet_format(c, font = 'isometric1')  
        print(out)
    else:
        print(f'{c} error blank text')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(" ".join(sys.argv[1:]))
    else:
        edit = input("text input: ")
        run(edit)
