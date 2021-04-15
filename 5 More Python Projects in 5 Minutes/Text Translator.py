from translate import Translator

translator = Translator(from_lang="english", to_lang="chinese")
translation = translator.translate("Good Morning")
print(translation)
