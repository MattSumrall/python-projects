# William Sumrall
# ITEC 1250
# Chapter 2 Challenge 4
# Car Salesman Program

print("Car sales receipt")

basePrice = float(input("\nEnter car price here: "))

tax = .07
licCharge = .08
dealerPrep = 30
desCharge = 200

salesTax = basePrice * tax

licenceFee = basePrice * licCharge

total = basePrice + dealerPrep + desCharge + salesTax + licenceFee

print("\nSales Tax: $" + format(salesTax, ",.2f"),
      "\nLicence Fee: $" + format(licenceFee, ",.2f"),
      "\nPreparation Charge: $" + format(dealerPrep, ",.2f"),
      "\nShipping: $" + format(desCharge, ",.2f"))

print("\nTotal $" + format(total, ",.2f"))

input("\nPress enter to continue.")
