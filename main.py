from translate import Translator
translator=Translator(to_lang="ja")
with open("test.txt",mode="w") as my_file:
    my_file.write("Computer programming is the process of writing instructions that get executed by computers. The instructions, also known as code, are written in a programming language which the computer can understand and use to perform a task or solve a problem.")

with open("test.txt") as my_file:
    text=my_file.read()
    translation=translator.translate(text)
    with open("ja.txt",mode="w",encoding="utf-8") as ja_file:
        ja_file.write(translation)
