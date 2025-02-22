lst= [17,4,7,10,11,12]
num = int(input("Введите число"))
diff=max(lst)-num
targer = 0


for i in lst:
    if abs(i-num)<=diff:
      diff= abs(i-num)
      targer=i
print("Искомое число", targer )
 