from googletrans import Translator

translator = Translator()

src = open('src.txt').read()

dst = translator.translate(src, dest='en').text

dstFile = open('dst.txt', 'w')

dstFile.write(dst)

dstFile.close()

print(dst)

