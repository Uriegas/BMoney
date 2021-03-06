class BMoney:
    def __init__(self, money = 0.0):
        self.money = money
    def madd(self, m1, m2):
        self.putMoney( m1 + m2 )

    def getMoney(self):
        return self.money

    def putMoney(self, money):
        self.money = money
        return self.money

    def __add__(self, m2):
        return BMoney(self.money + m2.getMoney())
    
    def __sub__(self, other):
        return BMoney(self.money - other.getMoney())
    
    def __mul__(self, other):
        return BMoney(self.money * other.getMoney())

    #Returns BMoney
    def __truediv__(self, other):
        return BMoney(self.money / other.money)
    
    #Returns float
    def __truediv__(self, other):
        return self.money / other.money

if __name__ == '__main__':
    dolares = BMoney()
    d1 = BMoney(10.1)
    d2 = BMoney(10)
    print(dolares.getMoney())

    d3 = d1+d2
    print(d3.getMoney())
    d3 = d1-d2
    print(d3.getMoney())
    