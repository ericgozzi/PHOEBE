import System
import Rhino
import Grasshopper

from Rhino.Geometry import PointContainment

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th



class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self,
            chunks: Grasshopper.DataTree[Rhino.Geometry.Rectangle3d],
            points: System.Collections.Generic.List[Rhino.Geometry.Point3d]):

        if chunks.BranchCount == 0 and points == None:
            ghenv.Component.Message = "Please provide chunks\n Please provide points"
            return
        elif points == None:
            ghenv.Component.Message = "Please provide points"
            return
        elif chunks.BranchCount == 0:
            ghenv.Component.Message = "Please provide chunks"
            return



        """
        In a terrain vast, with chunks so wide,
        The user's points in stillness bide.
        Each cell awaits with space to fill,
        To catch the points that lie at will.
        """
        
        alive_scheme = []
        
        # We traverse each branch, through the grid’s domain,  
        # A map of chunks, each path we attain.  
        for i in range(chunks.BranchCount):
            chunks_list = chunks.Branch(i)
            branchPath = chunks.Path(i)
            
            # For each cell in the list, we start our quest,  
            # Checking if points lie within, at their best.  
            for j in range(chunks_list.Count):
                
                # Now the points, scattered and free,  
                # Will find their place in the chunks, you’ll see.  
                for point in points:
        
                    """
                    Does the point lie within the chunk's form?
                    """
                    containement= chunks_list[j].Contains(point)
                    if containement == PointContainment.Inside:
                        bool = True
                    else:
                        bool = False                
        
                    # If the point’s inside, we make it known,  
                    # Record the position, its status shown.  
                    if bool == 1:
                        print (i, j, bool)                  # Print the status, where it belongs
                        alive_chunk = [i, j]                 # A cell marked alive, as the scheme grows strong
                        alive_scheme.append(alive_chunk)     # Add it to the scheme, the list prolongs
        
        # Finally, the alive scheme, all laid out,  
        # Points in chunks, without a doubt.  
        print(alive_scheme)
        alive_scheme = th.list_to_tree(alive_scheme)
        
        ghenv.Component.Message = "Alive-Scheme created"
        return alive_scheme
