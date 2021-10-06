# import dependencies
import csv
import os

# read the csv file
CSV_FILE_PATH = os.path.join("Resources", "budget_data.csv")

#output file location for the survey analysis
outputFile = os.path.join("budget_Analysis.txt")

#variables 
totalDates = 0 #variable that holds the total number of dates
totalPL = 0 #variable that holds the net profit/losses
averageChanges = [] #variable that holds the changes
months = [] #variable that holds the months

# read the csv file
with open(CSV_FILE_PATH) as surveyData:
    #establish csv reader
    csvreader = csv.reader(surveyData)

    #read the header
    header = next(csvreader)
    #move to the first row
    firstRow = next(csvreader)

    # add on to the total dates
    totalDates += 1 # same as totalDates = totalDates + 1

    #add the profit/losses
    totalPL += float(firstRow[1]) # index 1 is the Profit/Losses
 
    # establish what the previous amount
    #profit/losses are in index 1
    previousAmount = float(firstRow[1])

    
    # for each row
    for row in csvreader:
        # add on to the total dates
        totalDates += 1 # same as totalDates = totalDates + 1

        #add the profit/losses
        totalPL += float(row[1]) # index 1 is the Profit/Losses

        #calculate the net change
        netChange = float(row[1]) - previousAmount
        
        #add on to the list of average changes
        averageChanges.append(netChange)

        #add the first month that a change occurred
            #month is in index 0
        months.append(row[0])
        #update the previousAmount
        previousAmount = float(row[1])

    #calculate the average net change per month
    averageChangePerMonth = sum(averageChanges) / len(averageChanges)
    
    greatestincrease = [months[0],averageChanges[0]] #holds the month and the value for the greatest increase
    greatestdecrease = [months[0],averageChanges[0]] #holds the month and the value for the greatest decrease

#use the loop to calculate the index of the greatest and least average changes
for a in range(len(averageChanges)):
    #calculate the greatest increase and decrease
    if (averageChanges[a] > greatestincrease[1]):
        # if the value is greater that the greatest increase, then that valuse becomes the greatest increase
        greatestincrease[1] = averageChanges[a]
        #update the month
        greatestincrease[0] = months[a]

    if (averageChanges[a] < greatestdecrease[1]):
        # if the value is greater that the greatest decrease, then that valuse becomes the greatest decrease
        greatestdecrease[1] = averageChanges[a]
        #update the month
        greatestdecrease[0] = months[a]

output = (
    f"\n\nFinancial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {totalDates:,}\n"
    f"Total: ${totalPL:.0f}\n"
    f"Average Change: ${averageChangePerMonth:.2f}\n"
    f"Greatest Increase in Profits: {greatestincrease[0]} Amount ${greatestincrease[1]:.0f}\n"
    f"Greatest Decrease in Profits: {greatestdecrease[0]} Amount ${greatestdecrease[1]:.0f}"
)

#display output to the terminal
print(output)

#print results to text file
with open(outputFile, "w") as textFile:
    #write output to text file
    textFile.write(output)


