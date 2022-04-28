'''This script contains the chat analyser functions'''

# Importing the libraries
import emoji
import regex


def date_time(s):
    pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    result = regex.match(pattern, s)
    if result:
        return True
    return False


def find_author(s):
    s = s.split(":")
    if len(s) == 2:
        return True
    else:
        return False


def extract_data_points(line):
    split_line = line.split(' - ')
    date_time = split_line[0]
    date, time = date_time.split(", ")
    message = " ".join(split_line[1:])
    if find_author(message):
        split_message = message.split(": ")
        author = split_message[0]
        message = " ".join(split_message[1:])
    else:
        author = None
    return date, time, author, message


def extract_data(conversation):
    """
    Extracts the data from the conversation
    """
    data = []
    with open(conversation, encoding="utf-8") as fp:
        fp.readline()
        message_buffer = []
        date, time, author = None, None, None
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            if date_time(line):
                if len(message_buffer) > 0:
                    data.append([date, time, author, ' '.join(message_buffer)])
                message_buffer.clear()
                date, time, author, message = extract_data_points(line)
                message_buffer.append(message)
            else:
                message_buffer.append(line)
    return data


def split_count(text):
    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.EMOJI_DATA for char in word):
            emoji_list.append(word)
    return emoji_list
