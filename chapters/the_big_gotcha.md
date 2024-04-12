# The Big Gotcha

![Wonka about to turn you into a blueberry](/images/memes/type_hinting_meme.jpg)

## Hinting - Not Checking!

The word *Hinting* in "Type Hinting" is very important! The typing system in python does not effect the runtime program which is unexpected if you've ever learned a strongly typed language before.

## Types Are Not Enforced!

It bears repeating: the Python runtime does not enforce function and variable type annotations!

Let's look at some code examples:

```py
foo: int = 5
print(type(foo))
```
prints: `<class 'int'>`

```py
foo: float = 5
print(type(foo))
```
prints: `<class 'int'>`

If you are familiar with any other typed languages, you would expect foo to be a float in the second example. 
However, by default type hinting is merely what a developer puts for himself and other developers. Python does not actually enforces anything regarding the type without additional packages. This is why it's referred to as type **hinting**

To convert a type to a float, you must use the function `float`.

CHECK YOUR UNDERSTANDING

1. Which of the following will print?
```py
foo: int = "type hinting gotcha"
print(type(foo))
```
- `undefined`
- `<class 'string'>` (ANSWER)
- `<class 'float'>`
- `<class 'int'>`  

1. Why is the typing system called type "hinting" in Python?

- Because the word `type` is a reserved word in Python
- Because other programming languages already use the word `type` and Python wants to be different.
- Because type hinting does not effect the runtime program (ANSWER)
- Because type suggesting sounds funny

1. Given the code `is_hungry: bool = 5` what type is `is_hungry`?

- A boolean
- An Integer (Answer)
- A Float
- Not enough information to answer