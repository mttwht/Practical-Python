age = input("How old are you?\n> ")
age = int(age)
decades = age // 10
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")
