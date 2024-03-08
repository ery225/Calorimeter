# This starts to develop the scaling for the display window.
#   In order to make this file readable...
# import sys; sys.path[len(sys.path):]=['C:\\Users\\jcl3\\Documents\\PhysicsEducationResearch\\Calorimeter\\Python2']
import graphics
import math
import time
ConstantsWater=[273, 373, 2100, 334000, 4190, 2256000, 1996]
Constants1 = ConstantsWater
Constants2 = ConstantsWater
Thot=383   #  TEMPORARY OVERRIDE
Tcold=263  #  TEMPORARY OVERRIDE
Tspan=Thot-Tcold  
#  Tspan = 100  TEMPORARY OVERRIDE
print("Constants1 =", Constants1)
print("Constants2 =", Constants2)
NeedZones1 = [1,1,1,1,1]
NeedZones2 = [1,1,1,1,1]
Mass1=1
Mass2=4
TrialD1 = [0,0,0,0,0]
TrialD2 = [0,0,0,0,0]

TrialD1[0]=math.sqrt((4/(3.14159*100))*Mass1*Constants1[2]*Tspan)
TrialD1[1]=math.sqrt((4/(3.14159*100))*Mass1*Constants1[3])
TrialD1[2]=math.sqrt((4/(3.14159*100))*Mass1*Constants1[4]*Tspan)
TrialD1[3]=math.sqrt((4/(3.14159*100))*Mass1*Constants1[5])
TrialD1[4]=math.sqrt((4/(3.14159*100))*Mass1*Constants1[6]*Tspan)
print("TrialD1 =", TrialD1)
TrialD2[0]=math.sqrt((4/(3.14159*100))*Mass2*Constants2[2]*Tspan)
TrialD2[1]=math.sqrt((4/(3.14159*100))*Mass2*Constants2[3])
TrialD2[2]=math.sqrt((4/(3.14159*100))*Mass2*Constants2[4]*Tspan)
TrialD2[3]=math.sqrt((4/(3.14159*100))*Mass2*Constants2[5])
TrialD2[4]=math.sqrt((4/(3.14159*100))*Mass2*Constants2[6]*Tspan)
print("TrialD2 =", TrialD2)
Tmelt1=Constants1[0]
Tboil1=Constants1[1]
HeightLiquid1 = Tboil1-Tmelt1
Tmelt2=Constants2[0]
Tboil2=Constants2[1]
HeightLiquid2 = Tboil2-Tmelt2

# Calculate trial width
PrelimWidthHot = 15
PrelimWidthHot +=max(NeedZones1[0]*TrialD1[0],NeedZones1[2]*TrialD1[2],NeedZones1[4]*TrialD1[4])
if (NeedZones1[1] != 0 or NeedZones1[3] != 0) :
    PrelimWidthHot +=100
PrelimWidthCold = 15
PrelimWidthCold +=max(NeedZones2[0]*TrialD2[0],NeedZones2[2]*TrialD2[2],NeedZones2[4]*TrialD2[4])
if (NeedZones2[1] != 0 or NeedZones2[3] != 0) :
    PrelimWidthCold +=100

