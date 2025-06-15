from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'visitante')  # se não passar um nome, usa visitante
    return jsonify({"mensagem": f"Olá, {nome}!"})

# POST /soma
@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    a = dados.get('a')
    b = dados.get('b')

    if a is None or b is None:
        return jsonify({"erro": "Você precisa enviar os dois números 'a' e 'b'"}), 400

    resultado = a + b
    return jsonify({"soma": resultado})

if __name__ == '__main__':
    app.run(debug=True)
