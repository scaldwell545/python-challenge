import os
import csv

##Create list of each entry type for easier analysis
list_of_months = []
monthly_profitloss = []

##Create list of differences for min/max evaluation
list_of_differences = []

##Create Boolean to skip first entry for differences of profit/loss
first_row = True

input_file = os.path.join(os.getcwd(), 'Resources', 'budget_data.csv')
with open(input_file, newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    ##Create counter variable for net total and initialize previous value for min/max
    net_total = 0
    previous_value = 0
    
    next(csv_reader) ##Skip the first row (headers)
    for row in csv_reader:
        
        ##Pull month of row into list
        list_of_months.append(row[0])

        ##Pull profit/loss into list and add to the net total
        monthly_profitloss.append(row[1])
        net_total = net_total + int(row[1])

        ##calculate differences b/w entries of profit/loss + add to list
        if first_row == True:
            previous_value = int(row[1])
            first_row = False
        else:
            difference_of_monthly_profitloss = int(row[1]) - previous_value
            list_of_differences.append(difference_of_monthly_profitloss)
            previous_value = int(row[1])
            
    ##Calculate total # of months
    total_months = len(list_of_months)
    
    ##Calculate the Average Change of Profit/Loss Column ((last entry - first entry)/number of months in data set -1)
    average_change = (int(monthly_profitloss[total_months-1]) - int(monthly_profitloss[0])) / (total_months-1)

    ##Find the greatest increase in monthly profits and its corresponding month
    max_monthly_profit_difference = max(list_of_differences)
    max_index = list_of_differences.index(max_monthly_profit_difference)
    max_month = list_of_months[max_index+1]

    ##Find the greatest decrease in monthly profits and its corresponding month
    min_monthly_profit_difference = min(list_of_differences)
    min_index = list_of_differences.index(min_monthly_profit_difference)
    min_month = list_of_months[min_index+1]

    
##Write analysis to text file
output_path = os.path.join(os.getcwd(), 'Analysis', 'results.txt')
with open(output_path, 'w') as text_file:
    text_file.write("Financial Analysis\n--------------------\n" )
    text_file.write(f"Total Months : {total_months}\n")
    text_file.write(f"Total: ${net_total}\nAverage Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {max_month} (${max_monthly_profit_difference})\n")
    text_file.write(f"Greatest Decrease in Profits: {min_month} (${min_monthly_profit_difference})")

 