# Calculate trial height
PrelimHeigthHot = 15
#print("Preliminary heigth hot = ", PrelimHeigthHot)
PrelimHeigthHot +=max(NeedZones1[0]*100*min(Tmelt1-Thot,Thot-Tcold)/Tspan,0.5*NeedZones1[1]*TrialD1[1])
#print("Preliminary heigth hot = ", PrelimHeigthHot)
PrelimHeigthHot +=max(NeedZones1[2]*100*min(Thot-Tmelt1,Thot-Tcold,Tboil1-Thot)/Tspan,0.5*NeedZones1[1]*TrialD1[1]+0.5*NeedZones1[3]*TrialD1[3])
#print("Preliminary heigth hot = ", PrelimHeigthHot)
PrelimHeigthHot +=max(NeedZones1[4]*100*min(Thot-Tboil1,Thot-Tcold)/Tspan,0.5*NeedZones1[3]*TrialD1[3])
#print("Preliminary heigth hot = ", PrelimHeigthHot)
PrelimHeigthCold = 15
#print("Preliminary heigth cold = ", PrelimHeigthCold)
PrelimHeigthCold +=max(NeedZones2[0]*100*min(Tmelt2-Tcold,Thot-Tcold)/Tspan,0.5*NeedZones2[1]*TrialD2[1])
#print("Preliminary heigth cold = ", PrelimHeigthCold)
PrelimHeigthCold +=max(NeedZones2[2]*100*min(Tcold-Tmelt2,Thot-Tcold,Tboil2-Tcold)/Tspan,0.5*NeedZones2[1]*TrialD2[1]+0.5*NeedZones2[3]*TrialD2[3])
#print("Preliminary heigth cold = ", PrelimHeigthCold)
PrelimHeigthCold +=max(NeedZones2[4]*100*min(Tcold-Tboil2,Thot-Tcold)/Tspan,0.5*NeedZones2[3]*TrialD2[3])
#print("Preliminary heigth cold = ", PrelimHeigthCold)
print("Preliminary width hot = ", PrelimWidthHot, "  cold = ", PrelimWidthCold )
print("Preliminary heigth hot = ", PrelimHeigthHot, "  cold = ", PrelimHeigthCold )
print("Use larger of preliminary heights = ",max(PrelimHeigthHot,PrelimHeigthCold),"   to determine scaling!!!")
PrelimHeight = max(PrelimHeigthHot,PrelimHeigthCold)
win=graphics.GraphWin("Calorimeter",1300,600)
Axis1 = int(PrelimWidthHot/2)
Ycold = int((-400/Tspan)*(Tcold-Tcold)+550)
Ymelt = int((-400/Tspan)*(Tmelt1-Tcold)+550)
Yboil = int((-400/Tspan)*(Tboil1-Tcold)+550)
Yhot = int((-400/Tspan)*(Thot-Tcold)+550)
corner1 = graphics.Point(10+Axis1-0.5*TrialD1[0],Ymelt)
corner2 = graphics.Point(10+Axis1+0.5*TrialD1[0],600)
r0 = graphics.Rectangle(corner1,corner2)
r0.draw(win)
corner1 = graphics.Point(10+Axis1-0.5*TrialD1[2],Ymelt)
corner2 = graphics.Point(10+Axis1+0.5*TrialD1[2],Yboil)
r2 = graphics.Rectangle(corner1,corner2)
r2.draw(win)
corner1 = graphics.Point(10+Axis1-0.5*TrialD1[4],Yboil)
corner2 = graphics.Point(10+Axis1+0.5*TrialD1[4],0)
r4 = graphics.Rectangle(corner1,corner2)
r4.draw(win)
corner1 = graphics.Point(10+Axis1+0.5*max(TrialD1[0],TrialD1[2]),Ymelt-0.5*TrialD1[1])
corner2 = graphics.Point(10+Axis1+0.5*max(TrialD1[0],TrialD1[2])+4*100,Ymelt+0.5*TrialD1[1])
print(corner1,corner2)
r1 = graphics.Rectangle(corner1,corner2)
r1.draw(win)
corner1 = graphics.Point(10+Axis1+0.5*max(TrialD1[2],TrialD1[4]),Yboil-0.5*TrialD1[3])
corner2 = graphics.Point(10+Axis1+0.5*max(TrialD1[2],TrialD1[4])+4*100,Yboil+0.5*TrialD1[3])
print(corner1,corner2)
r3 = graphics.Rectangle(corner1,corner2)
r3.draw(win)
#  End of hot framework

#  Beginning of cold framework
Axis2 = int(600+PrelimWidthCold/2)
Ycold = int((-400/Tspan)*(Tcold-Tcold)+550)
Ymelt = int((-400/Tspan)*(Tmelt1-Tcold)+550)
Yboil = int((-400/Tspan)*(Tboil1-Tcold)+550)
Yhot = int((-400/Tspan)*(Thot-Tcold)+550)
corner1 = graphics.Point(10+Axis2-0.5*TrialD2[0],Ymelt)
corner2 = graphics.Point(10+Axis2+0.5*TrialD2[0],600)
rc0 = graphics.Rectangle(corner1,corner2)
rc0.draw(win)
corner1 = graphics.Point(10+Axis2-0.5*TrialD2[2],Ymelt)
corner2 = graphics.Point(10+Axis2+0.5*TrialD2[2],Yboil)
rc2 = graphics.Rectangle(corner1,corner2)
rc2.draw(win)
corner1 = graphics.Point(10+Axis2-0.5*TrialD2[4],Yboil)
corner2 = graphics.Point(10+Axis2+0.5*TrialD2[4],0)
rc4 = graphics.Rectangle(corner1,corner2)
rc4.draw(win)
corner1 = graphics.Point(10+Axis2+0.5*max(TrialD2[0],TrialD2[2]),Ymelt-0.5*TrialD2[1])
corner2 = graphics.Point(10+Axis2+0.5*max(TrialD2[0],TrialD2[2])+4*100,Ymelt+0.5*TrialD2[1])
print(corner1,corner2)
rc1 = graphics.Rectangle(corner1,corner2)
rc1.draw(win)
corner1 = graphics.Point(10+Axis2+0.5*max(TrialD2[2],TrialD2[4]),Yboil-0.5*TrialD2[3])
corner2 = graphics.Point(10+Axis2+0.5*max(TrialD2[2],TrialD2[4])+4*100,Yboil+0.5*TrialD2[3])
print(corner1,corner2)
rc3 = graphics.Rectangle(corner1,corner2)
rc3.draw(win)
#  End of cold framework

