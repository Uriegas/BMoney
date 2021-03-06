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

    #Multiply instance by float, return float
    def __mul__(self, other):
        return other * self.money

    #Returns BMoney
    def __truediv__(self, other):
        return BMoney(self.money / other.money)
    
    #Returns float
    def __truediv__(self, other):
        return self.money / other
    
    #Divides a float by a BMoney instance
    #https://cutt.ly/izyhMOR
    def __rtruediv__(self, other):
        return other / self.money

    def __str__(self):
        return str(self.money)

##Main
if __name__ == '__main__':
    while(True):
        #Save as BMoney
        a = BMoney(float(input("Enter a num > ")))
        #Save as float
        b = float(input("Enter a float > "))
        #Perform all 7 operations
        print("float + BMoney: ", a + BMoney(b))
        print("float - BMoney: ", a - BMoney(b))
        print("float * BMoney: ", a * b)
        print("BMoney * BMoney: ", a * BMoney(b))
        print("BMoney / BMoney: ", a / BMoney(b))
        print("BMoney / float: ", a / b)
        print("float / BMoney: ", b / a)
        print()