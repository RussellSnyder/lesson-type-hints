## Self Documenting Code

![Comments vs Typehinting](/images/memes/comments_vs_type_hinting_meme.jpg)

There is an expression that some programmers use to justify not documenting their code with either code comments or standalone documentation. They claim their code is "self documenting".

While it's still highly debated if code can ever be fully self documenting, using type hints certainly increases the ability of a developer to reason about how a piece of code will work *without running it*.

Take this example of code without typehints:

```py
import random

def revert_operation():
    success = random.randint(0, 1) == 1
    if (success):
        return 'Operation successful.'
    else:
        return 'Operation failed.'

```
In this function, there is a 50% chance that either the message "Operation successful. But Oh No! I wanted this function to return a boolean and only print the string. With this expectation, later on I might write the following code:

```py
is_success = revert_operation()
if (is_success):
    print("continue with program")
```

This boolean `is_success` will always be `True`! Now there is a hard bug to find later on.

However, if I started my function with the annotation of what return was expected, I would not have made this mistake:

```py
import random

def revert_operation() -> bool:
    success = random.randint(0, 1) == 1
    if (success):
        return 'Operation successful.'
    else:
        return 'Operation failed.'
```
Now if we look at this code in an IDE, we see the angelic red squiggles that will help us catch a bug before production:

![red squiggles in a function when the return type does not match](/images/code_snippets/type_hint_function_return.png)

This is a small contrived example, but imagine you start a function just before leaving work and pick it up again the next day. Would you be sure that you remember what type you wanted to return from that function? There is a reason that the return type for a function is declared towards the beginning of the function and not at the end: it helps document the expected return type *before* you finish writing the function!

CHECK YOUR KNOWLEDGE

1. Look at the beginning of this function. What is the expected return type?
```py
def is_awesome_code() -> bool:
```
- Boolean (Answer)
- Integer
- No return
- Float

2. How would you indicate that a function does not return anything?
- Use the `None` type as the return (Answer)
- Don't write anything
- Use the `Nil` type as the return
- Functions always return something so this is not needed

3. How can you create code that is "self documenting"
- [x] Use type hints for function returns
- [x] Use clear names for variables that follow clean code practices
- [ ] Write lots of documentation that lives in a Wiki somewhere