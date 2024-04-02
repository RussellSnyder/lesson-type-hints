import random

def revert_operation() -> bool:
    success = random.randint(0, 1) == 1
    if (success):
        return 'Operation successful.'
    else:
        return 'Operation failed.'
    
print(revert_operation())

is_success = revert_operation()
if (is_success):
    print("continue with program")