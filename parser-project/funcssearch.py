import json

# считывание данных
file = open('./pages/db.json', 'r', encoding='utf8')
data = json.load(file)
file.close()

# выбор частей с обязанностями
start = "Обязанности:"
end = "Требования:"
functionsvac = []
for i in range(0, len(data)):
    text = data[i]['description']
    start_index = text.find(start)
    end_index = text.find(end)
    if start_index != -1 and end_index != -1:
        start_index += len(start)
        result = text[start_index:end_index].strip()
        functionsvac.append(result)
print('done')

# разбиение части с обязанностями на сами обязанности
functions = []
for i in range(len(functionsvac)):
    if ';' in functionsvac[i]:
        functions.append(list(filter(None, functionsvac[i].split(';'))))
    elif (functionsvac[i].count(".") > 1):
        functions.append(list(filter(None, functionsvac[i].split('.'))))

print(functions)
str = ''

# форматирование для вывода
for i in range(0, len(functions)):
    for j in range(0, len(functions[i])):
        if any(i.isalpha() for i in functions[i][j]) and len(functions[i][j]) > 1:
            str += functions[i][j].strip() + '\n'

# вывод в файл
file = open('./pages/funcs.txt', 'w', encoding='utf8')
file.write(str)
file.close()
