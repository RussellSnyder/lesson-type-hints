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



