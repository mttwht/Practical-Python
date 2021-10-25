money_owed = float(input("How large is your loan? (€)\n>"))
apr = float(input("What is the Annual Percentage Rate? (%)\n>"))
payment = float(input("What is your monthly payment amount? (€)\n>"))
months = int(input("How many months to show interest for?\n>"))

monthly_rate = apr / 100 / 12

for i in range(months):
	interest_paid = money_owed * monthly_rate
	money_owed += interest_paid

	if money_owed - payment < 0:
		print("The last payment is", money_owed)
		print("The load was paid off in ", i+1, "months.")
		break

	money_owed -= payment

	print("Paid", payment, "of which", interest_paid, "was interest.", end=" ")
	print(money_owed, "is still owed.")