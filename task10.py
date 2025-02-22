def count_trailing_zeros():
    num = int(input("Введите число: "))
    
    
    str_num = str(num)
    
    
    zeros_count = 0
    
    
    for char in reversed(str_num):
        if char == '0':
            zeros_count += 1
        else:
            break
    
    print(f"Количество нулей в конце числа: {zeros_count}")

count_trailing_zeros()