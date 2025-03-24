from flask import Flask, render_template,url_for, request, flash
from validarsenha import validarSenha
from validarEmail import validarEmail

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/",methods=['POST','GET'])

def index():
    error = None
    if request.method == 'POST':
        email: str = request.form['email']
        senha_str: int = request.form['senha']  

        # senha_str = int(senha_str)    
        
        # Verifica se a senha não é um número
        if not senha_str.isdigit():
            error=True
            flash('⚠️ A senha não pode ser letras e deve ser maior que 8 números')
        
        # Verifica se o email não é válido
        if not validarEmail(email):
            error=True
            flash('⚠️ O e-mail fornecido é inválido.')

        print(f"📧 Email: {email}")
        print(f"🔑 Senha {senha_str}")
        print('Validando Senha: ',validarSenha(senha_str))
        print('Validando Email: ',validarEmail(email))
    return render_template('index.html',error=error)
