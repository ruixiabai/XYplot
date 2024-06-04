# list
Stuff=["Earth", "Moon", "Jupiter"]
Third=Stuff[2]
Stuff2=["Apple","Salad","Cake"]
Mystuff=Stuff+Stuff2
Mystuff.append("hammer")
Length=len(Mystuff)
Yourstuff=Mystuff[0:4]  #First three things
Herstuff=Mystuff[-4:-1] #Last three things


############################################
#Dictionary
#A key to a value
#stuff, destination, partner
Myquest={
    "stuff": Mystuff,
    "destination":34.4,
    "people":"Rita"}
Myquest["people"]
#############################
#Tuples
#use ()
for item in Mystuff:
    print(item)

for idx,item in enumerate(Mystuff):
    print(str(idx)+ ":" + item)


