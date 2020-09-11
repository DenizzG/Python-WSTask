PCarMil = int(input("How many miles was the car on before? = "))
NCarMil = int(input("How many miles is the car on now? = "))
tot = int(input("What is the total number of litres taken to fill the tank? = "))

Miles = NCarMil - PCarMil
anw = Miles/tot
print("you car does ", anw," miles per gallon")
