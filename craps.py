from random import randint
class diceNumber:
    def __init__(self):
        pass
    def number(self):
        num=randint(2,12)
        return num

    def winOrLoss(self,num):
        num=number()
        if((num) in (7,11)):
            return "You win"
        elif((num) in (2,3,12)):
            return "You losts"
        elif((num) in (4,5,6,8,9,10)):
            return "You win"
