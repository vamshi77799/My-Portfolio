import pandas as pd
import matplotlib.pyplot as plt
import math as mp
import numpy as np
import os

# 1. Get the folder where THIS script (another.py) is located
script_location = os.path.dirname(os.path.abspath(__file__))

# 2. Build the full path to the CSV file dynamically
# This tells Python: "Start at the script's location, go into 'numbers', find the CSV"
csv_path = os.path.join(script_location, "numbers", "NACA 9412 copy.csv")


# Load the file, telling pandas that the header is on the 6th row (index 5)
df = pd.read_csv(csv_path, header=5)
# Now you can directly access the 'X' column
x_values = df['X']
y_values=df["Yc"]
chord_x=df["Chord X"]
chord_y=df["Chord Y"]
xu_ = df["xu"]
yu_= df["yu"]
xl_ = df["xl"]
yl_ = df["yl"]

#For 2nd fig
aoa1=mp.radians(-5)
x_values1=[]
y_values1=[]

for i,m in zip(x_values,y_values):
    v=mp.cos(aoa1)*i - mp.sin(aoa1)*m
    w=mp.sin(aoa1)*i + mp.cos(aoa1)*m
    x_values1.append(v)
    y_values1.append(w)

chord_x1=[]
chord_y1=[]

for i,m in zip(chord_x,chord_y):
    v=mp.cos(aoa1)*i - mp.sin(aoa1)*m
    w=mp.sin(aoa1)*i + mp.cos(aoa1)*m
    chord_x1.append(v)
    chord_y1.append(w)

xu1_=[]
yu1_=[]
xl1_=[]
yl1_=[]

for i,m in zip(xu_,yu_):
    v=mp.cos(aoa1)*i - mp.sin(aoa1)*m
    w=mp.sin(aoa1)*i + mp.cos(aoa1)*m
    xu1_.append(v)
    yu1_.append(w)

for i,m in zip(xl_,yl_):
    v=mp.cos(aoa1)*i - mp.sin(aoa1)*m
    w=mp.sin(aoa1)*i + mp.cos(aoa1)*m
    xl1_.append(v)
    yl1_.append(w)
# Angle attack = 0°
fig, a=plt.subplots(nrows=2,ncols=2,figsize=(25,15),dpi=50)
a[0,0].plot(x_values,y_values,'--',markersize=3,c='black',label="Mean Camber Line")
a[0,0].set_title("NACA 9412",fontsize=20,color='red')
a[0,0].set_xlabel("X_Axis",fontsize=10)
a[0,0].set_ylabel("y_Axis",fontsize=10)
a[0,0].tick_params(axis="both",which="major",size=10,labelsize=15)
a[0,0].set(xlim=(-0.1,1.5),xticks=np.arange(0.5,1.6,0.5))
a[0,0].set(ylim=(-0.4,0.5),yticks=np.arange(-0.2,1,0.2))
a[0,0].plot(chord_x,chord_y,'r--',label="Chord Line")
a[0,0].plot(xu_,yu_,'g',label="Upper Surface")
a[0,0].plot(xl_,yl_,'b',label="Lower Surface")
a[0,0].legend(fontsize=10)
a[0,0].text(1.1,0.5,"AOA = 0°",c='blue',fontsize=20)


# angle of attack = 5°
a[0,1].plot(x_values,y_values,'--',markersize=3,c='grey',alpha=0.5)
a[0,1].set_title("NACA 9412",fontsize=20,color='red')
a[0,1].set_xlabel("X_Axis",fontsize=10)
a[0,1].set_ylabel("y_Axis",fontsize=10)
a[0,1].tick_params(axis="both",which="major",size=10,labelsize=15)
a[0,1].set(xlim=(-0.1,1.5),xticks=np.arange(0.5,1.6,0.5))
a[0,1].set(ylim=(-0.4,0.5),yticks=np.arange(-0.2,1,0.2))
a[0,1].plot(chord_x,chord_y,'--',c='grey',alpha=0.5)
a[0,1].plot(xu_,yu_,c='grey',alpha=0.5)
a[0,1].plot(xl_,yl_,c='grey',alpha=0.5)
a[0,1].plot(x_values1,y_values1,'--',markersize=3,c='black',label="Mean Camber Line")
a[0,1].set_title("NACA 9412",fontsize=20,color='red')
a[0,1].set_xlabel("X_Axis",fontsize=10)
a[0,1].set_ylabel("y_Axis",fontsize=10)
a[0,1].tick_params(axis="both",which="major",size=10,labelsize=15)
a[0,1].set(xlim=(-0.1,1.5),xticks=np.arange(0.5,1.6,0.5))
a[0,1].set(ylim=(-0.4,0.5),yticks=np.arange(-0.2,1,0.2))
a[0,1].plot(chord_x1,chord_y1,'r--',label="Chord Line")
a[0,1].plot(xu1_,yu1_,'g',label="Upper Surface")
a[0,1].plot(xl1_,yl1_,'b',label="Lower Surface")
a[0,1].legend(fontsize=10)
a[0,1].text(1.1,0.5,"AOA = 5°",c='blue',fontsize=20)



#For 3rd fig
aoa2=mp.radians(-10)
x_values2=[]
y_values2=[]

for i,m in zip(x_values,y_values):
    v=mp.cos(aoa2)*i - mp.sin(aoa2)*m
    w=mp.sin(aoa2)*i + mp.cos(aoa2)*m
    x_values2.append(v)
    y_values2.append(w)

chord_x2=[]
chord_y2=[]

