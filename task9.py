def exclude_elements_by_indices():
    
    my_list = [1, 44, 7, 9, 3, 2, 1, 44]
    
   
    indices = input("Введите два индекса через запятую: ")
    
   
    indices = [int(index) for index in indices.split(',')]
    
   
    new_list = [element for i, element in enumerate(my_list) if i not in indices]
    
    print(f"Список без элементов по указанным индексам: {new_list}")

exclude_elements_by_indices()
