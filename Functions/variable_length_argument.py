# assume we want to calcualte the  volume of a cuboid

# the asterisk is used to pass multiple values

def v_l_a(*var):
    print(var)
    return sum(var)
print(v_l_a(10,20,20))


#Swapping the numbers with temp variable
def Swaping_Numbers(x,y):
    print(x,y)
    temp=x
    x=y
    y=temp
    
    print(x,y)
Swaping_Numbers(10,20)