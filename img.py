import json
def check_words(word):
    word = word.split('\n')
    word = [element for element in word if element != '']

    print(word)

    with open('list.txt', 'r') as file:
        text = json.loads(file.read())
    if word[0] in text:
        return text[word[0]]
    else:
        if len(word) < 2:
            return 'bed1'
        else:
            text.update({word[1]: word[0]})
            with open('list.txt', 'w') as file:
                file.write(json.dumps(text))
            return 'bed1'
