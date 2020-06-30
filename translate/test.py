from googletrans import Translator

translator = Translator()

src = open('kor.txt').read()

dst = translator.translate(src, dest='en').text

dstFile = open('en.txt', 'w')

dstFile.write(dst)

dstFile.close()

print(dst)

