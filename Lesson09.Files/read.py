with open('mystery.txt') as text_file:
    text_data = text_file.read()
print(text_data)

with open('lines.txt') as file_object:
    file_data = file_object.readlines()
print(file_data)
for line in file_data:
    print(line)