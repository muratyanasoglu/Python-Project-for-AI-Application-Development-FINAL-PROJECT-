from flask import Flask, request, jsonify
import your_package

app = Flask(__name__)


@app.route('/translate/en_to_fr', methods=['POST'])
def translate_en_to_fr():
    data = request.get_json()
    text = data.get('text')
    translation = your_package.englishToFrench(text)
    return jsonify(translation=translation)


@app.route('/translate/fr_to_en', methods=['POST'])
def translate_fr_to_en():
    data = request.get_json()
    text = data.get('text')
    translation = your_package.frenchToEnglish(text)
    return jsonify(translation=translation)


if __name__ == "__main__":
    app.run(debug=True)
