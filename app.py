from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", success_message=None)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        msg = request.form.get('msg')
        
       
        
        success_message = "Envio do formulário com sucesso!"
        return render_template('index.html', success_message=success_message)

if __name__ == "__main__":
    app.run(debug=True)
