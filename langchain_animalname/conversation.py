from langchain.chains import LLMChain
from .input_message import input_message


def user_instruct(message: str, chain: LLMChain, end_request_phrase="おわり"):
    instruct: str = ""
    while instruct != end_request_phrase:  # end_request_phraseが入力されるとwhileを抜ける
        if instruct != "":  # 何も入力されなかった場合はLLMに処理を投げないようにしている
            print(chain.run(instruct))
        print(message, end=": ")
        instruct = input()

    else:
        print("ばいばい！")
