# Introduction to Typing

![dad joke about types dating](/images/memes/type_dating_meme.jpg)

## What is Typing?

Typing is a way to give either your compiler, interpreter or another developer more information about your code. Details such as:

- What type a variable or property is 
- What shape data will be
- What type of arguments a function takes and what type does it return

Typing can give similar information as code comments but in a way that machines (compiler/interpreter) can also understand. ****

## Type Safety

Type safety refers to the degree in which a programming language enforces what operations can be performed on what types of data.

## Inferred vs. Explicit Typing

Python uses inferred types to determine the type of a variable. This means that the program knows that when you write `foo = 5` that `foo` is an integer.

Languages that use explicit types (early Java) require you to write what type a variable is *before* setting the variable. 

With this said, there are times when neither python nor your IDE can infer a variables type correctly. This is where explicit typing (known in the Python world as "type hinting"), can really help.

## Static Code Analysis

Static code analysis refers to the ability to check code without running it. This is especially useful for large code bases where it would take a long time to run every branch of code but quality is still important. Explicit types help greatly with static code analysis as it enables the interpreter to know what types variables and functions return without executing the code.

> [Did You Know?] Static code analysis is sometimes viewed as the most important part of code testing. In the Kent Dodd's testing trophy strategy, all other types of tests rest on the foundation of static code analysis
![testing trophy from Kent C Dodds](/images/trophy_testing.webp)


Although static analysis cannot definitely assess whether a codebase is good or bad, it can suggest ways to improve and contribute metrics to assess a codebase's overall health.

Static code analysis can also help developers catch bugs early in the code creation process. Instead of waiting to run into errors when running code, static code analysis will show the developers where potential error or optimizations can occur *while* they are writing code. We'll see examples of this soon.

CHECK YOUR UNDERSTANDING

1. Which of the following are reasons to use a typing system

- [x] To help another developer understand your code
- [x] To avoid bugs in your program
- [x] To help yourself in 3 months understand your code
- [x] To help the compiler understand your code

2. Which of the following is an example of 'inferred typing' in Python?

- `foo = 5` the Python interpreter thinks foo is a string
- `foo = 5` the Python interpreter thinks foo is an integer [ANSWER]
- `bar = 2.0` the python interpreter thinks bar is a string

3. Why is static code analysis helpful?

- [x] It is a metric to assess the health of a codebase
- [x] It is a tool to help developers catch bugs without running a program
- [ ] It allows interpreted code to run in the cloud
- [ ] It ensures no malicious code is checked into a codebase
