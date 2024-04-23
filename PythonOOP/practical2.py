class Numbers:
    def __init__(self, num) -> None:
        self.number = num
    
    def __add__(self, *args):
        temp = []
        for i in range(0, len(args)):
            if isinstance(args[i], Numbers):
                temp.append(args[i].number)
            else:
                raise TypeError("Unsupported operand type. Must be an instance of Numbers")
        return temp
    
    def __pow__(self, other):
        if isinstance(other, Numbers):
            return self.number ** other.number
        else:
            raise TypeError("Unsupported operand type. Must be an instance of Numbers")
        
    def __lt__(self, other):
        if isinstance(other, Numbers):
            return True if self.number < other.number else False
        else:
            raise TypeError("Unsupported operand type. Must be an instance of Numbers")

    def __gt__(self, other):
        if isinstance(other, Numbers):
            return True if self.number < other.number else False
        else:
            raise TypeError("Unsupported operand type. Must be a an instance of Numbers")
    
class NumberOperations:
    def __init__(self, num1:Numbers, num2:Numbers) -> None:
        self.num1 = num1
        self.num2 = num2

    def add(self) -> int:
        return self.num1 + self.num2

    def baseAndPower(self) -> int:
        return self.num1 ** self.num2
    
    def concatenation(self) -> str:
        return str(self.num1) + str(self.num2) 
    
    def max(self) -> int:
        return self.num1 if self.num1 > self.num2 else self.num2
    
    def min(self) -> int:
        return self.num1 if self.num1 < self.num2 else self.num2


a = Numbers(5)
b = Numbers(2)
c = Numbers(2)
print(a+b+c)
