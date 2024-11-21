import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp
from ghpythonlib import treehelpers
from Rhino.Geometry import Plane, Point3d
import rhinoscriptsyntax as rs




class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, size_x: float, size_y: float, extent_x: int, extent_y: int):


        print(size_x, size_y, extent_x, extent_y)

        if size_x == None: 
            size_x = 1
        if size_y == None:
            size_y = 1
        if extent_x == None:
            extent_x = 10
        if extent_y == None:
            extent_y = 10


        # A plane of origin, from points it does rise,a
        # The basis of geometry beneath endless skies.
        origin_plane = Plane(Point3d(0, 0, 0), Point3d(1, 0, 0), Point3d(0, 1, 0))
        
        # Rectangles emerge, like tiles on a floor,
        # Crafted by Rectangular, their shapes we explore.
        rectangles = ghcomp.Rectangular(origin_plane, size_x, size_y, extent_x, extent_y).cells
        
        # From a collection, we form a reversed stream,
        # To organize rectangles with a logical theme.
        rectangles = list(rectangles)

        
        # Dividing rectangles into chunks so grand,
        # Each group aligned by the extent's command.
        chunks = partition_list(rectangles, extent_y)
        
        # Convert the chunks to a tree, so it may grow,
        # Nested structures where data may flow.
        chunks = treehelpers.list_to_tree(chunks)
        
        # A terrain we shape, a surface we plot,
        # Upon the WorldXY plane, our design is brought.
        terrain = rs.AddPlaneSurface( rs.WorldXYPlane(), size_x * extent_x, size_y * extent_y)
        
        ghenv.Component.Message = "Terrain generated"

        return terrain, chunks


def partition_list(lst, num):
    # To break the list into chunks so neat,
    # Dividing it whole, into pieces discrete.
    return [lst[i:i + num] for i in range(0, len(lst), num)]
