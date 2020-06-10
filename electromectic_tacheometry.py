#Electrometric Tacheometry
import math

print("""
Program for Electrometric Tacheometry Computation
---------------------------------------------------
""",end="")

id_ = []
y = []
x = []
height = []



id_.append(input("Enter the stationary traverse ID :")) #id_[0]
id_.append(input("Enter the referenced traverse ID :")) #id_[1]

for i in range(len(id_)-1,-1,-1):
    y.insert(0,float(input("Enter the Y coordinates of {} (m) :".format(id_[i]))))
    x.insert(0,float(input("Enter the X coordinates of {} (m) :".format(id_[i]))))
    height.insert(0,float(input("Enter the height of {} (m) :".format(id_[i]))))

id_.append(input("Enter the point ID of detail point :"))
horizontal = float(input("Enter the horizontal direction of point {} (grad) :".format(id_[-1])))
vertical = float(input("Enter the vertical direction of point {} (grad) :".format(id_[-1])))
slope = float(input("Enter the slope distance between {} and {} (m) :".format(id_[0],id_[-1])))
inst_h = float(input("Enter the height of instrument (m) :"))
ref_h = float(input("Enter the height of reflector (m) :"))

horizontal_rad = (horizontal / 200) * math.pi
vertical_rad = (vertical / 200) * math.pi
deltaH = slope*math.cos(vertical_rad) + inst_h - ref_h

height.append(height[0]+deltaH)

horizontal_dist = slope * math.sin(vertical_rad)

def azimuth(x1,y1,x2,y2):
    if (x2-x1) == 0:
        azi_grad = 100
    elif (y2 - y1) == 0:
        azi_grad = 200
    else:
        azimuth = math.atan(abs((y2-y1)/(x2-x1)))
        azimuth_grad = azimuth*200/math.pi
        if ((y2-y1) > 0) and ((x2-x1) > 0):
            azi_grad = azimuth_grad
        elif ((x2-x1) < 0) and ((y2-y1) > 0):
            azi_grad = 200 - azimuth_grad
        elif ((x2-x1) > 0) and ((y2-y1) < 0):
            azi_grad = 400 - azimuth_grad
        elif ((x2-x1) < 0) and ((y2-y1) < 0):
            azi_grad = 200 + azimuth_grad
    return azi_grad

azimuth1 = azimuth(x[0],y[0],x[1],y[1])

def azi_(t,a): #Azimuth calc
    azi = a+t
    if azi < 200:
        azi = azi + 200
    elif (azi > 200) and (azi < 600):
        azi = azi - 200
    elif (azi > 600):
        azi = azi - 600
    return azi
azimuth2 = azi_(azimuth1,horizontal)
azi2_rad = azimuth2*math.pi/200


x.append(x[0] + horizontal_dist * math.cos(azi2_rad))
y.append(y[0]+ horizontal_dist * math.sin(azi2_rad))


print("")
print("{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}{:<12}".format("Point ID","Point ID","Hor. Dist.","Delta H","Elevation","Coord. (Y)","Coord. (X)"))
print("-"*84)
print("{:<12}{:<12}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}{:<12.3f}".format(id_[0],id_[-1],horizontal_dist,deltaH,height[-1],y[-1],x[-1]))
print("-"*84)
