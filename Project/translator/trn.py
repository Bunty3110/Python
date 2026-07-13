from translate import Translator

tran = Translator(to_lang="ja")

try:
    with open('./minor projects/translator/text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    translation = tran.translate(text)

    with open('./minor projects/translator/translated_text.txt', 'w', encoding='utf-8') as translated_file:
        translated_file.write(translation)

    print("Translation successful!")

except FileNotFoundError:
    print("The file was not found. Please check the file path and try again.")