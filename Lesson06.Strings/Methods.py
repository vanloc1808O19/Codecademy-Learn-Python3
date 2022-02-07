# format
msg1 = "Fred scored {} out of {} points."
print(msg1.format(3, 10))
msg2 = "Fred {verb} a {adj} {noun}."
print(msg2.format(adj = 'fluffy', verb = 'tickled', noun = 'cat'))

# lower
greeting = "Welcome to Chill's"
print(greeting.lower())

# upper
print(greeting.upper())

# strip
text1 = '             apples and oranges    '
text1 = text1.strip()
print(text1)
text2 = '...+...lemons and limes...-...'
text3 = text2.strip('.')
print(text3)
text4 = text2.strip('.+')
print(text4)
text5 = text2.strip('.+-')
print(text5)

# title
my_var = 'dark knight'
print(my_var.title())

# split
text = "Silicon Valley"
print(text.split())
print(text.split('i'))

# find
mountain_name = "Mount Kilimanjaro"
print(mountain_name.find('o'))

# replace
fruit = "Strawberry"
print(fruit.replace('r', 'R'))

# join
x = "-".join(["Loc", "is", "handsome"])
print(x)