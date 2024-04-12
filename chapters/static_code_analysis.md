# Static Code Analysis

![Compile time bugs are better to find](/images/memes/bugs_at_compile_time.jpg)

Before we get into what static code analysis, we need to a little vocabulary.

## Compile vs. Runtime Time

Traditionally, compile time referred to the time when a language interpreter translates a high level programming language (like Python) into machine code (like bytecode for Python). However, with static analysis constantly 'compiling' your code to check for errors or improvements, compile time now refers to the period of time before your code is actually running (eg, when you are writing the code but are not running that code).

When you run the command `python my_program.py`, you are telling the Python interpreter to compile your code and execute it. The environment your program is in when it is executing is called the "runtime" environment. 

## Static Code Analysis

Static code analysis refers to the ability to check code without running it (at compile time). This is especially useful for large code bases where it would take a long time to run every branch of code but quality is still important. Explicit types help greatly with static code analysis as it enables the interpreter to know what types variables and functions return without executing the code.

> [Did You Know?] Static code analysis is sometimes viewed as the most important part of code testing. In the Kent Dodd's testing trophy strategy, all other types of tests rest on the foundation of static code analysis.
![testing trophy from Kent C Dodds](/images/trophy_testing.webp)

## Compile Time Bugs Are Easier to Squash Than Runtime Bugs

Static code analysis can also help developers catch bugs early in the code creation process. Instead of waiting to run into errors when running code (runtime), static code analysis will show the developers where potential error or optimizations can occur *while* they are writing code (compile time).

Just like with real insect infestations, bugs in computer software are better to get rid of early. Some reasons for this are:

- Code reuse can multiply bugs throughout a code base
- Bugs in a running system cause more damage (loss of sales, security holes) and create more time pressure to fix

> Linting: Applying Static Code Analysis
> Linting refers to the process of funding (and potentially automatically removing) bugs from your code using static code analysis. Using a set of 'lint rules', a static code analyzer scans code to see if any places violate these rules. This is where the red squiggle under error prone code comes from! 

## Taking it to the Extreme: Static Type Checking

By adding type hinting to your Python code, you are open the possibility to enforce static type checking in your Python code. This means that your code will not compile if there are any type errors!

Python made the decision to not enforce static typing in its core language for a variety of reasons. But it did implement the ability for 3rd parties to enable this static type checking.

At first glance, this sounds annoying (and it can be), but when working on a large code base with hundreds of developers, static type checking will blocks developers from committing code that have known errors in it. You can think of it like automating code reviews!

1. What is the difference between runtime and compile time?

- Compile time happens before the code is executed (Answer)
- There is no difference
- It's better to find bugs at runtime
- Type hinting applies types at runtime

2. Why is static code analysis helpful?

- [x] It is a metric to assess the health of a codebase
- [x] It is a tool to help developers catch bugs earlier in the development process
- [ ] It allows interpreted code to run in the cloud
- [ ] It ensures no malicious code is checked into a codebase

3. Why is it better to catch bugs at compile time?

- [x] There is less pressure to fix the bugs
- [ ] You can 'compile' them away
- [x] Bugs have less time to multiply
- [x] Static code analysis can automatically find bugs and this can only happen at compile time  

