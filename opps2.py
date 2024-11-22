class species:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def song(self,song):
        self.song = song
        print("{} sings {}".format(self.name,self.song))

molly=species("molly",3)
blu=species("blu",4)
print("molly is a {} ".format(molly.species))
print("blu is a {} ".format(blu.species))
print("name of 1st bird is {} she is {} years old".format(molly.name,molly.age))
print("name of 2nd bird is {} he is {} years old".format(blu.name,blu.age))
print(molly.song("molly,chacha"))
print(blu.song("blu,blues"))