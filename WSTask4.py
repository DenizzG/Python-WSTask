Nst = int(input("How many students are there? = "))
Nbk = int(input("How many books are there? = "))

Books_per_s = int(Nst % Nbk)
remaining = Nbk %Nst

print("Each student gets " , Books_per_s, " books and there are ", remaining, " books left over.")

## ACS - I don't think this works??? Haqve another look
