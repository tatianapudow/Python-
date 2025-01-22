connection = True
while connection:
        answer=input("Есть ли подключение" + " ")
        if answer=="да":
            email_user= str(input("Введите адрес электронной почты" + " "))
            sobaka = "@"
            tochka ="."
            if sobaka and tochka in email_user:
              print("Ваш адрес подходит")

            elif sobaka or tochka in email_user:
             print("Не хватает элемента")
            else:
             print("Не подходящий адрес электронной почты")

             

        else:
           print("Попробуйте снова")     




        

       

        
