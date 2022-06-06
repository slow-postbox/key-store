from os.path import exists
from uvicorn import run
from dotenv import load_dotenv

if __name__ == "__main__":
    if not exists(".KEY_STORE"):
        getattr(__import__("key"), "create")()

    load_dotenv()
    run(
        app="app:app",
        host="127.0.0.1",
        port=15882,
        log_level="info"
    )
