# Now try to catch boundaries correctly at Region of Validity
#   In order to make this file readable...
# import sys; sys.path[len(sys.path):]=['C:\\Users\\jcl3\\Documents\\PhysicsEducationResearch\\Calorimeter\\Python_HandOff']
import Trial9; import Trial11; import importlib
#
# This is the iteration testing!!!
# import importlib
# importlib.reload( Iter01 )
#
import Trial9
import Trial11
print("Welcome! You are testing the calorimeter problem.")
print("For now, you can only use water as the material.")
ConstantsWater=[273, 373, 2100, 334000, 4190, 2256000, 1996]
Constants1 = ConstantsWater
Constants2 = ConstantsWater
print("ConstantsWater = ", ConstantsWater)
#
#print()
State1 = [4,373,273,100,100,1,0]
State2 = [2,272,273,99,0,0,0]
Mass1 = 1
Mass2 = 1
print( State1, "   ", State2)
if Trial9.TotalHeat(State1,Mass1,Constants1) < Trial9.TotalHeat(State2,Mass2,Constants2)  :
	print( "Invalid start!  State 1 colder than State 2" )
Difference = Trial9.TotalHeat(State1,1,Constants1) - Trial9.TotalHeat(State2,1,Constants2)
print( "Difference in Heat = ", Difference)
NumberIterations = 20
Delta = Difference/NumberIterations
TrialDelta1 = Delta
TrialDelta2 = Delta
print( "Delta Heat = ", Delta)
Proceed = True
HitROV1 = False
HitROV2 = False

while Proceed :

	if HitROV1 :
		print( "Handle HitROV1.") #  descending!!!
		print( "Starting state is ", State1, "  Delta heat to ROV is ", NewDelta)
		if State1[0]==1 :
			print( "You get Nobel Prize because you hit zero Kelvin!")
			break
		elif State1[0]==2 :
			State1[0]=1
			State1[1]=Constants1[0]
			State1[2]=Constants1[0]
			State1[3]=0
			State1[4]=0
			State1[5]=0
			State1[6]=0
			HitROV1 = False  #  Clear the HitROV code!
			print( "Output state = ", State1)
			ReturnCode2 = Trial11.MoveHeat(State2,Mass2,Constants2,NewDelta)
			if ReturnCode2 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		elif State1[0]==3 :
			State1[0]=2
			State1[1]=Constants1[0]
			State1[2]=Constants1[0]
			State1[3]=100
			State1[4]=0
			State1[5]=0
			State1[6]=0
			HitROV1 = False  #  Clear the HitROV code!
			print( "Output state = ", State1)
			ReturnCode2 = Trial11.MoveHeat(State2,Mass2,Constants2,NewDelta)
			if ReturnCode2 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		elif State1[0]==4 :
			State1[0]=3
			State1[1]=Constants1[1]
			State1[2]=Constants1[0]
			State1[3]=100
			State1[4]=Constants1[1]-Constants1[0]
			State1[5]=0
			State1[6]=0
			HitROV1 = False  #  Clear the HitROV code!
			print( "Output state = ", State1)
			ReturnCode2 = Trial11.MoveHeat(State2,Mass2,Constants2,NewDelta)
			if ReturnCode2 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		elif State1[0]==5 :
			State1[0]=4
			State1[1]=Constants1[1]
			State1[2]=Constants1[0]
			State1[3]=100
			State1[4]=Constants1[1]-Constants1[0]
			State1[5]=100
			State1[6]=0
			HitROV1 = False  #  Clear the HitROV code!
			print( "Output state = ", State1)
			ReturnCode2 = Trial11.MoveHeat(State2,Mass2,Constants2,NewDelta)
			if ReturnCode2 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		else :
			print ("Couldn't handle ROV for State 1")
			break

