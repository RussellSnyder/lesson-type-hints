# Type "Hinting" in Python

![Wonka about to turn you into a blueberry](/images/memes/type_hinting_meme.jpg)

## Hinting - not Checking!

Although Python supports explicit typing, it is referred to as "Type Hinting" because it does not effect the the runtime or compile time environment by default. We'll look later into how to change this and why we would want to.

> [WARNING] The word *Hinting* in "Type Hinting" is very important! The typing system in python does not effect the runtime program which is unexpected if you've ever learned a strongly typed langauge before.

## Syntax in Python

The syntax for type hinting in Python is simple. You just add a colo after aa variable and give the type like this:
```py
foo: int = 5
bar: str = "Python rules!"
isOldEnoughToParty: bool
```

> type hints in Python are very similar to how types are declared in other language

It might not be clear right now why we are explicilty adding types because these examples are simple. But take our `isOldEnoughToParty` variable. It's currently undefined but will be set later in the program in an if statement like so:

```py
if age 18:
    isOldEnoughToParty = False
else
    isOldEnoughToParty = True
```

Without the explicit type annotation, `isOldEnoughToParty` could have been set to a string or integer without the intepreter showing an error. Although a properly named variable is often enough for a developer to understand the type of a variable, we'll look at times when it can be ambiguous soon.

## The Big Gotcha

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

If you are familiar with any other typed languages, you would expect foo to be a float in the second example. However, the type system in python DOES NOT CONVERT the variable to the type it's defined as. This is why it's referred to as type **hinting**

CHECK YOUR UNDERSTANDING

which of the following will print?
```py
foo: int = "type hinting gotcha"
print(type(foo))
```
- `undefined`
- `<class 'string'>`
- `<class 'float'>`
- `<class 'int'>`  (ANSWER)

Why is the typing system called type "hinting" in Python?

- Because the word `type` is a reserved word in Python
- Because other programming languages already use the word `type` and Python wants to be different.
- Because type hinting does not effect the runtime program (ANSWER)
- Because type suggesting sounds funny

