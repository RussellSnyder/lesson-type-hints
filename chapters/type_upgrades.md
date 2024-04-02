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

Why doesn't Python throw an error when adding an integer and a float like it does when adding a integer to a string? Well, the answer is not so technical. This is actually a language design choice the creators of Python have made. 

> Note Not Everything in Tech is Technical
> Some reasons why code works the way it does is based on historical limitations on computers. But sometimes, it's just a design choice. A computer language, like a real language, is a changing and evolving system. New technology and trends rise and some languages choose to include those features while other do not.


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

4. Why does Python use Type Upgrades
- [x] To enable developers to be as productive as possible
- [ ] There are technical limitations forcing type upgrades
- [ ] Integers are 'first class' citizens allowing for upgrades
- [ ] Python does not use type upgrades