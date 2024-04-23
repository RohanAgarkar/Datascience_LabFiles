# you are driving a little too fast, and a police officer stops you. Write a function 
def check(speed: int):
    if speed < 0:
        return 'speed cannot be negative'
    if speed <= 60:
        return 'no ticket'
    elif (speed <= 80):
        return 'small ticket'
    else:
        return 'big ticket'
    
print(check(25))
print(check(75))
print(check(125))
