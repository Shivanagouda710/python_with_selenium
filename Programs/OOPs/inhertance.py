



class vehicale:
    def engine(self):
        print(" This has engine ")

    def wheels(self):
        print(" This hav 4 wheels ")


class car(vehicale):
    def car_speed(self):
        print("My car speed is 500km/hr")




Objcar = car()
Objcar.car_speed()
Objcar.engine()
Objcar.wheels()
