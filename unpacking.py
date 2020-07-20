coordinates = [1, 2, 3]
#kind similar as desctructing in javascript
x , y , z = coordinates
print(z)

#dictionary part, its very similar as object literal in javascript but i think this doesnt have
#the same properties in javascript likewise this should have awesome things.
customer = {
    "name": "Rodrigo",
    "l_name": "Villarroel",
    "age": 21
}

print(customer["l_name"])
print(customer.get("age"))
customer["age"] = 19
print(customer["age"])
