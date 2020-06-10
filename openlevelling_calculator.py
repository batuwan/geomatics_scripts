#Open Levelling Network Calculator


print("""
This program calculates the elevations in open levelling net
----------------------------------------------------------------
""",end="")


id_ = []
elev = []
bs = []
fs = []
deltah = []

id_.append(input("Enter the point ID of known point:")) #id_[0]
elev.append(float(input("Enter the elevation of point {} (m) :".format(id_[0])))) #elev[0]

number_unknown = int(input("Enter the number of unknown points : "))

for i in range(1,number_unknown+1):
    id_.append(input("Enter the point ID of unknown point {} :".format(i))) #id_[i]

bs.append(float(input("Enter the BS reading of point {} :".format(id_[0])))) #BS of 1st point

for i in range(1,number_unknown):
    fs.append(float(input("Enter the FS reading of point {} :".format(id_[i])))) #FS
    bs.append(float(input("Enter the BS reading of point {} :".format(id_[i])))) #BS

fs.append(float(input("Enter the FS reading of point {} :".format(id_[-1])))) #FS of last point

for i in range(0,len(fs)):
    deltah.append(bs[i]-fs[i])

for i in range(0,len(deltah)):
    elev.append(deltah[i]+elev[i])

print("")
print("{: <12}{: <12}{: <12}".format("Point ID","Point ID","Delta H"))
print("-"*36)
for i in range(0,len(deltah)):
    print("{: <12}{: <12}{: <12.3f}".format(id_[i], id_[i + 1], deltah[i]))
print("-"*36)
print("")
print("{: <12}{: <12}".format("Point ID","Elevation"))
print("-"*24)
for i in range(1,len(elev)):
    print("{: <12}{: <12.3f}".format(id_[i],elev[i]))
print("-"*24)









