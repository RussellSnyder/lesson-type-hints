# Basic Type Hinting in Python

## Syntax in Python

The syntax for type hinting in Python is simple. You just add a colon after a variable and give the type like this:
```py
foo: int = 5
bar: str = "Python rules!"
is_old_enough_to_party: bool
```

> [WARNING] Examples must be done in your local IDE as type hinting is not currently supported in the code environment online.

It might not be clear right now why we are explicitly adding types because these examples are simple. But take our `is_old_enough_to_party` variable. It's currently undefined but will be set later in the program in an if statement like so:

```py
if age >= 18:
    is_old_enough_to_party = False
else
    is_old_enough_to_party = True
```

Without the explicit type annotation, `is_old_enough_to_party` could have been set to a string or integer without the interpreter showing an error. Although a properly named variable is often enough for a developer to understand the type of a variable, we'll look at times when it can be ambiguous soon.

> type hints in Python are very similar to how types are declared in other languages. So if you mater type hinting, you can quickly learn other typed languages!

> Let's try it!

Annotate the following code (about) with the appropriate types:
```py
first_name = "Joe"
last_name = "Quimby"
age = 46
weight_in_kg = 91.7
is_mayor = True
```


CHECK YOUR UNDERSTANDING

1. Why is it a good idea to give an uninitialized variable a type? (like `is_old_enough_to_party` earlier)
- [x] It reduces the chance that a wrong type will be set later
- [x] It makes your code easier to understand
- [x] So the interpreter knows what type the variable is without assigning a value
- [ ] This makes the variable less dynamic and should be avoided

1. An error is being caused by the variable weight being stored as an integer instead of a float. How can we help other developers and the interpreter undertand which type it should be?
- [x] use a type hint like so: `weight: float`
- [ ] use a type hint like so: `weight: int or float`
- [ ] use a type hint like so: `weight: int`
- [ ] use a type hint like so: `weight: float not int`

1. Which is the correct syntax for type hints in Python?
- `str my_variable`
- `my_variable => str`
- `my_variable: str` (Answer)
- `str(my_variable)`