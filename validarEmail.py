import re

def validarEmailUsuario(email: str):
     padrao = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
     return re.match(padrao, email) is not None
