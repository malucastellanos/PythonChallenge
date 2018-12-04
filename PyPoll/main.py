import os
import csv
import random

electionCSV = os.path.join('election_data.csv')

print("Election Results")
print("----------------")

votecount = 0
votesKhan = 0
votesCorrey = 0
votesLi = 0
votesOTooley = 0
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

with open(electionCSV, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
  		votecount = votecount + 1

  		if row[2] == candidates[0]:
  			votesKhan = votesKhan + 1
  		if row[2] == candidates[1]:
  			votesCorrey = votesCorrey + 1
  		if row[2] == candidates[2]:
  			votesLi = votesLi + 1
  		if row[2] == candidates[3]:
  			votesOTooley = votesOTooley+1


percentageKhan = votesKhan / votecount
percentageCorrey = votesCorrey / votecount
percentageLi = votesLi / votecount
percentageOTooley = votesOTooley / votecount
finalresults = {"Khan": votesKhan, "Correy": votesCorrey, "Li": votesLi, "O'Tooley": votesOTooley}
maxvotes = max(finalresults.values())
winner = [key for key, value in finalresults.items() if value == maxvotes][0]

print(f"Total Votes: " + str(votecount))
print("-------------------------------")
print(f"Khan: " + str("{0:.3%}".format(percentageKhan)) + " (" + str(votesKhan) + ")")
print(f"Correy: " + str("{0:.3%}".format(percentageCorrey)) + " (" + str(votesCorrey) + ")")
print(f"Li: " + str("{0:.3%}".format(percentageLi)) + " (" + str(votesLi) + ")")
print(f"O'Tooley: " + str("{0:.3%}".format(percentageOTooley)) + " (" + str(votesOTooley) + ")")
print("-------------------------------")
print(f"Winner: " + str(winner))

PyPollTXT = open('PyPollTXT', 'w')
PyPollTXT.write('Election Results \n')
PyPollTXT.write('------------------ \n')
PyPollTXT.write("Khan: " + str("{0:.3%}".format(percentageKhan)) + " (" + str(votesKhan) + ") \n")
PyPollTXT.write("Correy: " + str("{0:.3%}".format(percentageCorrey)) + " (" + str(votesCorrey) + ") \n")
PyPollTXT.write("Li: " + str("{0:.3%}".format(percentageLi)) + " (" + str(votesLi) + ") \n")
PyPollTXT.write("O'Tooley: " + str("{0:.3%}".format(percentageOTooley)) + " (" + str(votesOTooley) + ") \n")
PyPollTXT.write("------------------------------- \n")
PyPollTXT.write("Winner: " + str(winner) + "\n")








