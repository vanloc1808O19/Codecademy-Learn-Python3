from asyncore import read, write


def my_function(x):
    return x + 1

print(my_function(2))
print(my_function(3 * 5))

def write_a_book(character, setting, special_skill):
    print(character + " is in " + setting + " practicing his/her " + special_skill)

write_a_book("Harry", "Hogwarts", "Potions")

def ready_for_school(backpack, pencil_case):
    if (backpack == "full" and pencil_case == "full"):
        print("Ready for school!")
    else:
        print("Not ready for school!")

ready_for_school("full", "full")
ready_for_school("full", "empty")

def find_volume(length = 1, width = 1, depth = 1):
    print("Length = " + str(length))
    print("Width = " + str(width))
    print("Depth = " + str(depth))

    return length * width * depth

find_volume()
find_volume(2, 3, 4)
find_volume(length = 5, depth = 2, width = 4)

def square_point(x, y, z):
    x_square = x * x
    y_square = y * y
    z_square = z * z

    # return all three values
    return x_square, y_square, z_square

three, four, five = square_point(3, 4, 5)
print(three)
print(four)
print(five)