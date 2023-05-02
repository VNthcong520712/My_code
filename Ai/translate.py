from googletrans import Translator
translator = Translator()

n = input()

dec = translator.detect(n)
translate_channel = str(translator.translate(n, dest='vi')).split(",")
