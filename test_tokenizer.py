from BasicTokenizer import BasicTokenizer
import os

def unpack(text):
    if text.startswith("FILE:"):
        dirname = os.path.dirname(os.path.abspath(__file__))
        taylorswift_file = os.path.join(dirname, text[5:])
        contents = open(taylorswift_file, "r", encoding="utf-8").read()
        return contents
    else:
        return text

text = open("taylorswift.txt", "r", encoding="utf-8").read()
os.makedirs("models", exist_ok=True)

for TokenizerClass, name in zip([BasicTokenizer], ["basic"]):
    tokenizer = TokenizerClass()
    tokenizer.train(text, 512, verbose=True)

    prefix = os.path.join("models", name)
    tokenizer.save(prefix)