from email import message
import platform

version = platform.python_version()

def main():
    message()


def message():
    print("This is a Python version {}".format(version))


if __name__ == "__main__":
    main()