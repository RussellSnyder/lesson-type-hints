# pretend this is returned from a database query
# user = {
#     "id": 5,
#     "name": "John Doe",
# }

# id = user["id"]

# print("received id: " + id)
# This throws an error because id is not a string

from typing import TypedDict

class User(TypedDict):
    id: int
    name: str

# user: User = {
#     "id": 5,
#     "name": "John Doe",
# }
# user: dict[str, int | str] = {
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






# foo: int = "type hinting gotcha"
# print(type(foo))

check = float(5)
# Simple example

first_name = "German"
last_name = "Hacker"
age = 30
weight_in_kg = 96.5
is_mayor = True

# def calculate_days(start_date, end_date) -> int:
#     number_of_days = None
#     # logic here to assign number_of_days
#     return number_of_days

# def generate_total(meal_id: int) -> float:
#     pass
# def calculate_tax(total: float) -> float:
#     pass
# # returns the percentage a customer wants to tip
# def ask_for_tip_rate_amount() -> int:
#     pass
# def apply_tip_to_total(tip_rate: int, total: float) -> float:
#     pass


def get_total(checkout_complete: bool) -> float | str:
    if not checkout_complete:
        return "Checkout is not yet complete"
    return 100.75

total_or_error_message = get_total(True)

print("your total is" + total_or_error_message)

if (type(total_or_error_message) == float):
    total = total_or_error_message
    print("your total is" + str(total))
    

elif (type(total_or_error_message) == str):
    error_message = total_or_error_message
    print(error_message)

from typing import Optional

def is_ready_to_party(age: Optional[int]) -> Optional[bool]:
    if age == None or age < 0:
        print("Are you a human?")
        return None
    return age > 18

def calculate_area(side_length: int | None):
    if side_length is None:
        return "You did not enter a side length!"
    return side_length * side_length

def divide_7_by_number(number: int | None):
    if number == None:
        print("You did not enter a number!")
        return None
    if number == 0:
        print("Cannot divide by 0")
        return None
    return 7 / number
