from .langchain_setup import setup
from .conversation import conversation


def main():
    chain = setup()
    conversation("動物", chain)


if __name__ == "__main__":
    main()
