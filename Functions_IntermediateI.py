import random
def randInt(min=0, max=100):
    num = random.random()          
    result = num * (max - min) + min  
    return round(result)            
print(randInt())              
print(randInt(max=50))        
print(randInt(min=50))       
print(randInt(min=50, max=500))