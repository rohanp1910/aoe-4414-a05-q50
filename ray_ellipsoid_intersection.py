# ray_ellipsoid_intersection.py
# Written by Rohan Palande
# Other contributors: None

# import Python modules

import math # math 
import sys # argv

#constants 

re_KM = 6378.137
eE    = 0.081819221456

# Initialize Script Arguments

d_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 
c_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 

# Parse Script Arguments

if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()

#write script below this line

a = d_l_x*d_l_x + d_l_y*d_l_y + (d_l_z*d_l_z)/(1-eE*eE)
b = 2*(d_l_x*c_l_x+d_l_y*c_l_y+(d_l_z*c_l_z)/(1-eE**2))
c = c_l_x**2+c_l_y**2+(c_l_z**2)/(1-eE**2)-re_KM**2
disc = b*b-4.0*a*c

#Find discriminant using class slides

disc = (b**2 -4*a*c)
if disc >= 0:
    d = (-b - math.sqrt(disc))/(2*a)
    if d < 0:
        d = (-b + math.sqrt(disc))/(2*a)
    if d > 0:
        l_d = [d*d_l_x+c_l_x, d*d_l_y+c_l_y, d*d_l_z+c_l_z]

print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point
