import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs

class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, floors: System.Collections.Generic.List[object]):
            
        if floors == None:
            ghenv.Component.Message = "Please provide floors"
            return


        floors.reverse()

        # A **Blueprint** is formed, with floors now aligned,  
        # A vision in code, perfectly designed.  
        blueprint = Blueprint(floors)

        # Now the **ASCII blueprint** comes to life,  
        # Each floor’s tale, clear without strife.  
        ascii_section = blueprint.get_ASCII_blueprint()

        ghenv.Component.Message = "Have fun with the blueprint!"
        return blueprint, ascii_section




"""
____   .     .     . .____  .___  .___  _ __    _  _______
/   \  /     /     / /      /   \ /   \ | |\   |  '   /   
|,_-<  |     |     | |__.   |,_-' |__-' | | \  |      |   
|    ` |     |     | |      |     |  \  | |  \ |      |   
`----' /---/  `._.'  /----/ /     /   \ / |   \|      /   
                                                            
"""

class Blueprint(object):

    """
    Class Blueprint, a plan in hand,
    Where floors align to firmly stand.
    It holds them close, a steady guide,
    Creating form, with structure wide.
    """

    def __init__(self, floors):
        self.floors = floors





    def get_ASCII_blueprint(self):

        # The blueprint begins with a frame so grand,  
        # A border to guide the design by hand.   
        ascii = "      ____________________     \n"
        ascii +=".    /                    \\     "

        # Through each floor, we weave and trace,  
        # Giving each level its rightful place. 
        for i, floor in enumerate(self.floors):

            floor_number = floor.number     # The floor's number, where it resides 
            function = floor.function       # The role it plays, its function in strides


            # We count the letters, the function’s length,  
            # Then balance the spaces, to give it its strength. 
            string_length = len(list(function))
            white_spaces_number = 20 - string_length

            # Half the spaces, to center the name,  
            # Ensuring balance, symmetry the aim. 
            half_spaces_float = white_spaces_number / 2
            half_spaces_int = int(half_spaces_float)
            

            # Now we build the spaces, soft and wide,  
            # To frame the function on either side.  
            white_spaces = []
            one_space = ""

            for i in range(0, half_spaces_int, 1):
                white_spaces.append(" ")
                if (white_spaces_number % 2 == 1):
                    one_space = " "
            
            # Join the spaces, a perfect line,  
            # Ready to place the function so fine. 
            white_spaces = "".join(white_spaces)


            # Add the function and number with grace,  
            # As each floor takes its rightful space.  
            ascii += ("\n     |{}{}{}{}|              {}. Floor".format(white_spaces, function.upper(), white_spaces, one_space, floor_number))
            
        
        # The blueprint ends with a closing sign,  
        # A boundary firm, the design divine.  
        ascii += "\n________________________________\n"
        ascii += "////////////////////////////////"

        # The masterpiece complete, ready to unfold,  
        # A blueprint of stories, in numbers bold.  
        return ascii
