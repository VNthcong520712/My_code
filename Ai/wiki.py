import wikipedia

wikipedia.set_lang("vi")

about = input()
con = wikipedia.summary(about).split("\n")
print(con[0])