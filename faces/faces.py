# imput
fr = input ("-->")

# func to transform emojis
def emoji_replace(text):
    text_replace = text.replace(":)", "🙂").replace(":(", "🙁")
    return text_replace

# main
def main():
    fr_final = emoji_replace(fr)
    print(fr_final)

main()
