x = list(map(int, list(input("Билетик предъявите: "))))
left = sum(x[0:-3]) 
right = sum(x[-3:]) 
if left == right:
    print("Счастье в дом!")
else:
    print("Попробуй еще раз, лузер!!!")