for i,m in zip(chord_x,chord_y):
    v=mp.cos(aoa2)*i - mp.sin(aoa2)*m
    w=mp.sin(aoa2)*i + mp.cos(aoa2)*m
    chord_x2.append(v)
    chord_y2.append(w)

xu2_=[]
yu2_=[]
xl2_=[]
yl2_=[]

for i,m in zip(xu_,yu_):
    v=mp.cos(aoa2)*i - mp.sin(aoa2)*m
    w=mp.sin(aoa2)*i + mp.cos(aoa2)*m
    xu2_.append(v)
    yu2_.append(w)

for i,m in zip(xl_,yl_):
    v=mp.cos(aoa2)*i - mp.sin(aoa2)*m
    w=mp.sin(aoa2)*i + mp.cos(aoa2)*m
    xl2_.append(v)
    yl2_.append(w)

a[1,0].plot(x_values,y_values,'--',markersize=3,c='grey',alpha=0.5)
a[1,0].set_title("NACA 9412",fontsize=20,color='red')
a[1,0].set_xlabel("X_Axis",fontsize=10)
a[1,0].set_ylabel("y_Axis",fontsize=10)
a[1,0].tick_params(axis="both",which="major",size=10,labelsize=15)
a[1,0].set(xlim=(-0.1,1.5),xticks=np.arange(0.5,1.6,0.5))
a[1,0].set(ylim=(-0.4,0.5),yticks=np.arange(-0.2,1,0.2))
a[1,0].plot(chord_x,chord_y,'--',c='grey',alpha=0.5)
a[1,0].plot(xu_,yu_,c='grey',alpha=0.5)
a[1,0].plot(xl_,yl_,c='grey',alpha=0.5)
a[1,0].plot(x_values2,y_values2,'--',markersize=3,c='black',label="Mean Camber Line")
a[1,0].set_title("NACA 9412",fontsize=20,color='red')
a[1,0].set_xlabel("X_Axis",fontsize=10)
a[1,0].set_ylabel("y_Axis",fontsize=10)
a[1,0].tick_params(axis="both",which="major",size=10,labelsize=15)
a[1,0].set(xlim=(-0.1,1.5),xticks=np.arange(0.5,1.6,0.5))
a[1,0].set(ylim=(-0.4,0.5),yticks=np.arange(-0.2,1,0.2))
a[1,0].plot(chord_x2,chord_y2,'r--',label="Chord Line")
a[1,0].plot(xu2_,yu2_,'g',label="Upper Surface")
a[1,0].plot(xl2_,yl2_,'b',label="Lower Surface")
a[1,0].legend(fontsize=10)
a[1,0].text(1.1,0.5,"AOA = 10°",c='blue',fontsize=20)

# For 4th fig (a[1,1])
aoa3 = mp.radians(-15)
x_values3 = []
y_values3 = []

# Rotate Mean Camber Line
for i, m in zip(x_values, y_values):
    v = mp.cos(aoa3) * i - mp.sin(aoa3) * m
    w = mp.sin(aoa3) * i + mp.cos(aoa3) * m
    x_values3.append(v)
    y_values3.append(w)

chord_x3 = []
chord_y3 = []

# Rotate Chord Line
for i, m in zip(chord_x, chord_y):
    v = mp.cos(aoa3) * i - mp.sin(aoa3) * m
    w = mp.sin(aoa3) * i + mp.cos(aoa3) * m
    chord_x3.append(v)
    chord_y3.append(w)

xu3_ = []
yu3_ = []
xl3_ = []
yl3_ = []

# Rotate Upper Surface
for i, m in zip(xu_, yu_):
    v = mp.cos(aoa3) * i - mp.sin(aoa3) * m
    w = mp.sin(aoa3) * i + mp.cos(aoa3) * m
    xu3_.append(v)
    yu3_.append(w)

# Rotate Lower Surface
for i, m in zip(xl_, yl_):
    v = mp.cos(aoa3) * i - mp.sin(aoa3) * m
    w = mp.sin(aoa3) * i + mp.cos(aoa3) * m
    xl3_.append(v)
    yl3_.append(w)

# Plotting the 4th subplot
# 1. Plot the ghost (grey) original airfoil
a[1,1].plot(x_values, y_values, '--', markersize=3, c='grey', alpha=0.5)
a[1,1].plot(chord_x, chord_y, '--', c='grey', alpha=0.5)
a[1,1].plot(xu_, yu_, c='grey', alpha=0.5)
a[1,1].plot(xl_, yl_, c='grey', alpha=0.5)

# 2. Plot the rotated airfoil
a[1,1].plot(x_values3, y_values3, '--', markersize=3, c='black', label="Mean Camber Line")
a[1,1].set_title("NACA 9412", fontsize=20, color='red')
a[1,1].set_xlabel("X_Axis", fontsize=10)
a[1,1].set_ylabel("y_Axis", fontsize=10)
a[1,1].tick_params(axis="both", which="major", size=10, labelsize=15)
a[1,1].set(xlim=(-0.1, 1.5), xticks=np.arange(0.5, 1.6, 0.5))
a[1,1].set(ylim=(-0.4, 0.5), yticks=np.arange(-0.2, 1, 0.2))

# 3. Add lines and legends
a[1,1].plot(chord_x3, chord_y3, 'r--', label="Chord Line")
a[1,1].plot(xu3_, yu3_, 'g', label="Upper Surface")
a[1,1].plot(xl3_, yl3_, 'b', label="Lower Surface")
a[1,1].legend(fontsize=10)
a[1,1].text(1.1, 0.5, "AOA = 15°", c='blue', fontsize=20)

plt.show()