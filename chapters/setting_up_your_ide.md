# Setting up Your IDE for Type Hinting

Type hinting allows a developer to catch potential bugs without having to run the program. However, if your IDE is not setup for type checking, you may not see a red squiggly or receive messages when there are type mismatches.

If you already see type mismatch errors, you cna skip this section. Otherwise, here is a list of Instructions depending on your IDE.

### VS Code

In your settings.json file (`ctr+shift+p` and type `settings` to find the command `Preferences: Open User Settings (JSON)). Once open, add a new line with the following setting:

```json
{
    "python.analysis.typeCheckingMode": "basic"
}
```

There are two settings, `basic` and `strict`. 