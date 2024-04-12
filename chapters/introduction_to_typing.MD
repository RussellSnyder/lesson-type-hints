# Introduction to Typing

![dad joke about types dating](/images/memes/type_dating_meme.jpg)

## What is Typing?

Typing is a way to give either your compiler, interpreter or another developer more information about your code. Details such as:

- What type a variable or property is 
- What shape data will be
- What type of arguments a function takes and what type does it return

## Why is Typing Helpful?

Typing can help catch bugs early in the development process. When variables are typed, Python can highlight errors in your IDE **before** running your program. This saves time (and headaches) debugging programs later in the development process.

The classic example in Python is adding a string to an integer:

```py
foo = 5
bar = '10'
print(foo + bar)
```

This example will fail when running your program as a string cannot be added to an integer in Python. However, with type checking on, your IDE will highlight the error like this:

![error highlighting in Python](/images/code_snippets/error_highlighting.png)

When hovering over the highlighted code, we even get the exact error that this code has:

![error highlighting in Python](/images/code_snippets/error_fix_suggestion.png)

Not only does our IDE tell us there is an error, but it tells us how to fix there error all without running our program!

> Vocabulary "Type Safety"
> Refers to the degree in which a programming language enforces what operations can be performed on what types of data.
> Javascript is less type safe than Python because it allows integers and strings to be added together by *implicitly converting* the integer to a string. Java is more type safe than Python because it uses a static typing systems.
> Type safety is a continuum and does not mean one language is better or worse than another: just different.


CHECK YOUR UNDERSTANDING

1. Which of the following are reasons to use a typing system

- [x] To help another developer understand your code
- [x] To avoid bugs in your program
- [x] To help yourself in 3 months understand your code
- [x] To help the compiler understand your code

2. What would happen when you execute a Python program where an integer is added to a string?

- The program would convert the integer to a string to not fail
- The program would convert the string to an integer to not fail
- The program would throw an error only when running your code [Answer] 
- The program would not compile because of the error

