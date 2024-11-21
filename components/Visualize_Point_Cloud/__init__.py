import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
from compas_rhino.conversions import point_to_rhino


class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, point_cloud: System.Collections.Generic.List[object]):
        points = []
        for p in point_cloud:
            points.append(point_to_rhino(p))
        points = th.list_to_tree(points)
        return points
