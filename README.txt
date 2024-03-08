DIRECTORY
This directory contains Python code to hand off to student programmers.
This code has been tested in the Python 3.11 platform running on 64-bit Microsoft Windows 10 Enterprise on a Dell machine with an Intel processor.



MODULE: Trial32.py (requires graphics.py)
The code Trial32.py requires the library graphics.py to be available in the same directory, but then is executable by simply double-clicking on the Trial32.py file.  The action of the Trial32.py module is to:
1) Dynamically generate the skeleton/framework/outline structure of the cylindrical "tanks" based on...
a) the specific heats and latent heats of the substances involved (note that both materials are water in this implementation)
AND 
b) the quantities of each material (note that the quantities are currently hard-coded as 1kg for the cold water and 4kg for the hot water, so the hot tanks have twice the diameter of the corresponding cold tanks)
AND 
the temperature span required (so not include unneeded tanks) 
...in order that they fit aesthetically within the graphcs output window.
2) Fill the tank structures up to the required level of temperature (vertical) or percent completion of a phase transition (horizontal).  At this point, we only show heat being added to the cold substance rather than also heat being removed from the hot substance, and only over a demonstration loop rather than an actual thermal equilibration.  

TASKS:
1) Enhance graphics to give tanks and level a 3-D appearance?
2) Add a thin horizontal pipe to connect the latent heat tanks to the specific heat tanks to convey that the connection is only at exactly the transition temperature.
3) Add code to show the fill level of the hot material as that decreases.
4) Fill tanks based on values from the iterative calculations (rather than just a simple loop as executed so far).
5) Interactive user input needs to be added, etither on this screen or elsewhere.



MODULE: Iter40.py (requires Trial9.py and Trial11.py)
The code Iter40.py requires Trial9.py and Trial11.py to be available in the same directory.  The action of the Iter40.py module is to:
1) Supply the initial conditions. At the moment this is hard-coded, but it should be part of a sequence to accept user input.
2) Use calls to Trial9.TotalHeat(State1,1,Constants1) and Trial9.TotalHeat(State2,1,Constants2) to determine a not-physically-valid calculation of the total heat needed to raise that sample from zero Kelvin to those current states.  The difference between these quantities is used to ESTIMATE the total amount of heat that may have to be transferred during equilibration, so it can be broken into suitable increments.  The number of increments shoud be small enoiugh so that the iteration completes in a reasonable time but large enough so that the user sees a gradual approach to equilibrium. 
3) The "ROV" flags stand for "Region Of Validity" which is the cutoff for when a particular equation is valid.  For example, the specific heat equation for liquid water is valid for raising the temperature from 85 to 95 Celsius, but is NOT valid for raising the temperature from 95 to 105 Celsius.  In the latter case, the amount of heat to transfer is temporarily reduced to just the valid amount and then the next increment would be used to vaporize some of the liquid.
4) Repeatedly call Trial11.MoveHeat() (limited by ROV) to add or remove heat to a material and determine the new state.
5) As the system gets closer to equilibrium the amount of heat that gets transfered in an increment gets smaller so that it approaches gradually rather than overshoots.

TASKS:
1) Create user input module so that user can input states of choice.
2) Add capability for a third material (for example a copper calorimeter can). This should probably then be integrated into a total effective heat capacity data structure for the starting material.
3) Make provision for making the ROV calculations accessible for a new module that would convey the pedagogy -- perhaps displaying the ROVs for the processes that are currently in play and highlighting the smallest of these.
4) Feed the actual incrementing state descriptions to the graphics module for display.
5) Set up program so it resets all necessary variables and returns to wait for user input, rather than requiring having to exit and restart Python.
6) Set up a clean exit path so the user can end the program.



DATA STRUCTURE: THERMODYNAMIC CONSTANTS
ConstantsWater contains the materials constants as these seven values
[273, 373, 2100, 334000, 4190, 2256000, 1996]
273 = solid-liquid transition temperature in Kelvin
373 = liquid-vapor transition temperature in Kelvin
2100 = specific heat of solid water (ice) in J / (kg K)
334000 = latent heat for solid-liquid transition in J / kg
4190 = specific heat of liquid water in J / (kg K)
2256000 = latent heat for liquid-vapor transition in J / kg
1996 = specific heat of vapor water (steam) in J / (kg K)



DATA STRUCTURE: STATE DESCRIPTION
State1 and State 2 contains the description of the current thermodynamic state as these seven values
State1 = [4,373,273,100,100,1,0]
State2 = [2,272,273,99,0,0,0]
# Redefine State array:
#State [0] {1=solid, 2=melting, 3=liquid, 4=boiling, 5=vapor}
#State [1] temperature in Kelvin
#State [2] temp of ice in Kelvin (up to max value of Tmelt)
#State [3] percentage progress of solid to liquid
#State [4] temp of water above Tmelt (up to max value of Tvap-Tmelt)
#State [5] percentage progress of liquid to vapor
#State [6] temp of vapor (no limit)
State1=[3,373,273,100,100,0,0] # liquid at 100C
StateLiq50=[3,323,273,100,50,0,0] # input liquid at 50C
State2=[3,273,273,100,0,0,0] # liquid at 0C
StateSolid=[1,200,200,0,0,0,0] # solid ice at 200K