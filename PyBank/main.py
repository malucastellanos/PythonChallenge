import os
import csv

budgetCSV = os.path.join('budget_data.csv')

print("Financial Analysis")
print("------------------")


monthlycount = 0
totalprofit = 0
profits = []
changes = []
dates = []

with open(budgetCSV, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
  		monthlycount = monthlycount + 1
  		profit = int(row[1])
  		totalprofit = totalprofit + profit
  		profits.append(float(row[1]))
  		dates.append(str(row[0]))
  	
	for i in range(1, len(profits)):
		changes.append(int(profits[i]) - int(profits[i-1]))

def average(changes):
	totalchange = 0
	lenght = len(changes)
	for change in changes:
		totalchange = totalchange + change
		averagechange = totalchange / lenght
	return float(averagechange)

MaxChange = max(changes)
MinChange = min(changes)

for i in range(len(changes)):
	if changes[i] == MaxChange:
		MaxDate = dates[i]
	if changes[i] == MinChange:
		MinDate = dates[i]

print(f"Total Months: " + str(monthlycount))
print(f"Total: $" + str(totalprofit))
print(f"Average Change: $" + str("{0:.2f}".format(average(changes))))
print(f"Greatest Increase in Profits: " + str(MaxDate) + " $ (" + str(MaxChange) + ")")
print(f"Greatest Increase in Profits: " + str(MinDate) + " $ (" + str(MinChange) + ")")


PyBankTXT = open('PyBankTXT', 'w')
PyBankTXT.write('Financial Analysis \n')
PyBankTXT.write('------------------ \n')
PyBankTXT.write('Total Months: ' + str(monthlycount) + "\n")
PyBankTXT.write('Total: $' + str(totalprofit) + '\n')
PyBankTXT.write("Average Change: $" + str("{0:.2f}".format(average(changes))) + '\n')
PyBankTXT.write("Greatest Increase in Profits: " + str(MaxDate) + " $ (" + str(MaxChange) + ") \n")
PyBankTXT.write("Greatest Increase in Profits: " + str(MinDate) + " $ (" + str(MinChange) + ") \n")
