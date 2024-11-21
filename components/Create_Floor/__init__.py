import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th

class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, floor_functions: System.Collections.Generic.List[str]):

        if floor_functions == None:
            ghenv.Component.Message = "Please provide list of floors functions"
            return

        floors = []
        #The pairing starts, the list unfolds,
        for i, function in enumerate(floor_functions):
            #A floor takes shape, its story told.
            #Its number set, its role defined,
            floor = Floor(i, function)
            #Each step reveals a thoughtful design.
            floors.append(floor)
            
        ghenv.Component.Message = f"Created {len(floors)} floors"

        floors = th.list_to_tree(floors)
        return floors



"""
/$$$$$$$$ /$$        /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ 
| $$_____/| $$       /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$
| $$      | $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$   | $$      | $$  | $$| $$  | $$| $$$$$$$/|  $$$$$$ 
| $$__/   | $$      | $$  | $$| $$  | $$| $$__  $$ \____  $$
| $$      | $$      | $$  | $$| $$  | $$| $$  \ $$ /$$  \ $$
| $$      | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$/
|__/      |________/ \______/  \______/ |__/  |__/ \______/                                                            
"""
class Floor(object):

    """
    A Floor object, simple and neat,
    To help a blueprint be complete.
    Its number shows its ordered spot,
    Its function tells the role it's got.
    """

    def __init__(self, number, function):
        self.number = number
        self.function = function