#============================================

	if HitROV2 :
		print( "Handle HitROV2.") #  ascending!!!
		print( "Starting state is ", State2, "  Delta heat to ROV is ", NewDelta)
		if State2[0]==1 :
			State2[0]=2
			State2[1]=Constants2[0]
			State2[2]=Constants2[0]
			State2[3]=0
			State2[4]=0
			State2[5]=0
			State2[6]=0
			HitROV2 = False  #  Clear the HitROV code!
			print( "Output state = ", State2)
			ReturnCode1 = Trial11.MoveHeat(State1,Mass1,Constants1, -NewDelta)
			if ReturnCode1 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		elif State2[0]==2 :
			State2[0]=3
			State2[1]=Constants2[0]
			State2[2]=Constants2[0]
			State2[3]=100
			State2[4]=0
			State2[5]=0
			State2[6]=0
			HitROV2 = False  #  Clear the HitROV code!
			print( "Output state = ", State2)
			ReturnCode1 = Trial11.MoveHeat(State1,Mass1,Constants1, -NewDelta)
			if ReturnCode1 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode1)
				break
			print( State1, "   ", State2)
			continue
		elif State2[0]==3 :
			State2[0]=4
			State2[1]=Constants2[0]
			State2[2]=Constants2[0]
			State2[3]=100
			State2[4]=Constants2[1]-Constants2[0]
			State2[5]=0
			State2[6]=0
			HitROV2 = False  #  Clear the HitROV code!
			print( "Output state = ", State2)
			ReturnCode1 = Trial11.MoveHeat(State1,Mass1,Constants1, -NewDelta)
			if ReturnCode1 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		elif State2[0]==4 :
			State2[0]=5
			State2[1]=Constants2[0]
			State2[2]=Constants2[0]
			State2[3]=100
			State2[4]=Constants2[1]-Constants2[0]
			State2[5]=100
			State2[6]=0
			HitROV2 = False  #  Clear the HitROV code!
			print( "Output state = ", State2)
			ReturnCode1 = Trial11.MoveHeat(State1,Mass1,Constants1, -NewDelta)
			if ReturnCode1 == -1 :
				print( "Hit issue! MoveHeat return code = ", ReturnCode)
				break
			print( State1, "   ", State2)
			continue
		elif State2[0]==5 :
			print( "You get Nobel Prize because you hit infinite Kelvin!")
			break
		else :
			print ("Couldn't handle ROV for State 2")
			break



	TrialState1 = State1
	print( "TrialDelta1 = ", TrialDelta1, "   Now setting it to Delta = ", Delta)
	TrialDelta1 = Delta
	ReturnCode1 = Trial11.MoveHeat(TrialState1,Mass1,ConstantsWater,-TrialDelta1)
	print( "MoveHeat for State 1 returned ReturnCode1 = ", ReturnCode1)
	if ReturnCode1 == -1 :
		print( "Hit bad issue! MoveHeat return code = ", ReturnCode1)
		break
	if ReturnCode1 > 0 :
		NewDelta = ReturnCode1
		print( "Hit region of validity for State 1! MoveHeat return code = NewDelta = ", NewDelta)
		HitROV1 = True
#1		continue


	TrialState2 = State2
	TrialDelta2 = Delta
	ReturnCode2 = Trial11.MoveHeat(TrialState2,Mass2,ConstantsWater,TrialDelta2)
	print( "MoveHeat for State 2 returned ReturnCode2 = ", ReturnCode2)
	if ReturnCode2 == -1 :
		print( "Hit bad issue! MoveHeat return code = ", ReturnCode2)
		break
	if ReturnCode2 > 0 :
		NewDelta = ReturnCode2
		print( "Hit region of validity for State 2! MoveHeat return code = NewDelta = ", NewDelta)
		HitROV2 = True
#1		continue

	if (ReturnCode1 > 0) or (ReturnCode2 > 0) :
		NewDelta = min(TrialDelta1, TrialDelta2)
		print( "Try again with smaller of ", TrialDelta1, TrialDelta2, "   which is ", NewDelta)
		continue


	if TrialState1[1] == TrialState2[1]  : # Equal temperatures
		print( "SUCCESS" )
		State1 = TrialState1
		State2 = TrialState2
		print( State1, "   ", State2)
		break
	if Trial9.TotalHeat(TrialState1,1,Constants1) == Trial9.TotalHeat(TrialState2,1,Constants1)  : # Note mass =1 to compare state only!
		print( "SUCCESS" )
		State1 = TrialState1
		State2 = TrialState2
		print( State1, "   ", State2)
		break
	if TrialState1[1] < TrialState2[1]  : # Overshot
		print( State1, "   ", State2)
		print( "Reverse last iteration.")
		Trial11.MoveHeat(TrialState1,Mass1,Constants1, +Delta)
		Trial11.MoveHeat(TrialState2,Mass2,Constants2, -Delta)
		print( State1, "   ", State2)
		Delta = Delta / 10
		print( "New smaller Delta is ", Delta)
		if Delta < 1 :
			break
	if Trial9.TotalHeat(TrialState1,1,ConstantsWater) < Trial9.TotalHeat(TrialState2,1,ConstantsWater)  : # Note mass =1 to compare state only!
		print( State1, "   ", State2)
		print( "Reverse last iteration.")
		Trial11.MoveHeat(TrialState1,Mass1,Constants1, +Delta)
		Trial11.MoveHeat(TrialState2,Mass2,Constants2, -Delta)
		print( State1, "   ", State2)
		Delta = Delta / 10
		print( "New smaller Delta is ", Delta)
		if Delta < 1 :
			break
	# else the iteration process looks complete!
	State1 = TrialState1
	State2 = TrialState2
	print( State1, "   ", State2)

print( "OK! We finished the loop!" )
print( State1, "   ", State2)




