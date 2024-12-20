from utils.load_dotenv import *
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

gemini = GoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_api_key)

while True:
    os.system("cls")
    print("==== Iniciando ChatBot ====")
    print("Digite 'sair' para sair do ChatBot")
    prompt = str(input("Qual a sua pergunta? "))

    if prompt == "sair":
        break

    output_parser = StrOutputParser()
    chain = gemini | output_parser
    response = chain.invoke(prompt)
    print(response)