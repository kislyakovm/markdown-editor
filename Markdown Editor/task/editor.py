formatters = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'new-line', 'ordered-list', 'unordered-list']
user_text = []


def print_str():
    for string in user_text:
        print(string, end='')


def plain():
    global user_text

    text = input('Text: ')
    user_text.append(text)
    print_str()
    print()


def bold():
    global user_text

    text = input('Text: ')
    new_text = '**' + text + '**'
    user_text.append(new_text)
    print_str()
    print()


def italic():
    global user_text

    text = input('Text: ')
    new_text = '*' + text + '*'
    user_text.append(new_text)
    print_str()
    print()


def inline_code():
    global user_text

    text = input('Text: ')
    new_text = '`' + text + '`'
    user_text.append(new_text)
    print_str()
    print()


def link():
    global user_text

    label = input('Label: ')
    url = input('URL: ')
    new_text = f'[{label}]({url})'
    user_text.append(new_text)
    print_str()
    print()


def header():
    global user_text

    while True:
        level = int(input('Level: '))
        if level in range(1, 7):
            break
        else:
            print('The level should be within the range of 1 to 6')
            continue
    text = input('Text: ')
    new_text = f'{"#" * level} {text}\n'
    user_text.append(new_text)
    print_str()
    print()


def new_line():
    print_str()
    user_text.append('\n')
    print()
    print()


def unordered_list():
    while True:
        num_of_rows = int(input('Number of rows: '))
        if num_of_rows > 0:
            break
        else:
            print('The number of rows should be greater than zero')
            continue

    for i in range(num_of_rows):
        text = input(f'Row #{i + 1}: ')
        new_text = f'* {text}\n'
        user_text.append(new_text)
    print_str()
    print()


def ordered_list():
    while True:
        num_of_rows = int(input('Number of rows: '))
        if num_of_rows > 0:
            break
        else:
            print('The number of rows should be greater than zero')
            continue

    for i in range(num_of_rows):
        text = input(f'Row #{i + 1}: ')
        new_text = f'{i + 1}. {text}\n'
        user_text.append(new_text)
    print_str()
    print()


def write_to_file():
    file = open('output.md', 'w')
    for string in user_text:
        file.write(str(string))


while True:
    user_input = input('Choose a formatter: ')

    if user_input == '!help':
        print('''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done''')
    elif user_input == '!done':
        write_to_file()
        break
    elif user_input in formatters:
        if user_input == 'plain':
            plain()
        elif user_input == 'bold':
            bold()
        elif user_input == 'italic':
            italic()
        elif user_input == 'inline-code':
            inline_code()
        elif user_input == 'link':
            link()
        elif user_input == 'header':
            header()
        elif user_input == 'new-line':
            new_line()
        elif user_input == 'unordered-list':
            unordered_list()
        elif user_input == 'ordered-list':
            ordered_list()
    else:
        print('Unknown formatting type or command')
