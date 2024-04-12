# Unions and Optional

Sometimes a single type isn't enough for a variable or you want to make sure the consumer of a function handles the case when None is returned. Type hinting has your back.

## Union - When Multiple Types Are Returned

![Why pick just one type!?](/images/memes/string_int_union.jpg)

Union types allow you to use multiple types for the same variable. This is useful when a function may return different types depending on a condition. 

For example, let's say you want to get the total for a purchase (a float) but only the sale is complete (some condition). Let's look at an example:

```py
def get_total(checkout_complete: bool):
    if not checkout_complete:
        return "Checkout is not yet complete"
    return 100.75
```

What is the return type for this function? It looks like it could be a `float` OR a `str` depending on whether `checkout_complete` is true of false. And again, we have to look into the body to determine what types might be return which wastes out precious time and brain power.

If we annotate this function with a union return type, we can reason about returns without having to look into the function

```py
def get_total(checkout_complete: bool) -> float | str:
    #...logic here
```

Later in our application, if we try to print the result of this function, we will get an error if it is a float.

![This could be a float so there is a warning](/images/code_snippets/could_be_float.png)

But if we check the type, we can handle the return value accordingly. In this case, casting the total to a string.

![casting the float so that we don't get errors](/images/code_snippets/is_float.png)

> Note - For The Future
> Usually we would use a class (like `Exception`) for error messages like in the previous example. Class based error messages allows use to separate those messages from normal strings
> Also, `raise` would usually be called to allow the error to bubble up to a centralized error handling system.

## Exercise

Add return types to the following functions:

```py
def calculate_area(side_length: int | None):
    if side_length is None:
        return "You did not enter a side length!"
    return side_length * side_length

def divide_7_by_number(number: int | None):
    if number == None:
        print("You did not enter a number!")
        return None
    if number == 0:
        print("Cannot divide by 0")
        return None
    return 7 / number
```

## Optional - When None or a Type Are Returned 

![Why pick just one type!?](/images/memes/marked_safe_optional.jpg)

Because returning `type | None` is so common, there is a special type of to declare this called an "Optional". When you wrap a type with an Optional, you are simply telling the interpreter that a variable will either be that type OR `None`. 

For example, we may not always know if a variable has been set to a value yet. Or we may not have enough information to always return a value from a function:

```py
from typing import Optional

def is_ready_to_party(age: Optional[int]) -> Optional[bool]:
    if age == None or age < 0:
        print("Age is invalid")
        return None
    return age >= 18
```

By wrapping this types in `Optional`, we are telling the interpreter "Hey, we need to handle situations where this will be None". This will help find 

> Info "Null: The Billion Dollar Mistake"
> One of the most common errors in programming is called the 'null pointer' error. This is when a program uses a variable assuming that it is assigned a value when in fact, it is assigned to null (`None` in Python). Null as we know it in computer science was invented in 1965 by Tony Hoare. 
> Because of the countless bugs null pointer errors have caused in programs leading to lost developer time and company revenue, Hoare refers to null as his "Billion Dollar Mistake". Technically, null never needed to exist and Hoare himself said he added it "...simply because it was so easy to implement."
> How can we avoid null pointer errors? Modern languages (like Rust and Haskell) solve the null pointer error by strictly enforcing the handling of variables that may be null (`Option` in Rust and `Maybe` in Haskell). Python's solution is to mark variables as `Optional` to ensure that consumers of that variable handle cases when that variable is `None`. So use 

## Exercise

Look at the exercise above. Replace union types with `None` with optionals.