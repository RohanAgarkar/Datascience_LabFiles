# create a function that grabs the email website domain from a strign the form 

def grab(email:str):
    return email.split('@')[1]

print(grab('user@domain.com'))