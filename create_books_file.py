import os

outfile=open("./books.txt",'w',encoding="utf16")
for file_name in os.listdir("C:/Users/loren/Documents/Lorenzo/UniPi/BookCorpus/out_txts"):
    with open("C:/Users/loren/Documents/Lorenzo/UniPi/BookCorpus/out_txts/"+file_name,encoding="utf8") as file:
        outfile.write(file.read())
outfile.close()