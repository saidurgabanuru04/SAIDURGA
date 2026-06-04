principal_amount = int(input("enter investment amount :"))
principal_amount =float(principal_amount)

annual_interest = int(input("enter annual amount:"))
annual_interest = float(annual_interest)

rate = annual_interest/100

cmp_int_5 = principal_amount * (1 + rate) ** 5 
cmp_int_5 = principal_amount * (1 + rate) ** 10
cmp_int_5 = principal_amount * (1 + rate) ** 15