#print("About to enter first fill loop.")
Tloop=Tcold
dTloop=(Tmelt1-Tcold)/50
while Tloop<=Tmelt1 :
#	print("Iteration")
	Ylevel = int((-400/Tspan)*(Tloop-Tcold)+550)
	corner1 = graphics.Point(10+Axis1-0.5*TrialD1[0],Ylevel)
	corner2 = graphics.Point(10+Axis1+0.5*TrialD1[0],600)
	r0fill = graphics.Rectangle(corner1,corner2)
	r0fill.setFill("red")
	r0fill.draw(win)
	time.sleep(0.1)
	Tloop += dTloop
print("Starting melting")
Ploop=0
dPloop=1
while Ploop<=100 :
#	print("Iteration")
	Ylevel = int((-400/Tspan)*(Tloop-Tcold)+550)
	corner1 = graphics.Point(10+Axis1+0.5*max(TrialD1[0],TrialD1[2]),Ymelt-0.5*TrialD1[1])
	corner2 = graphics.Point(10+Axis1+0.5*max(TrialD1[0],TrialD1[2])+4*Ploop,Ymelt+0.5*TrialD1[1])
	r0fill = graphics.Rectangle(corner1,corner2)
	r0fill.setFill("red")
	r0fill.draw(win)
	time.sleep(0.1)
	Ploop += dPloop
print("Starting to warm up liquid.")
Tloop=Tmelt1
dTloop=(Tboil1-Tmelt1)/100
while Tloop<=Tboil1 :
#	print("Iteration")
	Ylevel = int((-400/Tspan)*(Tloop-Tcold)+550)
	corner1 = graphics.Point(10+Axis1-0.5*TrialD1[2],Ylevel)
	corner2 = graphics.Point(10+Axis1+0.5*TrialD1[2],Ymelt)
	r0fill = graphics.Rectangle(corner1,corner2)
	r0fill.setFill("red")
	r0fill.draw(win)
	time.sleep(0.1)
	Tloop += dTloop
print("Starting boiling")
Ploop=0
dPloop=1
while Ploop<=100 :
#	print("Iteration")
	Ylevel = int((-400/Tspan)*(Tloop-Tcold)+550)
	corner1 = graphics.Point(10+Axis1+0.5*max(TrialD1[2],TrialD1[4]),Yboil-0.5*TrialD1[3])
	corner2 = graphics.Point(10+Axis1+0.5*max(TrialD1[2],TrialD1[4])+4*Ploop,Yboil+0.5*TrialD1[3])
	r0fill = graphics.Rectangle(corner1,corner2)
	r0fill.setFill("red")
	r0fill.draw(win)
	time.sleep(0.1)
	Ploop += dPloop
print("Starting to warm up vapor.")
Tloop=Tboil1
dTloop=(Thot-Tmelt1)/50
while Tloop<=Thot :
#	print("Iteration")
	Ylevel = int((-400/Tspan)*(Tloop-Tcold)+550)
	corner1 = graphics.Point(10+Axis1-0.5*TrialD1[4],Ylevel)
	corner2 = graphics.Point(10+Axis1+0.5*TrialD1[4],Yboil)
	r0fill = graphics.Rectangle(corner1,corner2)
	r0fill.setFill("red")
	r0fill.draw(win)
	time.sleep(0.1)
	Tloop += dTloop
print("Done")