import sys

from arithmetic import divide_by_x

def main():
    """Divides by three"""

    if len(sys.argv) > 1:
        print(sys.argv)
    else:
        print("You must specify exactly one argument!")


if __name__ == "__main__":
    main()