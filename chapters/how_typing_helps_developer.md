# How Typing Helps Developers

![write code for the next developer](/images/memes/next_developer.jpg)

## Let Your Tools Help you

Now that we have discussed what static analysis is and type hinting syntax in Python, let's look at some real examples of where type hinting is helpful.

## Preventable Error: ID as Unknown Type

Type hinting can help when it's unclear what type a property is. This can frequently happen with a dictionary as Python struggles to infer the types of values in a dictionary.

For example, take the property `id`. When using an auto-incremented key in a database, id will usually be an integer, but when using a `uuid` or `guid` strategy, it is a string. This can cause errors even when using a simply print statement:

```py
# pretend this is returned from a database query
user = {
    "id": 5,
    "name": "John Doe",
}

id = user["id"]

print("received id: " + id)
# fails throwing 'TypeError: can only concatenate str (not "int") to str'
```

When running this locally with type hinting on, you will not see any indication that there is something wrong with the code. If you hover over `id` you will see that it has the type `Unknown`. 

![static analysis showing id unknown](/images/code_snippets/static_code_analysis_id_unknown.png)

No wonder the IDE didn't know this was going to fail! This is because Python is not able to interpret the type of value for a given property in a dictionary. 

How could we have caught this error?

## Creating Custom Types

To catch the previous runtime error before running the code, we can create our own type! 

Let's create a type `User` using `TypedDict` from the built-in `typing` package: 

```py
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
```

> Info: Classes as Interfaces in Python
> An Interface is a structure that defines the shape of a piece of data without the data needing to be defined. This is very common in statically typed languages, but because Python is not statically typed, it uses classes to define interfaces.
> The biggest advantage of using a class for a type is that you can check the type of a value at runtime.

Now we can use our custom type to tell the Python interpreter that `id` is an integer. Now we can use this type in our previous example to explicitly type the variable `user`:

```py
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str

user: User = {
    "id": 5,
    "name": "John Doe",
}

id = user["id"]

print("received id: " + id)
```

If you hover over the `id` variable now, you'll see that it's not `Unknown`, but an `int`! Our code just got a little safer 😎

![static analysis showing id as an integer](/images/code_snippets/static_code_analysis_id_int.png)

You'll also see the red squiggle under the print statement. If you hover over that you will see:

![static_code_analysis_red_squiggle_hover](/images/code_snippets/static_code_analysis_red_squiggle_hover.png)

We get a message that this print statement will not work *BEFORE* running our code. We just caught a bug without having to run our program!

## Error Message Analysis

The exact message we receive is:

`Operator "+" not supported for types "Literal['received id: ']" and "int" Pylance (reportOperatorIssue)`.

This is different from the runtime error we would get and arguably more useful.

The `Pylance` at the end of the message shows the static type checker where this message comes from. If you click on `reportOperatorIssue` you will get be taken to a website with the [exact rule](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOperatorIssue) that this error comes from.

> Good To Know: Context Switching Tax
> There are some parts of your code that may be clear to you *NOW* but in a few months, your memory may fade and you may mistake the type of a variable in your project with the type from another project.
> This forgetfulness when moving between projects is so common, it's referred to as a "Context Switching Tax". Type hints working with linting rules is a great way to help you and other developers remember how your code works.

1. How can you make sure another developer will know the type of a variable?
-  [x] Give the variable a clear name following clean code practices
-  [ ] It is not your responsibility for other developers to understand your code 
-  [x] Annotate the variable with a type hint
-  [ ] Give a variable the shortest name possible like 'a' or 'b'

2. What is code linting?
-  An automated process enabled by static code analysis that helps developers find bugs at compile time. (ANSWER)
-  A way to remove fuzz from a code base.
-  A tool for composing functions together by 'linting' them together

3. How is code linting useful for developers?
-  [x] It allows developers to see errors in their code before running
-  [x] It allows static analysis tools to visualize errors to a developer
-  [x] It ensures a basic level of code quality
-  [ ] It deletes ugly code in a code base