import io


def custom_write(file_name, strings):
    f1 = open(file_name, 'w', encoding='utf-8')
    res = {}
    num_str = 1
    byte = f1.tell()
    for el in strings:
        f1.write(el + "\n")
        res[num_str, byte] = el
        num_str += 1
        byte = f1.tell()
    f1.close()
    return res


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
