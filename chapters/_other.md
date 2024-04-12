There is certainly a trend of modern languages moving towards strongly typed systems. The rising popularity of Typescript and [proposals to add type annotations](https://github.com/tc39/proposal-type-annotations) into an upcoming version of javascript suggests that it's just a matter of time before typing systems will be everywhere.



## Make Your Own Type Upgrades If You Want

Just as Python makes the decision to upgrade certain types, you can overload the  

```py
class AlwaysFloat(object):
    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other_value):
        return self.value + other_value

print(AlwaysFloat(2) + 3)
# will always print a float even through only integers were input
```

EXCERISE
Create a class that only returns integers when divided by another integer. Round the number down is a float is received.


## VS Code

In your settings.json file (`ctr+shift+p` and type `settings` to find the command `Preferences: Open User Settings (JSON)). Once open, add a new line with the following setting:

```json
{
    "python.analysis.typeCheckingMode": "basic"
}
```

Now you a red squiggle will appear under code that violates typing.

TODO: Instructions for other IDEs


## Why Doesn't Everybody use Typing?

the main opponents of typing say that there is a loss in productivity when using types. Instead of focusing on the run time product, too much time is spent doing 'type gymnastics'.

While this may be true in some situations, there are some situations where types are especially helpful:

- Building a library to be imported into other projects
- On large, open-source code bases to enable automated checks
- When code quality is very important (e.g. medical devices)