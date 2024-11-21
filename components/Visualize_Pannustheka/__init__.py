import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import rhinoscriptsyntax as rs
from compas_rhino.conversions import point_to_compas, line_to_rhino, point_to_rhino, mesh_to_rhino, box_to_rhino
from ghpythonlib.componentbase import executingcomponent as component
import ghpythonlib.treehelpers as th
from compas.scene import SceneObject
from compas.geometry import Vector, Point, Translation




class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    
    def RunScript(self, pannustheka):

        if pannustheka == None:
            ghenv.Component.Message = "Please provide pannustheka"
            return


        # The origin, the beginning, the place where it starts, 
        origin = pannustheka.permutations[0].box.frame.point.copy()
        # A point copied from the first, a seed in the soil,  
        # From this, all things will grow, and with it, toil.
        
        
        # Now gather the empty canvas, waiting to be filled,  
        pannus = []
        bbox = []
        points = []
        # Empty vessels, like a poet’s blank page,  
        # Await the coming of shapes to step from the stage.
        
        
        # A dance begins, as permutations swirl,
        for permutation in pannustheka.permutations:
        
            # The mesh, an ethereal shape, now takes form,  
            # In this space, it shall bend and transform.
            mesh = permutation.mesh.copy()
            # The box, a boundary that keeps it all tight,  
            # Holding the chaos, defining the light
            box = permutation.box.copy()
            # Points, like whispers, scattered and free,  
            # Each a part of a greater symmetry.
            c_points = permutation.points.copy()
            
            
        
            # Translation—a shift, a gentle move,  
            # The box’s frame, now set to prove.
            translation_vector = Vector.from_start_end(box.frame.point, origin)
        
            # A matrix born from the vector’s breath,  
            # Shaping form, conquering death.
            translation_matrix = Translation.from_vector(translation_vector)
            
        
            # Mesh transforms, with elegance it moves,  
            # Changing place, its shape improves.
            mesh.transform(translation_matrix)
            pannus.append(mesh_to_rhino(mesh))
            # Brought to life in Rhino's embrace,  
            # The mesh now finds its rightful place.
        
            
            # The bounding box follows close behind,  
            # Transformed, it aligns, in the same frame, confined.
            box.transform(translation_matrix)
            bbox.append(box_to_rhino(box))
            # The edges are sharp, the corners are clear,  
            # In the same world, they now appear.
                
            
            # Points are not forgotten, each one moves,  
            # A soft step forward, as each one improves.
            for pt in c_points:
                pt.transform(translation_matrix)
                points.append(point_to_rhino(pt))
                # A journey they take, across the sky,  
                # Each point ascends, too proud to deny.
                
            
            # The origin climbs, a gentle rise,  
            # Reaching upwards, toward endless skies.
            origin.z = origin.z + 2
            # Upward it soars, in its quiet refrain,  
            # The z-axis bending, again and again.
        
        
        pannus = th.list_to_tree(pannus)
        bbox = th.list_to_tree(bbox)
        points = th.list_to_tree(points)

        ghenv.Component.Message = ""

        return pannus, bbox, points
