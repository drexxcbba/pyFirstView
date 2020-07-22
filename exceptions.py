try:
    number = int(input("put a number > "))
    aux = 550
    val = aux / number
    print(number)
except ZeroDivisionError:
    print("invalid number")
except ValueError:
    print("ivalid number")
