# Type Upgrades

## What is a Type Upgrade?

When operations are done on values of the same type, the result is usually of the same type. For example, `"Hello" + "World"` will result is a string and `1 + 2` an integer.

However, when values of different types are operated on, Python may upgrade the less precise value. 

This is easy to see when doing operations between an integer and a float:
```py
print(1 + 2)   # outputs integer
print(1 + 2.0) # outputs float
print(4 / 2.0) # outputs float
print(4 / 2)   # outputs float
```

## Why Type Upgrade and not Error?

Why doesn't Python throw an error when adding an integer and a float like it does when adding a integer to a string? The answer is not so technical, it is simply a choice that the creators of Python have made.

## Make Your Own Type Upgrades If You Want

Just as Python makes the decision to upgrade certain types, you can overload the  

```py
class AlwaysFloat(object):
    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other_value):
        return self.value + other_value

print(AlwaysFloat(2) + 3)
# will always print a float even through only integers were input
```

EXCERISE
Create a class that only returns integers when divided by another integer. Round the number down is a float is received.


CHECK YOUR UNDERSTANDING

1. Why is does `1 + 1.0` equal `2.0` and not `2` in Python?
- This is a fundamental in computer science
- Modern banking would break otherwise
- This is a design choice in Python (ANSWER)
- Because Python is weakly typed

2. What type is returned when running `print(1/2)`
-  float (ANSWER)
-  int
-  string
-  class

3. What happens when you run `print(1 + '2')`
-  There will be an error (ANSWER)
-  Python upgrade the string to an integer
-  Python downgrades the integer to a string
-  The string '12' is printed 