# # 1
# name = input('What is your name? ')
# print('Hello, ' + name + '!' + '\n')

# # 2
# name = input('WHAT IS YOUR NAME? ')
# output = 'HELLO, ' + name.upper()+ '!\nYOUR NAME HAS ' + str(len(name)) + ' LETTERS IN IT! AWESOME!\n'
# print(output.upper())

# # 3
# print('Please fill in the blanks below:')
# print('''____(name)____'s favorite subject in school is ____(subject)____.''')
# user_name = input('What is name? ')
# subject = input('What is subject? ')
# print(user_name.capitalize() + "'s favorite subject in school is " + subject)

# # 4
# day = int(input('Day(0-6)? '))
# days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# print(days_of_the_week[day])

# # 5
# day = int(input('Day(0-6)? '))
# days_of_the_week = ['Sleep in', 'Go to work', 'Go to work', 'Go to work', 'Go to work', 'Go to work', 'Sleep in']
# print(days_of_the_week[day])

# # 6
# user_temperature_in_celcius = input('Input a temperature in Celcius\n')
# converted_temperature_in_fahrenheit = float(user_temperature_in_celcius) * 9 / 5 + 32
# print(str(int(converted_temperature_in_fahrenheit)) + ' F')

# # 7
# i = 1
# while i <= 10:
#   print(i)
#   i += 1

# # 8
# start = int(input('Start on: '))
# end = int(input('End on: '))
# while end >= start:
#   print(start)
#   start += 1

# # 9
# height = width = 5
# x = y = 0
# row = ""
# symbol = "*"
# spacer = " "
# while x < width:
#   row += symbol + spacer
#   x += 1
# while y < height:
#   print(row)
#   y += 1

# # 10
# height = width = int(input('How big is the square? '))
# x = y = 0
# row = ""
# symbol = "*"
# spacer = " "
# while x < width:
#   row += symbol + spacer
#   x += 1
# while y < height:
#   print(row)
#   y += 1

# 10b
# ask user for input
height = int(input('height: ')) 
width = int(input('width: '))
symbol = str(input('symbol: '))
spacer = str(input('spacer: '))

# row of symbols
row = ''

# build first row of symbols with a trailing spacer
while width > 1:
  row += symbol + spacer
  width -= 1

# add a symbol without a spacer to finish the row
row += symbol

# print a new row subtracting one from y until 0
while height > 0:
  print(row)
  height -= 1