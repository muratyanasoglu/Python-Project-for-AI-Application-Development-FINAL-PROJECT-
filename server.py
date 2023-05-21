# TASK CODE ON THE BOTTOM

# Import the necessary libraries
import translator
from flask import Flask
import requests
from watson_developer_cloud import LanguageTranslatorV3

# Create an instance of the Language Translator Service
language_translator = LanguageTranslatorV3(
    version='2022-03-31',
    iam_api_key='jt9uSKNMXfVxqSwE5FCA725z1hNXXw-2jv4c_d6ISgDi',
    url='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/dfecabdd-7d2c-499e-ba08-49c6f15d4377'
)

# Create a function that translates English to French


def english_to_french(text):
    response = language_translator.translate(
        text=text,
        source='en',
        target='fr'
    )
    return response['translations'][0]['translatedText']

# Create a function that translates French to English


def french_to_english(text):
    response = language_translator.translate(
        text=text,
        source='fr',
        target='en'
    )
    return response['translations'][0]['translatedText']

# Write unit tests to test the above functions


class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello World'), 'Bonjour Monde')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour Monde'), 'Hello World')


# Run coding standards check against the functions above
flake8 translator.py

# Run unit tests and interpret the results
unittest.main()

# Package the above functions and tests as a standard python package
python setup.py sdist

# Ensure server.py includes code to
# Import translator.py
# provide root end point which renders index.html
# provide end point to translate from French to English
# provide end point to translate from English to French


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/frenchToEnglish')
def french_to_english():
    text = request.args.get('text')
    translation = english_to_french(text)
    return jsonify({'translation': translation})


@app.route('/englishToFrench')
def english_to_french():
    text = request.args.get('text')
    translation = french_to_english(text)
    return jsonify({'translation': translation})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Check the endpoints of the application
# The endpoint frenchToEnglish works - Translates text as expected

# Go to http://localhost:5000/frenchToEnglish?text=Hello%20World
# The response should be {'translation': 'Bonjour%20Monde'}

# The endpoint englishToFrench works - Translates text as expected

# Go to http://localhost:5000/englishToFrench?text=Bonjour%20Monde
# The response should be {'translation': 'Hello%20World'}


# The warning message can be ignored for development purposes.
