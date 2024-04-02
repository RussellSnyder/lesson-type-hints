# How Typing Helps Developers

![write code for the next developer](/images/memes/write_code_for_next_developer.jpg)

## Let Your Tools Help you

Now that we have discussed what static analysis is and type hinting syntax in Python, let's look at some real examples of where type hinting is helpful.

> [WARNING] Examples must be done in your local IDE as type hinting is not currently supported in the code environment online.

## Preventable Error: ID as Unknown Type

Type hinting can help when it's unclear what type a property is. This can frequently happen with a dictionary. 

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

## Error Detected: ID as Integer

To catch the previous runtime error before running the code, we could have used type hinting! 

Let's create aa class type `User` using `TypedDict` from the built-in `typing` package: 

```py
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
```

Now we can use this type to tell the Python interpreter that `id` is an integer. Now we can use this type in our previous example to explicitly type the variable `user`:

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

If you hover over the `id` variable now, you'll see that it's not `Unknown`, but an `int`!

![static analysis showing id as an integer](/images/code_snippets/static_code_analysis_id_int.png)

You'll also see the red squiggle under the print statement. If you hover over that you will see:

![static_code_analysis_red_squiggle_hover](/images/code_snippets/static_code_analysis_red_squiggle_hover.png)

We get a message that this print statement will not work *BEFORE* running our code. We just caught a bug without having to run our program!

> WARNING/NOTE
> If you run this program, upi will still get an error...BUT our interpreter now "hints" to us that we have an error before running the program. In other static languages or in Python with a 3rd party static code package, this code would refuse to compile all together.  

## Error Message Analysis

The exact message we receive is:

`Operator "+" not supported for types "Literal['received id: ']" and "int" Pylance (reportOperatorIssue)`.

This is different from the runtime error we would get and arguably more useful.

The `Pylance` at the end of the message shows the static type checker where this message comes from. If you click on `reportOperatorIssue` you will get be taken to a website with the [exact rule](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOperatorIssue) that this error comes from.

## Linting Rules

The word `reportOperatorIssue` is commonly referred to as a "linting rule". Linting rules enforce particular styles or code conventions on a code base. It's like an automated PR review in real time!

Linting rules are a very good way to ensure code base health. There are common sets of linting rules (like Pylance) but you can also create your own linting rules to make sure you and your fellow developers write clean code. 

Code linting is only be possible because of the static analysis happening on a code base. You can think of it like a GUI through which static analysis shows errors to a developer. Without code linting, errors caught by static analysis tools would be invisible!

## Context Switching Tax

There are some parts of your code that may be clear to you *NOW* but in a few months, your memory may fade and you may mistake the type of a variable in your project with the type from another project leading to a bug in a new feature. This forgetfulness from moving between projects is often referred to as a "Context Switching Tax" and is very common in the programming world. Type hints working with linting rules is a good way to help you and other developers remember how your code works.

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