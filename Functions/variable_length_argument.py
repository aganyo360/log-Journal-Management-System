# assume we want to calcualte the  volume of a cuboid

# the asterisk is used to pass multiple values

def v_l_a(*var):
    return sum(var)
print(v_l_a(10,20,20))