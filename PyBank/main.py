# Modules
import os
import csv     # for reading csv files

results = {}  # Create a dictionary

data = os.path.join("C:\\Users\\sanj1\\OneDrive\\BootCamp\\Week3_Python\\Homework\\budget_data.csv")

with open(data, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(csv_header)

    for row in csvreader:
        results[row[0]] = float(row[1])
    #line_count += 1
print("Financial Analysis")
print("------------------------------")

# The total number of months included in the dataset
y = len(list(results.values()))
print("Total Months: ", y)


# The net total amount of "Profit/Losses" over the entire period
print("Total: $", sum(results.values()))

# The average of the changes in "Profit/Losses" over the entire period
avg = sum(results.values()) / y
print("Average Change: $", avg)

# The greatest increase in profits (date and amount) over the entire period

maximum = max(results, key=results.get)
print("Greatest Increase in Profits:", maximum, "($",results[maximum],")")

# The greatest decrease in losses (date and amount) over the entire period

minimum = min(results, key=results.get)
print("Greatest Decrease in Profits:", minimum, "($",results[minimum],")")

# Output file
output_file = os.path.join("C:\\Users\\sanj1\\OneDrive\\BootCamp\\Week3_Python\\Homework\\Python-challenge\\PyBank\\budget_data.txt")

with open(output_file, "w") as text_file:
   text_file.write ("Financial Analysis\n")
   text_file.write ("-------------------------------\n")
   
   text_file.write ("Total Months: ")
   text_file.write (str(y))
   text_file.write ("\n")
   
   text_file.write ("Total: $")
   text_file.write (str(sum(results.values())))
   text_file.write ("\n")

   text_file.write ("Average Change: $")
   text_file.write (str(avg))
   text_file.write ("\n")

   text_file.write ("Greatest Increase in Profits: ")
   text_file.write (maximum)
   text_file.write (" $")
   text_file.write (str(results[maximum]))
   text_file.write ("\n")

   text_file.write ("Greatest Decrease in Profits: ")
   text_file.write (minimum)
   text_file.write (" $")
   text_file.write (str(results[minimum]))
   