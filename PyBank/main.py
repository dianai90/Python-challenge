import csv
import os

#set path
csvpath= os.path.join('PyBank/Resources/budget_data.csv')
#path to collect data
output_path = os.path.join('PyBank/Analysis/Financial_Analysis.txt')

#PyBank Variables
total_months = 0
previous_revenue = 0
month_of_change = []
revenue_change_L = []
greatest_increase = ["",0]
greatest_decrease = ["", 99999999999]
total_revenue = 0

# open and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_months = total_months + 1
        print(row)
        total_revenue = total_revenue + int(row[1])

        revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change_L = revenue_change_L + [revenue_change]
        month_of_change.append(row[0])

    #Increase 
    if (revenue_change > greatest_increase[1]):
        greatest_increase[0] = row[0]
        greatest_increase[1] = revenue_change

   #Decrease
    if (revenue_change < greatest_decrease[1]):
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = revenue_change

    revenue_average = sum(revenue_change_L) / len(revenue_change_L)

#output summary
    output = (
        f"\nFinancial Analysis\n"
        f"-------------------------\n"
        f"Total_Months: {total_months}\n"
        f"Total_Revenue: ${total_revenue}\n"
        f"Average_Revenue Change: ${revenue_average}\n"
        f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

#print the output

print(output)

with open(output_path, "w") as txt_file:
    txt_file.write(output)

          
           
        
    
   