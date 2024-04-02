# pretend this is returned from a database query
# user = {
#     "id": 5,
#     "name": "John Doe",
# }

# id = user["id"]

# print("received id: " + id)
# This throws an error because id is not a string

# from typing import TypedDict

# class User(TypedDict):
#     id: int
#     name: str

# user: User = {
#     "id": 5,
#     "name": "John Doe",
# }


# id = user["id"]

# print("received id: " + id)

# test: float = 5
# print(test)
# print(type(test))

foo = 5
bar = "yolo"

print(4 + 2)
# print(4 + '2')
# prints 6 and then throws an error
print (4 + 1.1)

print(1 / 2)

class AlwaysFloat(object):
    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other_value):
        return self.value + other_value

print(AlwaysFloat(2) + 3)
