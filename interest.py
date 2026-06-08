principal_amount = int(input("enter investment amount :"))
principal_amount =float(principal_amount)

annual_interest = int(input("enter annual interest:"))
annual_interest = float(annual_interest)

rate = annual_interest/100

cmp_int_5 = principal_amount * (1 + rate) ** 5 
cmp_int_10 = principal_amount * (1 + rate) ** 10
cmp_int_15 = principal_amount * (1 + rate) ** 15

doubling_years = int(72// annual_interest)
print (f"investment:{principal_amount:.2f}")
print (f"annual interest:{annual_interest:.2f}")
print (f"balance 5 years:{cmp_int_5:.2f}")
print (f"balance 10 years:{cmp_int_10:.2f}")
print (f"balance 15 years:{cmp_int_15:.2f}")
print (f"doubling years: {doubling_years:.2f}")

if (doubling_years % 2==0) :
    print("doubling years are even ")
else:
    print(" doubling years are odd")

