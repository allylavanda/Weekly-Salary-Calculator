print("Welcome to Danni's Weekly Salary Calculator!")
taxInput = input('What is your estimated Tax Rate?')
tax = float(taxInput)
wageInput = input('What is your current hourly wage?')
wage = float(wageInput)
hoursInput = input('How many hours have you worked this week?')
hoursInput = float(hoursInput)
grossSalary = hoursInput * wage
estTax = grossSalary * tax
netSalary = grossSalary - tax
print('Your Net Salary for this week is' , netSalary, '!')
input('Thank you! Please press enter to exit.')
