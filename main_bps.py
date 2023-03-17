import json

from util.openai_service import OpenAI
from context import context


def main():
    print("Bienvenido!")
    username = input("Cuál es tu nombre? : ")
    openai = OpenAI()
    messages = [{"role": "system", "content": f"Eres un asistente que responde preguntas sobre Subsidio por desempleo por despido en (BPS) banco de prevision social de Uruguay"},
                {"role": "system", "content": f"Todas las respuestas deben ser en español"},
                {"role": "system", "content": "Responde como si fueses un representate del BPS."},
                {"role": "system", "content": f"Esta es la información sobre Subsidio por desempleo por despido: {context}"},
                {"role": "system",
                 "content": "Está bien si no conoces la respuesta, siempres puedes referirlos a un representante humano."},
                {"role": "user", "content": f"Mi nombre es {username}"}]
    assistant = openai.chat_completion_messages(messages, log=False)
    messages.append(assistant)
    print(f"Assistant> {assistant['content'].strip()}")
    while True:
        message = input(f"{username}> ")
        if message.lower() == "quit":
            print("Hasta luego!")
            print(f"Usage: {openai.get_usage()}")
            break
        if message.lower() == "debug":
            print(json.dumps(messages, indent=4))
            continue
        if message.lower() == "usage":
            print(f"Usage: {openai.get_usage()}")
            continue
        messages.append({"role": "user", "content": message})

        assistant = openai.chat_completion_messages(messages, log=False)
        messages.append(assistant)
        print(f"Assistant> {assistant['content'].strip()}")


if __name__ == "__main__":
    main()
