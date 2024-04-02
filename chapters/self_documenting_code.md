## Self Documenting Code

![Comments vs Typehinting](/images/memes/comments_vs_type_hinting_meme.jpg)

There is an expression that some programmers use to justify not documenting their code with either code comments or standalone documentation. They claim their code is "self documenting".

While it's still highly debated if code can ever be fully self documenting, using type hints certainly increases the ability of a developer to reason about how a piece of code will work *without running it*.

Take this example of code without typehints:

EXAMPLE OF CODE THAT IS AMBIGOUS

QUIZ What could be the type of FOO

QUIZ what could be the type of BAR

As you can see, these variables could be a few different types. You would have to check at runtime with the the `isinstance` or `type` method. However, if you add type hints, you would be able to know what these types are without running the code

EXAMPLE OF CODE THAT IS TYPED

QUIZ What type is FOO
QUIZ What type if BAR

As you can see, adding type hints removes ambigiuty from our program. This not only helps us in the future looking back at code we wrote last year, it helps other developers understand how our code works.