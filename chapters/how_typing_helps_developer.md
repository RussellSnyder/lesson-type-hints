# How Typing Helps Developers

![write code for the next developer](/images/memes/write_code_for_next_developer.jpg)

## Let Your IDE Help

Now that we have discussed what static analsis is and type hinting styntax in Python, let's look at some real examples of where type hinting is helpful.

> [WARNING] Examples must be done in your local IDE as type hinting is not currently supported in the code environment online.

## Preventable Error: ID as Unknown Type

Type hinting can help when it's unclear what type a property is in a dictionary. For example, take the property `id`. When using an auto-incremented key in a database, id will usually be an integer, but when using a `uuid` or `guid` strategy, it is a string. This can cause errors even when using a simply print statement:

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

When running this locally with type hinting on, you will not see any indication that there is something wrong with the code. If you however over `id` you will see that it has the type `Unknown`. 

![static analysis showing unknown](/images/code_snippets/static_code_analysis_unknown.png)

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

now we can use this type to tell the Python interpretter that id is an integer. Now we can use this type in our previous example to explicilty type the variable `user`:

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

If you run this program, we still get an error...BUT our interpretter now shows us we have an error before running the program. If you hover over the `id` variable now, you'll see that it's not `Unknown`, but is infact an `int`

![static analysis showing id as an integer](/images/code_snippets/static_code_analysis_id_int.png)

You'll also see the red squiggle under the print statement. If you hover over that you will see:

![static_code_analysis_red_squiggle_hover](/images/code_snippets/static_code_analysis_red_squiggle_hover.png)

We get a message that this print statement will not work *BEFORE* running our code. We just caught a bug without having to run our program!

## Error Message Analysis

The exact message we receive is:

`Operator "+" not supported for types "Literal['received id: ']" and "int" Pylance (reportOperatorIssue)`.

This is different from the runtime error we would get and arguably more useful.

The `Pylance` at the end of the message shows the static type checker where this message comes from. If you click on `reportOperatorIssue` you will get be taken to a website with theh [exact rule](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportOperatorIssue) that this error comes from.

## Linting Rules

The word `reportOperatorIssue` is commonly referred to as a "linting rule". Linting ruless enforce particular styles or code conventions on a code base. It's like an automated PR review in real time!

Linting rules are a very good way to ensure code base health. There are common sets of linting rules (like Pylance) but you caan also create your own linting rules to make sure you and your fellow developers write clean code. 

## Context Switching Tax

There are some parts of your code that may be clear to you *NOW* but in a few months, your memory may fade and you may mistake the type of a variable in your project with the type from another project leading to a bug in a new feature. This forgetfulness from moving between projects is often reffered to as a "Context Switching Tax" and is very common in the programming world. Type hints working with linting rules is a good way to help you and other developers remember how your code works.
