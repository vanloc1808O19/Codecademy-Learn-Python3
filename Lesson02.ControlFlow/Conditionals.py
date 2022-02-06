# if statement

test_var = 100

if test_var > 1:
    # expressions evaluates to True
    print("This code is executed")

if test_var > 1000:
    # expression evaluates to False
    print("This code is not executed")

print("Program continues at this point.")

# else statement

test_value = 50
if test_value < 1:
    print("Value is < 1")
else:
    print("Value is >= 1")

test_string = "VALID"

if test_string == "NOT_VALID":
    print("String is NOT valid")
else:
    print("String is valid")

# elif statement

pet_type = "fish"

if pet_type == "dog":
    print("You have a dog")
elif pet_type == "cat":
    print("You have a cat")
elif pet_type == "fish":
    # this is executed
    print("You have a fish")
else:
    print("Not sure!") 