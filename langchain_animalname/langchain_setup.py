import os
import dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def setup():
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    llm = OpenAI(temperature=1.0, openai_api_key=OPENAI_API_KEY)
    prompt = PromptTemplate.from_template("{cute_object}の可愛い名前を5つ日本語で出力せよ。")

    return LLMChain(llm=llm, prompt=prompt)
