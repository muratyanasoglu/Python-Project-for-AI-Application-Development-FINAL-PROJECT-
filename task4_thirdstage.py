def frenchToEnglish(text):
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
