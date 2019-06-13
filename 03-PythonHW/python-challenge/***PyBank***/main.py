# imports
import os, csv

# set file path
csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path, newline="", encoding="UTF8") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    next(csv_reader)
  
    #Establish lists
    Row_numbers = []
    NetProfitLoss = []


    for row in csv_reader:
        Row_numbers.append(row[0])
        NetProfitLoss.append(float(row[1]))
    
    Great_Increase = max(NetProfitLoss)
    Great_Increase_index= NetProfitLoss.index(max(NetProfitLoss))
    Great_Increase_month= Row_numbers[Great_Increase_index]
    Great_Decrease = min(NetProfitLoss)
    Great_Decrease_index= NetProfitLoss.index(min(NetProfitLoss))
    Great_Decrease_month= Row_numbers[Great_Decrease_index]

    print("Financial Analysis")
    print("-"*20)
    print(f"Total months: {len(Row_numbers)}")
    print(f"Total : {sum(NetProfitLoss)}")
    print(f"Average: {(sum(NetProfitLoss))/(len(Row_numbers))}") 
    print(f"Greatest increase: {Great_Increase_month} {Great_Increase}")
    print(f"Greatest decrease: {Great_Decrease_month} {Great_Decrease}")

    f= open("FinancialAnalysis.txt", "w+")
    f.write("Financial Analysis\n")
    f.write("-"*20 + "\n")
    f.write(f"Total months: {len(Row_numbers)}\n")
    f.write(f"Total : {sum(NetProfitLoss)}\n")
    f.write(f"Average: {(sum(NetProfitLoss))/(len(Row_numbers))}\n") 
    f.write(f"Greatest increase: {Great_Increase_month} {Great_Increase}\n")
    f.write(f"Greatest decrease: {Great_Decrease_month} {Great_Decrease}\n")
    f.close()