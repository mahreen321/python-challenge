import os
import csv

# setting up variables and list
total_month = 0
total_net = 0
previous_change = 0
netchange = []

# file path
budgetData = os.path.join("Resources/budget_data.csv")

# reading file and first row values
with open (budgetData) as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=",")


    header = next(csvreader)

    janData = next(csvreader)


    totalMos = total_month + 1
    totalNet = total_net + int(janData[1])
    prevChange = int(janData[1])
    months = []

# counting no. of months and total net profit/loss

    for row in csvreader:
       
        months.append(row[0])
        totalMos = totalMos + 1
        totalNet = totalNet + int(row[1])
      
        netChange =  (int(row[1]) - prevChange)

        prevChange = int(row[1])
        netchange.append(netChange)

# calculating net average 
    netAvgChange = round(sum(netchange) / len(netchange),2)

    maxValue = max(netchange)
    greatMonth = netchange.index(maxValue)

    minValue = min(netchange)
    minMonth = netchange.index(minValue)

# printing to terminal
    print ("Financial Analysis")
    print ("----------------------------")
    finAnalysis = [
        "Total Months: " + str(totalMos),
        "Total: $" + str(totalNet),
        "Average Change: $" + str(netAvgChange),
        "Greatest Increase in Profits: " + str(months[greatMonth]) + " " + "($" + str(maxValue) + ")",
        "Greatest Decrease in Profits: " + str(months[minMonth]) + " " + "($" + str(minValue) + ")"
        ]
for results in finAnalysis:
    print(results)


# writing to file

header = 'Financial Analysis'
dash = '----------------------------'

with open('analysis/budget_analysis.txt', 'w') as f:
    f.write(header + '\n')
    f.write(dash+ '\n')
    f.write("Total Months: " + str(totalMos)+ '\n')
    f.write("Total: $" + str(totalNet)+ '\n')
    f.write("Average Change: $" + str(netAvgChange)+ '\n')
    f.write("Greatest Increase in Profits: " + str(months[greatMonth]) + " " + "($" + str(maxValue) + ")"+ '\n')
    f.write("Greatest Decrease in Profits: " + str(months[minMonth]) + " " + "($" + str(minValue) + ")"+ '\n')
