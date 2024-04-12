## Inferred vs. Explicit Typing

Sometimes Python can guess what type each variable is, but this will not always work. This 'type guessing' is called 'inferred'. For example, Python knows that when you write `foo = 5` that `foo` is an integer.

In languages that require explicit types (like early Java or C++) the type is written *before* setting the variable. In Java, this looks like this:

```java
int foo = 5
```

With type hinting in Python, the type is written just after the variable like this:

```py
foo: int = 5
```

Type hinting is how we can make types 'explicit' in Python programs.

## Python Variable Types can Change at Runtime

Python is a 'dynamic language' which means a variable can be changed to a different type at runtime. Python has no problem running this:

```py
foo = 5
foo = 'hello world'
```

A 'static language' like Java cannot do this and requires that a variable remains its original type for the entirety of the application execution. 

CHECK YOUR UNDERSTANDING

1. Which of the following is an example of 'inferred typing' in Python?

- `foo = 5` the Python interpreter thinks foo is a string
- `foo = 5` the Python interpreter thinks foo is an integer [ANSWER]
- `bar = 2.0` the python interpreter thinks bar is a string

3. Look at the following function:

```py
def add(thing1, thing2):
    return thing1 + thing2
```

developers keep getting errors when adding a string to a number. This function should only be used with numbers. How could we improve this function *using type hints*?

- [x] Use type hints for the function arguments
- [ ] Use a different operator than '+'
- [x] Add a return type to the function to help users understand the output better
- [ ] rename variables to better convey meaning