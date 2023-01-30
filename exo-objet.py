#************************
#* En commentaire tous mes tests
#***********************

#class Robot_deplacement:
#    "La classe: robot"

#Robot_deplacement()
#r = Robot_deplacement()


#print(r.__doc__) # affiche ce que j'ai ecrit dans la classe

#print(r) #  affiche une adresse précise en hexa



class Robot:
    "Le robot peut se déplacer, communiquer et etre réparé (normalement)"
    def __init__(self, Alice, LaGlisse):
        self.deplace = True
        self.parler = True
        self.reparage = True

#    def deplace(self, dx, dy):
#        self.x = self.x + dx
#        self.y = self.y + dy
#        r = Robot()
#        r.x = 1
#        r.y = 2
#        print("Coordonnées du Robot : x =", r.x, "y =", r.y)
#        r.deplace(3, 5)
#        print("Coordonnées du Robot : x =", r.x, "y =", r.y)

    def deplace(self):
        if self.deplace:
            print("je peux marcher")
        else:
            print("je ne peux pas marcher")


#    def parler(self, message):
#        self.message = message
#        message1 = Robot("mon message :", self.message)

    def parler(self):
        if self.parler:
            print("J'ai un message")
        else:
            print("je n'ai pas de message")

#for i in range (0,10):
#    deplace()

#if parler()

    def reparage(self):
        if self.reparage:
            print("je peux etre réparé")
        else:
            print("je ne peux pas etre réparé")

