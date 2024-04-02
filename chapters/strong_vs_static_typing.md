# Strong vs. Static Typing

Although often confounded one for the other, strong and static typing are actually different. Python is strongly AND dynamically typed but it is NOT statically typed. We can visualize these types along to perpendicular axis:

```
                  [Compile time]
                     Static
                        ▲
                        |
                        |                   
  [Runtime] Weak<---------------->Strong 
                        |
                        |
                        ▼
                     Dynamic
```

Before we explain this chart, we must first understand the difference between compile time and run time.

## Compile vs. Runtime Time

Traditionally, compile time referred to the time when a language interpreter translates a high level programming language (like Python) into machine code (like bytecode for Python). However, with static analysis and linting constantly 'compiling' your code to check for errors or improvements, compile time now refers to the period of time before your code is actually running (eg, when you are writing the code but are not running that code).

When you run the command `python my_program.py`, you are telling the Python interpreter to compile your code and execute it. The environment your program is in when it is executing is called the "runtime" environment. 

## Runtime: Weak vs. Strong Typing

A weak (or loosely typed) language allows a program to change the type of a variable *while the program is running*. For example, if we initially set a variable to string number (eg. `foo = '5'`) and add that variable to an integer (eg. `print(foo + 5)`) a weakly typed language (like javascript) may *implicitly convert* either the string to a number or the number to a string so that the application continues to run. 

Strongly typed programming languages (like Python) tracks what type a variable and will throw useful error *at runtime* if errors are encountered.

> Example of weak typing
> In javascript, 4 + '2' equals '42'. Javascript implicitly converts the number 4 to a string in order to make the program continue to run.
> In Python, the interpreter throws an error because it is strongly typed. 

EXAMPLE
```py
print(4 + 2)
print(4 + '2')

```


## Compile Time: Static vs. Dynamic Typing

A statically typed language, once a type of a variable is declared *that type cannot change*. If the variable type does change *the code will not compile*! This failure of compilation is the biggest difference between static and dynamically typed languages. 

The opposite of statically typed is dynamically typed. Python is dynamically typed allowing compilation to always happen even if variables are entered of the wrong type.

> GOOD TO KNOW
> Proponents of dynamic programming say that static typing lowers productivity and does not add the security that it claims. Proponents of static typing say dynamic programming is dangerous and leads to more bugs. Which is best probably depends a lot on the situation, but there is clearly a trend towards static types in newer languages (e.g. Swift, Rust and Go). 

![graph of programming languages and type safety](/images/Programming_Language_Type_Safety.png)

> WARNING note on language 
> Some old school developers will call Python a 'weakly typed' language. This is probably there is more of a focus on compile time analysis than runtime safety for most languages. Most statically typed languages also have a strongly typed runtime (except Typescript because it compiles down to Javascript)

CHECK YOUR UNDERSTANDING

1. What is the opposite of a dynamic programming language?
- Weak
- Strong
- Static (Answer)
- Stiff

2. Can a language be strongly typed but not static?
- No, impossible
- Yes, that's Python! (Answer)

1. What type combination is most common in modern languages?
- Strong and Statically typed (Answer)
- Strong and Dynamically typed
- Weak and Statically typed
- Weak and Dynamically typed

1. Which of the following applies to Typescript? (Pick 2)
- [ ] Strongly typed 
- [x] Weakly typed
- [x] Statically typed
- [ ] Dynamically Typed  
