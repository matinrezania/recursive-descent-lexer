from token_util import *

tokens = []


def add_token_if_valid(token):
    if token:
        tokens.append(token)
        print(token)


token = next_token()
add_token_if_valid(token)

while token or token == '':
    token = next_token()
    add_token_if_valid(token)
# print(tokens)

close_the_file()
