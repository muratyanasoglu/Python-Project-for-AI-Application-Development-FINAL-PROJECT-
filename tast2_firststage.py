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
