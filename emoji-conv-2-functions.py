#put into separate function
def emoji_converter(message):
    words= message.split(' ') #when meets a space, indicator to plit up string into number of wors/chars
    emojis ={
    ":)": "😊",
    ":(": "🙁",
    ":3": "😸",
    "<3": "❤",
    "^.^": "╰(*°▽°*)╯",
    ":*": "😘",
    ":P": "😋"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " " #get the key-value for word, or simply use that word instead of emoji
    return output


message = input(">")
print(emoji_converter(message))
