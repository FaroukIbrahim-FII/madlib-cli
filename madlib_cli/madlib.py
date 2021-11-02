import re 
def read_template(path):
    try :
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("Error: file not found")


def parse_template(text: str):
    list = []
    selected_text = re.sub(r'\{.*?\}', '{}', text)
    result = re.findall(r'\{.*?\}', text)
    for i in result:
        list.append(i.strip("{ }"))
    list = tuple(list)
    return selected_text, list


def merge(text: str, list: tuple):
    finalText = text.format(*list)
    return finalText


def write_new_file(content: str):
    with open('assets/make_me_a_video_game_output.txt', 'w') as f:
        f.write(content)


if __name__ == "__main__":
    print("Welcome to Madlib Game\nlets start the game with adding some words:")
    itemsList = []
    textRead = read_template("assets/make_me_a_video_game_template.txt")
    text, items = parse_template(textRead)
    for i in range(0, len(items)):
        userInput = input(f'type a {items[i]}  ')
        itemsList.append(userInput)
    itemsList = tuple(itemsList)
    finalText = merge(text, itemsList)
    print(finalText)
    write_new_file(finalText)
