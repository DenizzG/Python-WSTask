dimension1 = int(input("Please enter the first dimensions of the room = "))
dimension2 = int(input("Please enter the second dimensions of the room = "))


Tunpaintable = int(input("Please enter the dimensions of the unpaintable areas = "))
Tcoats = int(input("How many coats of paint are required? = "))

sq = (dimension1 * dimension2) - Tunpaintable
Tsq = sq*Tcoats
Anwser = Tsq/11

print("in total you will need", Anwser, " amount of paint")
