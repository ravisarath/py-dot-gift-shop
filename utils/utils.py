class Operations(object):

    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b
        self.__sum = 0

    def addition(self):
        self.__sum = self.a +self.b
        return self.__sum
    
    def substraction(self):
        sub = self.a-self.b
        return sub
    
    @staticmethod
    def multiply(a, b):
        return a*b
    
    
    def __call__(self):
        return self.substraction()
    
    def __str__(self):
        return "operations methos"
    
    
    
