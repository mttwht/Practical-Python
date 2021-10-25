expenses = [7.50, 7, 6.50, 7.50, 10.00]
total = sum(expenses)

sum = 0

for x in expenses:
	sum = sum + x

print("You spent €", sum, sep="")