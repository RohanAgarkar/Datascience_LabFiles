class NumberList:
    def __init__(self, *args):
        self.args = args;

    def Sum(self) -> tuple:
        self.newList = []
        if len(self.args) % 2 != 0:
            self.newList.append(self.args[len(self.args)//2])
        for i in range(0, int(len(self.args)/2)):
            self.newList.append(self.args[i]+self.args[len(self.args)-1-i])
        return tuple(set(self.newList))
    
if __name__ == "__main__":
    num = NumberList(1,5,10,15,20)
    print(num.Sum())