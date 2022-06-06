from os.path import exists
from secrets import token_bytes

FILE = ".KEY_STORE"


def read() -> str:
    with open(FILE, mode="rb") as reader:
        return reader.read().hex()


def create():
    with open(FILE, mode="wb") as writer:
        writer.write(token_bytes(32))

    print("* NEW TOKEN GENERATED *")


if __name__ == "__main__":
    if exists(FILE):
        print(f"TOKEN={read()}")
    else:
        create()
