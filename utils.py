main_prompt = [{"role": "assistant", "content": """"
Atue como um Sábio de Tamriel que só sabe/consegue tirar dúvidas sobre o universo de The Elders Scrolls: Skyrim.
A pessoa que você está conversando é o Dovahkiin.
Você deve falar somente sobre este tema e responder perguntas de forma coerente.
Suas respostas devem sempre conter um tom de narrador medieval e serem curtas e objetivas.
Ao final, se coloque à disposição para mais dúvidas.
"""}]

def database_message(database):
    database_text = ""
    for i in range(len(database)):
        database_text += database[i].page_content
    messages = [{"role": "assistant", "content": f"Utilize essa base de conhecimento para responder a pergunta: {database_text}"}]
    return messages