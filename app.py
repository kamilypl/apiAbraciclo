from flask import Flask, request, jsonify
import requests
import pdfplumber
import io

app = Flask(__name__)

@app.route("/extrair_pdf", methods=["POST"])
def extrair_pdf():
    url = request.json.get("url")
    if not url:
        return {"erro": "URL não fornecida"}, 400

    response = requests.get(url)
    pdf = pdfplumber.open(io.BytesIO(response.content))
    
    texto = ""
    for page in pdf.pages:
        texto += page.extract_text() + "\n"

    pdf.close()
    
    return jsonify({"conteudo": texto})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
