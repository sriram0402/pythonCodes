from dice import Die
class Player(object):

    def __init__(self):
        self.die1=Die()
        self.die2=Die()

        self.rolls=[]
    def Play(self):

        self.rolls=[]
        self.die1.roll()
        self.die2.roll()
        (v1,v2)=(self.die1.getValue(),self.die2.getValue())

        self.rolls.append((v1,v2))

        initalsum=v1+v2
        if initialsum in (7,11):
            return True
        elif initalsum in (2,3,12):
            return False


        while True:
            self.rolls=[]

            self.die1.roll()
            self.die2.roll()

            (V1,v2)=(self.die1.getValue(), self.die2.getValue())

            sumValues=v1+v2

            if sumValues==7:
                return False
            elif sumValues==initalsum:
                return Trues
        
