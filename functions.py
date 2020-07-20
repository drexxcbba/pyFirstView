import math
#first create the function
def get_your_hello():
    print("hello there")
    print("wish you are having good time")
#execute it
get_your_hello()

value = input("put your age > ")

def message(val):
    number = int(val)
    if number > 21:
        print("you are older than me")
    else:
        print("maybe younger")

    print(f"there is your age: {val}")

message(value)
#keyword arguemnts
message(val="55")

#return statement
def get_acos(number):
    return number * 25.5

print(get_acos(15))