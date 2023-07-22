import dotenv
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def input_animal():
    print('好きな動物を入力してください。かわいい名前をかんがえるよ。\n動物の種類を入力(「おわり」で終了)：',end='')
    return input()

def main():

    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    llm = OpenAI(temperature=1.0)
    prompt = PromptTemplate.from_template('{animal}の可愛い名前を5つ日本語で出力せよ。')

    chain = LLMChain(llm=llm, prompt=prompt)

    end_request = False

    while end_request == False:
        animal = input_animal()
        if animal == 'おわり':
            end_request = True
            continue
        print(chain.run(animal))

    print('ばいばい！')

if __name__ == '__main__':
    main()