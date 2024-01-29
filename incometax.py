# Calculates income tax based on given income and tax rules.
# Tax brackets and rates.
# Calculate tax for each bracket.
# Calculate tax for the remaining income. 4

def calculate_income_tax(taxable_income):

    brackets = [10000, 10000]
    rates = [0, 0.1]

    tax = 0
    for i in range(len(brackets)):
      if taxable_income <= brackets[i]:
        tax += taxable_income * rates[i]
        break
    else:
      tax += brackets[i] * rates[i]
      taxable_income -= brackets[i]

    tax += taxable_income * rates[-1]
    return tax

taxable_income = 45000
income_tax = calculate_income_tax(taxable_income)
print(f"Income tax payable for ${taxable_income:,.2f} is ${income_tax:,.2f}")