from . import setup
from .conversation import conversation


def main():
    langchain_number = setup.choice()
    if langchain_number == "llm":
        setup.llm()
    elif langchain_number == "chat":
        setup.chat()


if __name__ == "__main__":
    main()
