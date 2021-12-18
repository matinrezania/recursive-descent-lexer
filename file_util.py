index = -1
previous_char = ''
current_char = ''
file = open("code.txt", "r")
buffer_size = 10
buffer_index = -1
buffer = ''


def get_char():
    global index, buffer, buffer_size, buffer_index
    global previous_char, current_char, index
    previous_char = current_char

    if buffer_index == -1:
        if buffer == '':  # at the beginning of the program. it needs to get initiated
            buffer = file.read(buffer_size)
        buffer_index += 1

    if buffer_index >= buffer_size:
        buffer_index = 0
        buffer = file.read(buffer_size)
        # print('BUFFER', buffer)

    if buffer_size != len(buffer) and buffer_index == len(buffer):
        # print('reached end of file')
        return '\0'


    current_char = buffer[buffer_index]
    char = current_char

    buffer_index += 1
    index += 1
    return char


def unget_char():
    global index, buffer_size, buffer_index
    global previous_char, current_char, index
    current_char = previous_char
    previous_char = ''

    buffer_index -= 1
    index -= 1


def close_the_file():
    file.close()