# for <temporary variable> in <sequence>:
#     <statements>
#     <statements>

# each num in nums will be printed below
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

for i in range(0, 10, 2):
    print(i)

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for num in big_number_list:
    if num < 0:
        continue
    print(num)

numbers = [0, 254, 2, -1, 3]
for num in numbers:
    if (num < 0):
        print('Negative number detected!')
        break
    print(num)