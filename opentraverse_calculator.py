#Open Traverse Calculator
import math
print("""
This program calculates the coordinates in open traverse serie
----------------------------------------------------------------
""",end="")

id_ = []
coord_y = []
coord_x = []
traverse = []
distance = []
azimuth_list = []
delta_y = []
delta_x = []
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


id_.append(input("Enter the point ID of first known point :")) #id_[0]
coord_y.append(float(input("Enter the Y coordinates of first known point (m):"))) #coord_y[0]
coord_x.append(float(input("Enter the X coordinates of first known point (m):"))) #coord_x[0]

id_.append(input("Enter the point ID of second known point :")) #id_[1]
coord_y.append(float(input("Enter the Y coordinates of second known point (m):"))) #coord_y[1]
coord_x.append(float(input("Enter the X coordinates of second known point (m):"))) #coord_x[1]

azimuth_A_B = azimuth(coord_x[0],coord_y[0],coord_x[1],coord_y[1]) #AzimuthAB
azimuth_list.append(azimuth_A_B) #[0]
number_unknown = int(input("Enter the number of unknown traverse points: "))
for i in range(1,number_unknown+1):
    id_.append(input("Enter the point ID of unknown point {} :".format(i))) #id_[1+i]

for i in range(1,number_unknown+1):
    traverse.append(float(input("Enter the traverse angel of {} (grad) :".format(id_[i]))))

for i in range(1,number_unknown+1):
    distance.append(float(input("Enter the horizontal distance between {} and {} (m) :".format(id_[i],id_[i+1]))))

def azi_(t,a): #Azimuth calc
    azi = a+t
    if azi < 200:
        azi = azi + 200
    elif (azi > 200) and (azi < 600):
        azi = azi - 200
    elif (azi > 600):
        azi = azi - 600
    return azi

azimuth_list.append((azi_(traverse[0],azimuth_list[0])))
for i in range(1,len(traverse)):
    azimuth_list.append(azi_(float(traverse[i]),float(azimuth_list[i])))


def deltay(distance,azimuth):
    dy = distance * math.sin(azimuth)
    return dy
def deltax(distance,azimuth):
    dx = distance * math.cos(azimuth)
    return dx
for i in range(1,len(distance)+1):
    delta_x.append(deltax(distance[i-1],azimuth_list[i]*math.pi/200))
    delta_y.append(deltay(distance[i-1],azimuth_list[i]*math.pi/200))

for i in range(1,len(delta_y)+1):
    coord_y.append(coord_y[i]+delta_y[i-1])
    coord_x.append(coord_x[i]+delta_x[i-1])

print("")
print("{: >12}{: >12}{: >12}{: >12}{: >12}".format("Point ID","Point ID","Azimuth","Delta Y","Delta X"))
print("-"*60)
print("{: >12}{: >12}{: >12.4f}{: >12}{: >12}".format(id_[0],id_[1],azimuth_list[0],"",""))
for i in range(1,len(id_)-1):
    print("{: >12}{: >12}{: >12.4f}{: >12.2f}{: >12.2f}".format(id_[i],id_[i+1],azimuth_list[i],delta_y[i-1],delta_x[i-1]))
print("-"*60)
print("{:>16}{:>16}{:>16}".format("Point ID","Coordinate(Y)","Coordinate(X)"))
print("-"*48)
for i in range(2,len(id_)):
    print("{:>16}{:>16.2f}{:>16.2f}".format(id_[i],coord_y[i],coord_x[i]))
print("-"*48)















