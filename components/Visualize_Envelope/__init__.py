import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
from compas_rhino.conversions import mesh_to_rhino


class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, envelope: System.Collections.Generic.List[object]):
        geometry = []
        for m in envelope:
            geometry.append(mesh_to_rhino(m))

        geometry = th.list_to_tree(geometry)
        return geometry
