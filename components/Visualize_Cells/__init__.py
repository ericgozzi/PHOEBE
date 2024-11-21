import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
from compas_rhino.conversions import box_to_rhino

class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, cells: System.Collections.Generic.List[object]):
        geometry = []
        
        for c in cells:
            box = c.draw_box()
            geometry.append(box_to_rhino(box))

        geometry = th.list_to_tree(geometry)
        return geometry
