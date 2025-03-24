import re

def validarEmail(email):
    # Expressão regular para validar o formato do e-mail
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(padrao, email):
        return "E-mail válido!"
    else:
        return "E-mail inválido. Por favor, insira um formato válido."