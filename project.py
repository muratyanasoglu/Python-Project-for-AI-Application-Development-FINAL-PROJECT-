import your_package
from flask import Flask, request, jsonify
import unittest
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(
    'jt9uSKNMXfVxqSwE5FCA725z1hNXXw-2jv4c_d6ISgDi')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(
    'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/dfecabdd-7d2c-499e-ba08-49c6f15d4377')


def englishToFrench(text):
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']


def frenchToEnglish(text):
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']


class TestTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()


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
