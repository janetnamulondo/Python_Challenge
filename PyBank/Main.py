
#import Files 
import csv
import os 

#Path to collect data from the resource folder
Budget_data_csv = os.path.join('..' , 'Budget_data.csv')

#Define variables  
Total_Months = 0 
PnL_Total = 0 
Av_netchange = 0 
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999] 
cur_amount = 0
prev_amount = 0
cur_month = []
month_to_month_pnl = []
Net_change = 0
total_monthly_change = 0
Month_of_Change = []

#Read the Budget_data.csv 
with open(Budget_data_csv, newline="") as csvfile:

    #Split the data on commas in Rows
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header 
    csv_header = next(csvreader)
    first_row = next(csvreader)
    Total_Months = Total_Months + 1
    PnL_Total = PnL_Total + int(first_row[1])
    prev_amount = int(first_row[1])
    

    # Read through each row to add data to lists 
    for row in csvreader:
      
    #The total months in the Data base can be found by 
        Total_Months = Total_Months + 1
     
    #The net amount of Profit/Losses over time can be found by 
        PnL_Total = PnL_Total + int(row[1])
       
    #Average in the changes in Profit/Losses over the entire period can be found by
        Net_change =   int(row[1]) - prev_amount
        prev_amount = int(row[1])
        month_to_month_pnl = month_to_month_pnl + [Net_change]
        Av_netchange =sum(month_to_month_pnl)/len(month_to_month_pnl)
          
    #The greatest increase in profit (Date and amount) can be found by 
        if Net_change > greatest_increase[1]:
           greatest_increase[0] = row[0]
           greatest_increase[1] = Net_change
   
    #The greates decrease in profit (Date and amount) can be found by 
        if Net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = Net_change
   

print("Financial Statement") 
print("--------------------------------------------------------------------------------")
print(f"Total Months: {Total_Months} ")
print(f"PnL Total: ${PnL_Total}")
print(f"Average Net Change: (round(${Av_netchange}),2)")
print(f"Greatest increase month in profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest decrease month in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

          


       

  
     
        
