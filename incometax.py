# Calculates income tax based on given income and tax rules.
# Tax brackets and rates.
# Calculate tax for each bracket.
# Calculate tax for the remaining income. 
# Using elif statement.

income = 45000

tax_payable = 0
if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * 0.1
else:
    tax_payable = 10000 * 0.1 + (income - 20000) * 0.2

print("Total tax to pay is", tax_payable)