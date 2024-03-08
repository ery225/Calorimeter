#   In order to make this file readable...
# import sys; sys.path[len(sys.path):]=['C:\\Users\\jcl3\\Documents\\PhysicsEducationResearch\\Calorimeter\\Python']
# Change definition of state to [case,T,Tsolid_up_to_melt,%melt,Tliq_above_melt,%boil,Tvap_above_boil] (seven elements)
# try to modularize
#
# Redefine State array:
#State [0] {1=solid, 2=melting, 3=liquid, 4=boiling, 5=vapor}
#State [1] temperature
#State [2] temp of ice (up to max value of Tmelt)
#State [3] percentage of liquid
#State [4] temp of water (up to max value of Tvap)
#State [5] percentage of vapor
#State [6] temp of vapor (no limit)
State1=[3,373,273,100,100,0,0] # liquid at 100C
StateLiq50=[3,323,273,100,50,0,0] # input liquid at 50C
State2=[3,273,273,100,0,0,0] # liquid at 0C
StateSolid=[1,200,200,0,0,0,0] # solid at 200K
StateSolidBad=[1,300,300,0,0,0,0]
StateBoiling=[4,0,0,0,0,50,0]
StateVapor=[5,0,0,0,0,0,55]
Constants1=[273, 373, 2100, 334000, 4190, 225600, 1996]
Constants2=[273, 373, 2100, 334000, 4190, 225600, 1996]
ConstantsCopper=[1358,2835,385,9999,9999,9999,9999]
Mass1=4 # kg
Mass2=2 # kg
# Trial4.IsStateValid(StateSolidBad, Constants1)
def try1(name):
	print("Hello, " + name)

def IsStateValid(state,constants) :
#	print( "Input state = ", state)
	if state[0]==1 :
		Temp = state[2]
		Tmelt = constants[0]
#		print("Case= ", state[0],"Temp= ", Temp, "  Tmelt= ", Tmelt)
		if Temp <= Tmelt :
			state[3]=0
			state[4]=0
			state[5]=0
			state[6]=0
#			print( "Output state = ", state)
			state[1]=Temp
			return Temp
		else :
			return "For case= " + str(state[0]) + ",  Invalid Temp"
	elif state[0]==2 :
		Percent = state[3]
		Tmelt = constants[0]
#		print("Case= ", state[0],"  Tmelt= ", Tmelt, " Percent melt= ", Percent)
		if (Percent >= 0 ) and (Percent <= 100) :
			state[1]=Tmelt
			state[2]=Tmelt
			state[4]=0
			state[5]=0
			state[6]=0
#			print( "Output state = ", state)
			Temp=Tmelt
			state[1]=Temp
			return Temp
		else :
			return "For case= " + str(state[0]) + ",  Invalid Percent"
	elif state[0]==3 :
		Tmelt = constants[0]
		Tboil = constants[1]
		Temp = Tmelt+state[4]
#		print("Case= ", state[0],"Temp= ", Temp, "  Tmelt= ", Tmelt, " Tboil= ", Tboil)
		if (Temp >= Tmelt) and  (Temp <= Tboil) :
			state[2]=Tmelt
			state[3]=100
			state[5]=0
			state[6]=0
#			print( "Output state = ", state)
			state[1]=Temp
			return Temp
		else :
			return "For case= " + str(state[0]) + ",  Invalid Temp"
	elif state[0]==4 :
		Percent = state[5]
		Tmelt = constants[0]
		Tboil = constants[1]
#		print("Case= ", state[0],   " Percent boiled= ", Percent)
		if (Percent >= 0 ) and (Percent <= 100) :
			state[2]=Tmelt
			state[3]=100
			state[4]=Tboil-Tmelt
			state[6]=0
#			print( "Output state = ", state)
			Temp=Tboil
			state[1]=Temp
			return Temp
		else :
			return "For case= " + str(state[0]) + ",  Invalid Percent"
	elif state[0]==5 :
		Tmelt = constants[0]
		Tboil = constants[1]
		Temp = Tboil+state[6]
#		print("Case= ", state[0],"Temp= ", Temp, "  Tmelt= ", Tmelt, " Tboil= ", Tboil)
		if (Temp >= Tboil) :
			state[2]=Tmelt
			state[3]=100
			state[4]=Tboil-Tmelt
			state[5]=100
#			print( "Output state = ", state)
			state[1]=Temp
			return Temp
		else :
			return "For case= " + str(state[0]) + ",  Invalid Temp"
#============================================
def TotalHeat(state,mass,constants) :
	HeatTerms = [0,0,0,0,0]
#	print( "Total Heat:  Input state  = ", state, "  mass = ", mass)
#	print( "  constants = ", constants)
	HeatTerms[0] = mass*state[2]*constants[2]
	HeatTerms[1] = mass*0.01*state[3]*constants[3]
	HeatTerms[2] = mass*state[4]*constants[4]
	HeatTerms[3] = mass*0.01*state[5]*constants[5]
	HeatTerms[4] = mass*state[6]*constants[6]
	TotalHeat = HeatTerms[0] + HeatTerms[1] + HeatTerms[2] + HeatTerms[3] +HeatTerms[4]
#	print("TotalHeat = ", TotalHeat, "  terms are ", HeatTerms)
	return TotalHeat
#============================================
def CreateNewState(NewTemp,NewState,constants) :  # based on temperature
#	print( "NewTemp = ", NewTemp,  "NewState = ", NewState)
	Tmelt = constants[0]
	Tboil = constants[1]
	if NewTemp < Tmelt :
		NewState[0]=1
		NewState[2]=NewTemp
	elif NewTemp == Tmelt :
		NewState[0]=2
		NewState[3]=0 # assume zero percent
	elif (NewTemp > Tmelt) and  (NewTemp < Tboil) :
		NewState[0]=3
		NewState[4]=NewTemp-Tmelt
	elif NewTemp == Tboil :
		NewState[0]=4
		NewState[5]=0 # assume zero percent
	elif NewTemp > Tboil :
		NewState[0]=5
		NewState[6]=NewTemp-Tboil
	else :
		return "Not handled"
	IsStateValid(NewState,constants)  # create the rest of the NewState array
#	print ("NewState updated = ", NewState)
	return NewState

#============================================
	

#   In order to make this file readable...
# import sys
# sys.path[len(sys.path):]=['C:\\Users\\jcl3\\Documents\\PhysicsEducationResearch\\Calorimeter\\Python']
# import Trial2
#
# Create array to describe state of each material
Mass1=4 # kg
Mass2=2 # kg
#
#MaxDelta1 = TotalHeat1-TotalHeat1as2
#
#Needed to warm Material2 up to initial temp of Material1
#
#MaxDelta2 = TotalHeat2-TotalHeat2as1
#print(MaxDelta2)
#Tmax=100
#Tmin=20
#Nsteps=20
#C1=4 # Specific heat of material 1
#C2=2 # Specific heat of material 2
#T1=Tmax
#T2=Tmin
#Q1max=C1*(Tmax-Tmin)
#Q2max=C2*(Tmax-Tmin)
#deltaQ=min(Q1max,Q2max)/Nsteps
#print(Q1max,Q2max,Nsteps)
#while T1>=T2:
#	print(T1,T2)
#	T1=T1-deltaQ/C1
#	T2=T2+deltaQ/C2
#else:
#	T1=T1+deltaQ/C1
#	T2=T2-deltaQ/C2
#	print('final iteration')
#	print(T1,T2)
#	T1=T2=(T1*C1+T2*C2)/(C1+C2)
#	print(T1,T2)
#	print("end")