string = input('Введите строку ')
start_sign = input("Введите первый символ ")
end_sign = input("Введите второй символ ")

start_index = string.index(start_sign)
end_index=string.index(end_sign)
print(string[start_index+1:end_index])