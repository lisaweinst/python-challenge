# Import statements
import os
import csv

input_file = os.path.join("..", "Instructions", "budget_data.csv")

# making empty lists for profit changes, months and profit
profit_change = []
months = []
total_profit = []

 

with open(input_file,newline="") as money:

    #read file and then avoid header labels
    csvreader = csv.reader(money,delimiter=",") 

    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # get the months and profit to the correct lists
        months.append(row[0])
        total_profit.append(int(row[1]))

    #go through each profit
    for i in range(len(total_profit)-1):
        
        # obtain the different of each profit from each month
        profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
maxed_value = max(profit_change)
decrease_value = min(profit_change)

# get the min and max increase of each month
#use plus 1 to get each month
increase_month = profit_change.index(max(profit_change)) + 1
decrease_month = profit_change.index(min(profit_change)) + 1 

#Final Summary text file for the analysis text file


print("Financial Analysis")
print("-" * 20)
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[increase_month]} (${(str(maxed_value))})")
print(f"Greatest Decrease in Profits: {months[decrease_month]} (${(str(decrease_value))})")

# Output files
#. means in the same directory
output_file = "./Financial_Analysis_Summary.txt"

with open(output_file,"w") as file:
    
# Writing the data to Financial_Analysis_Summary 
    file.write("Financial Analysis\n")
    file.write("-" * 20) 
    file.write("\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {months[increase_month]} (${(str(maxed_value))})\n")
    file.write(f"Greatest Decrease in Profits: {months[decrease_month]} (${(str(decrease_value))})")