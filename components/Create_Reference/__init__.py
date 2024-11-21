import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
from compas.geometry import Box
from compas_rhino.conversions import *



class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self,
            mesh: Rhino.Geometry.Mesh,
            box: Rhino.Geometry.Box,
            points: System.Collections.Generic.List[Rhino.Geometry.Point3d],
            function: str):

        
        # A list for points, converted with care,  
        # From Rhino to Compas, a format we share
        c_points = []
        for pt in points:
            c_points.append(point_to_compas(pt))
        
        # The box transitions, Compas it meets,  
        # A transformation complete, the process repeats.  
        box = box_to_compas(box)
        
        # The mesh, like the box, undergoes its turn,  
        # To a new structure where insights burn.  
        mesh = mesh_to_compas(mesh)
        
        # A reference created, its pieces combined,  
        # A structure of logic, where forms are aligned.  
        reference = Reference(box, c_points, mesh, function)
        
        return reference




"""
________________________________________________________________ _______  _________ ___________
\______   \_   _____/\_   _____/\_   _____/\______   \_   _____/ \      \ \_   ___ \\_   _____/
 |       _/|    __)_  |    __)   |    __)_  |       _/|    __)_  /   |   \/    \  \/ |    __)_ 
 |    |   \|        \ |     \    |        \ |    |   \|        \/    |    \     \____|        \
 |____|_  /_______  / \___  /   /_______  / |____|_  /_______  /\____|__  /\______  /_______  /
        \/        \/      \/            \/         \/        \/         \/        \/        \/ 
"""

# A class to guide, a **Reference** named,  
# To organize objects, its purpose proclaimed.  
class Reference(object):
    
    # The constructor defines this geometric crew,  
    # A box, points, a mesh, and a function too. 
    def __init__(self, box, points, mesh, function):
        self.box = box                                  # A bounding box, defining the space
        self.points = points                            # Points to describe the geometry's grace
        self.mesh = mesh                                # A mesh for form, with its net of faces.  
        self.function = function                        # A purpose that logic embraces.  

    # To find the heart, the **centroid** you seek,  
    # A central point where balance will speak.      
    def get_centroid(self):
        centroid = self.box.frame.point                 # The frame reveals the anchor's domain.
        return centroid                                 # The center returned, precision maintained