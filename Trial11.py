import Trial9
def State1Hotter(StateA,ConstantsA,StateB,ConstantsB) :
	print( "Hi there!")
	print( "State 1 = ", StateA, "   Constants1 = ", ConstantsA )
	print( "State 2 = ", StateB, "   Constants2 = ", ConstantsB )
	print( "Difference in Heat = ", Trial9.TotalHeat(StateA,1,ConstantsA) - Trial9.TotalHeat(StateB,1,ConstantsB) )
	if Trial9.TotalHeat(StateA,1,ConstantsA) >= Trial9.TotalHeat(StateB,1,ConstantsB)  :
		print( "State 1 is hotter." )
	else :
		print( "State 2 is hotter." )

#================================
def MoveHeat(State,Mass,Constants,Delta) :
#  LOGIC:
#  Check if Delta would exceed region of validity.
#     If so, return region of validity as new Delta
#     If not, do the heat move (could be positive or negative) and return modified state
#
	print( "Input state = ", State )
	OldTemp = State[1]
	Tmelt = Constants[0]
	Tboil = Constants[1]
# Calculate break points
	THBreak12 = Trial9.TotalHeat([1,Tmelt,Tmelt,0,0,0,0],Mass,Constants)
	THBreak23 = Trial9.TotalHeat([2,Tmelt,Tmelt,100,0,0,0],Mass,Constants)
	THBreak34 = Trial9.TotalHeat([3,Tboil,Tmelt,100,(Tboil-Tmelt),0,0],Mass,Constants)
	THBreak45 = Trial9.TotalHeat([4,Tboil,Tmelt,100,(Tboil-Tmelt),100,0],Mass,Constants)
	print( "Input temperature = ", OldTemp )
#	print( "THBreak12 = ", THBreak12)
#	print( "THBreak23 = ", THBreak23)
#	print( "THBreak34 = ", THBreak34)
#	print( "THBreak45 = ", THBreak45)
#	print( "Did reload.")
#	return 1
	if Delta == 0 :
		return -1
	if State[0]==1 :
		if Delta < 0 :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants)) : # would be below 0 Kelvin
				return -1
			NewTemp = OldTemp + Delta / (Mass*Constants[2])
			print( "New temperature = ", NewTemp )
			State[1] = NewTemp
			State[2] = NewTemp
			print( "New State = ", State )
			return 0
		else :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak12 ) : # would be above Tmelt
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak12 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			NewTemp = OldTemp + Delta / (Mass*Constants[2])
			print( "New temperature = ", NewTemp )
			State[1] = NewTemp
			State[2] = NewTemp
			print( "New State = ", State )
			return 0
	elif State[0]==2 :
		if Delta < 0 :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak12 ) : # would be below 0% melted
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak12 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			OldPercent = State[3]
			NewPercent = OldPercent + 100*Delta / (Mass*Constants[3])
			print( "Old percent = ", OldPercent, "   New percent = ", NewPercent )
			State[3] = NewPercent
			print( "New State = ", State )
			return 0
		else :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak23 ) : # would be more than 100% melted
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak23 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			OldPercent = State[3]
			NewPercent = OldPercent + 100*Delta / (Mass*Constants[3])
			print( "Old percent = ", OldPercent, "   New percent = ", NewPercent )
			State[3] = NewPercent
			print( "New State = ", State )
			return 0
	elif State[0]==3 :
		if Delta < 0 :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak23 ) : # would be below Tmelt
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak23 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			NewTemp = OldTemp + Delta / (Mass*Constants[4])
			print( "New temperature = ", NewTemp )
			State[1] = NewTemp
			State[4] = NewTemp-Tmelt
			print( "New State = ", State )
			return 0
		else :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak34 ) : # would be above Tmelt
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak34 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			NewTemp = OldTemp + Delta / (Mass*Constants[4])
			print( "New temperature = ", NewTemp )
			State[1] = NewTemp
			State[4] = NewTemp-Tmelt
			print( "New State = ", State )
			return 0
	elif State[0]==4 :
		if Delta < 0 :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak34 ) : # would be below 0% boiled
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak34 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			OldPercent = State[5]
			NewPercent = OldPercent + 100*Delta / (Mass*Constants[5])
			print( "Old percent = ", OldPercent, "   New percent = ", NewPercent )
			State[5] = NewPercent
			print( "New State = ", State )
			return 0
		else :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak45 ) : # would be more than 100% boiled
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak45 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			OldPercent = State[5]
			NewPercent = OldPercent + 100*Delta / (Mass*Constants[5])
			print( "Old percent = ", OldPercent, "   New percent = ", NewPercent )
			State[5] = NewPercent
			print( "New State = ", State )
			return 0
	elif State[0]==5 :
		if Delta < 0 :
			if abs(Delta) > abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak45 ) : # would be below Tboil
				NewDelta = abs(Trial9.TotalHeat(State,Mass,Constants) - THBreak45 )
				Delta = NewDelta
				print( "Go back and try again with new Delta = ", NewDelta)
				return NewDelta # Go back and try again with NewDelta = ROV
			NewTemp = OldTemp + Delta / (Mass*Constants[6])
			print( "New temperature = ", NewTemp )
			State[1] = NewTemp
			State[6] = NewTemp-Tboil
			print( "New State = ", State )
			return 0
		else :
			NewTemp = OldTemp + Delta / (Mass*Constants[6])
			print( "New temperature = ", NewTemp )
			State[1] = NewTemp
			State[6] = NewTemp-Tboil
			print( "New State = ", State )
			return 0
	else :
		print( "Invalid state code = ", State[0] )
		return -1