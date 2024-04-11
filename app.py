from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        EMAIL = request.form['email']
        SENHA = request.form['senha']

        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="login"
        )

        cursor = conexao.cursor()
        cursor.execute(f"select * from login where email = '{EMAIL}' and senha = '{SENHA}'")
        result = cursor.fetchall()
        cursor.close()
        conexao.close()

        if len(result) > 0:
            return ('Login efetuado com sucesso!')
        else:
            return ('Email ou senha incorretos!')

        # cursor.execute(f"INSERT INTO login (email, senha) VALUES ('{EMAIL}', '{SENHA}')")
        # conexao.commit()       

    else:
        return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)