print("Welcome to the Tip Calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like yo give? 0, 10, 12 or 15? ")
split = input("How many people to split the bill? ")
tip_per = float(tip)/100
tip_n_split = float(bill) * tip_per
total = float(bill) + tip_n_split
split_total = total / float(split)
final = "{:.2f}".format(split_total)
print(f"Each person should pay ${final}")

