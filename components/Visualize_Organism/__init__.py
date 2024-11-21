import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
from compas_rhino.conversions import box_to_rhino

class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, organism):
        geometry = []
        
        for c in organism.get_cells():
            if c.is_alive():
                box = c.draw_box()
                geometry.append(box_to_rhino(box))
        geometry = th.list_to_tree(geometry)
        return geometry
