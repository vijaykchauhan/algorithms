

def reverse_string(str):
    result = ''
    for index in range(len(str) - 1, -1, -1):
        char = str[index]
        result += char
    print(result)
    return result

def reverse_string_tuple(str):
    return ''.join(c for c in str[::-1])

def reverse_string_inbuilt(str):
    return ''.join(reversed(str))

if __name__ == '__main__':
    assert reverse_string('abcdefghijklmnopqrstuvwxyz') == 'zyxwvutsrqponmlkjihgfedcba'
    assert reverse_string(reverse_string('I am a programmer')) == 'I am a programmer'
    assert reverse_string_inbuilt('hello') == 'olleh'
