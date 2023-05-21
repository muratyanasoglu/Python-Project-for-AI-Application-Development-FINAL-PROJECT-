def englishToFrench(text):
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']
