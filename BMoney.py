class BMoney:
    def __init__(self, money = 0.0):
        self.money = money
    def madd(self, m1, m2):
        self.putMoney( m1 + m2 )

    def getMoney(self):
        return self.money

    def putMoney(self, money):
        self.money = money

    def __add__(self, m2):
        return self.money + m2.getMoney()


if __name__ == '__main__':
    dolares = BMoney()
    d1 = BMoney(10.1)
    d2 = BMoney(10)
    print(dolares.getMoney())
    dolares.madd(d1, d2)
    print(dolares.getMoney())
    