# Function Typing

Functions allow us to encapsulate logic in a reusable way. To use a function, we do not have to understand the code inside the function. However, we do need to know what arguments are passed into a function and the return value will be. Type hinting really helps ensure a developer knows what types go into a function and what type comes out.

## Typing Function Arguments

To add typing to function arguments, you use almost same syntax as with variables:

```py
def check_weight_limit(weight: float):
    pass
```

In this example, the argument `weight` is specified to be a `float`. Without this type, a user might input an integer causing unintended side effects (a nice phrase for bugs) in our application. 

With type hints, this danger goes away as the user will be informed that they input the wrong type.

### Exercise - Add Type Arguments

Given the following function, add type hints to function's arguments:

```py
def process_and_send_email(job_id, email, is_priority, retry_count, image_quality):
    pass
```

## Typing Functions Returns

Your colleague has written a 400 line function that starts like this:

```py
def calculate_days(start_date, end_date):
```

You want to use the function, but it is not clear what the return type will be. Will it be an integer rounded to the nearest day or a more specific float? Or maybe it will be a string like `"5 days"`?

We could look into the function body to figure out the return type, but this costs time and brain power. However, with type hints we can easily know the return type.

```py
def calculate_days(start_date, end_date) -> int:
```

Ah, it returns an integer! This is most likely the number of whole days that has passed. 

Function return type hints are very popular in 3rd party libraries (NumPy for example). It allows users of that library to safely and quickly use functions without having to look into the source code.

### Exercise - Add Type Returns

Add type returns to the following functions:

```py
def get_area_of_square(side_length: int):
    return side_length * side_length
def get_area_of_triangle(base: int, height: int):
    return base * 0.5 / height
def is_legal_age(age: int):
    return age > 18
def say_hello(name: str):
    return "hello " + name
```

## Using Type Hints to Scaffold Code

Sometimes we get wrapped up working on each individual function and forget to take a step back and think about how all the functions will work together. 

Let's say we are making an application to pay for a meal at a restaurant. We already know which functions we need and what type their arguments and return will be. Instead of completing each function one by one, we can write the scaffolding for each function using type hints:

```py
def generate_sub_total(meal_id: int) -> float:
    pass
def calculate_tax(total: float) -> float:
    pass
def apply_tax_to_total(tax_rate: float, total: float) -> float:
    pass
```

Of course none of these functions will work in their current state, this is a work in progress (WIP). But you can already see how the output of one function will fit the input of another function.

This is actually how code can look during the initial stages of a software creation practice called Test Driven Development (TDD). In TDD, you first write tests that fail and then you write the code so that they pass.

Whether you just want to remember what the arguments of a WIP are or want to use TDD, type hints help you keep better track of what the input and output of functions will be.

## Exercise - Function Planning 

Imagine you are writing software to cook pasta for you while you are out of the house. We have special sensors that can tell when water is boiled and robots that can perform basic tasks. Given the following scaffolding, what type hints would you add? 

```py
def get_home_id(user_id):
    pass
# returns an id
def start_food_request(home_id):
    pass
# returns amount of pasta needed to satisfy hunger
def get_user_hunger_level(request_id):
    pass
# determines the appropriately sized pot
# returns the id of the pot used
def choose_pot(home_id, amount_of_pasta):
    pass
def fill_pot_and_boil_water(pot_id, amount_of_pasta):
    pass
```

What other functionality could be added? Write some more pseudo code for this application. For example:

- Check the status of the pasta to see if it is ready
- Send a message to the user that the pasta is ready
- Ask the user how many people are eating the pasta and calculate the amount of pasta needed
- If there is a malfunction, send a message to the developer with the pot id that isn't working

