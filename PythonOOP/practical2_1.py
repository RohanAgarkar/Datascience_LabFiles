class Numbers:
    def __init__(self, number):
        self.number = number
    
    def add(self, other) -> int: 
        if isinstance(other, Numbers):
            return self.number + other.number
        else:
            raise TypeError("The arguments are not an instance of a number")
    
    def pow(self, other) -> int: 
        if isinstance(other, Numbers):
            return self.number ** other.number
        else:
            raise TypeError("The arguments are not an instance of a number")
    
    def concat(self, other) -> str: 
        if isinstance(other, Numbers):
            return str(self.number) + str(other.number)
        else:
            raise TypeError("The arguments are not an instance of a number")
        
    def max_min(self, other, max=True) -> int: 
        if isinstance(other, Numbers):
            if max:
                return self.number if self.number > other.number else other.number
            else:
                return self.number if self.number < other.number else other.number
        else:
            raise TypeError("The arguments are not an instance of a number")
        

a = Numbers(3)
b = Numbers(2)

print(a.add(b))
print(a.pow(b))
print(a.concat(b))
print(a.max_min(b)) # for max
print(a.max_min(b, False)) # for min


