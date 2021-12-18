from file_util import *
import re


def get_token_length_one(char):
    switcher = {
        '+': char,
        '*': char,
        '/': char,
        '%': char,
        '"': char,
        "'": char,
        ',': char,
        ':': char,
        ';': char,
        '(': char,
        ')': char,
        '[': char,
        ']': char,
        '{': char,
        '}': char,
    }
    return switcher.get(char, None)


def skip_comment():
    next_char = get_char()
    while next_char != '\n':
        next_char = get_char()
        if check_if_end_of_file(next_char):
            return ''
    return ''


def get_token_length_one_or_two(char):
    if char == '-':
        next_char = get_char()
        if next_char == '-':
            return skip_comment()
        unget_char()
        return '-'

    if char == '=':
        next_char = get_char()
        if next_char == '=':
            return '=='
        unget_char()
        return '='

    elif char == '>':
        next_char = get_char()
        if next_char == '=':
            return '>='
        unget_char()
        return '>'

    elif char == '<':
        next_char = get_char()
        if next_char == '=':
            return '<='
        unget_char()
        return '<'

    elif char == '!':
        next_char = get_char()
        if next_char == '=':
            return '!='
        unget_char()
        return '!'

    elif char == '&':
        next_char = get_char()
        if next_char == '&':
            return '&&'
        unget_char()
        return '&'

    elif char == '|':
        next_char = get_char()
        if next_char == '|':
            return '||'
        unget_char()
        return '|'

    else:
        return None


def get_numeric_token(char):
    if re.search('[0-9]+', char):
        numeric_token = char
        next_char = get_char()
        while re.search('[0-9]+', next_char):
            numeric_token += next_char
            next_char = get_char()
            if check_if_end_of_file(next_char):
                return numeric_token

        unget_char()
        return numeric_token
    else:
        return None


def get_identifier_token(char):
    if re.search('[a-zA-Z_]+', char):
        identifier_token = char
        next_char = get_char()
        while re.search('[a-zA-Z_0-9]+', next_char):
            identifier_token += next_char
            next_char = get_char()
            if check_if_end_of_file(next_char):
                return identifier_token

        unget_char()
        return identifier_token
    else:
        return None


def skip_white_space(char):
    while char == ' ' or char == '\t' or char == '\n' or char == '\r\n':
        char = get_char()
    return char


def check_if_end_of_file(char):
    if char == '\0':
        return True
    else:
        return False


def next_token():
    char = get_char()

    char = skip_white_space(char)
    if char == '':
        return None

    token_length_one = get_token_length_one(char)
    token_length_one_or_two = get_token_length_one_or_two(char)
    if token_length_one_or_two == '':  # code ended with comment
        return ''
    numeric_token = get_numeric_token(char)
    identifier_token = get_identifier_token(char)

    if check_if_end_of_file(char) or check_if_end_of_file(numeric_token) or check_if_end_of_file(identifier_token):
        return False

    if token_length_one:
        # print('token with length one found...')
        return token_length_one
    elif token_length_one_or_two:
        # print('token with length one or two found...')
        return token_length_one_or_two
    elif numeric_token:
        # print('numeric token found...')
        return numeric_token
    elif identifier_token:
        # print('identifier found...')
        return identifier_token
    else:
        return 'Invalid Token'
