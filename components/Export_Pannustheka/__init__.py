import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import rhinoscriptsyntax as rs
import Rhino.FileIO
import System
from compas_rhino.conversions import mesh_to_rhino, point_to_rhino, box_to_rhino




class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, pannustheka, file_path, export):


        if pannustheka == None:
            ghenv.Component.Message = "Please provide pannustheka"
            return
        elif file_path == None:
            ghenv.Component.Message = "Please provide pannustheka file_path"
            return
        elif not export:
            ghenv.Component.Message = "All set up: let's export!" 
            return


        """
        ___  __  __  ___    ___    ___   _____   ___   _  _    ___                  
        | __| \ \/ / | _ \  / _ \  | _ \ |_   _| |_ _| | \| |  / __|                 
        | _|   >  <  |  _/ | (_) | |   /   | |    | |  | .` | | (_ |                 
        |___| /_/\_\ |_|    \___/  |_|_\   |_|   |___| |_|\_|  \___|                 
        ___     _     _  _   _  _   _   _   ___   _____   _  _   ___   _  __    _   
        | _ \   /_\   | \| | | \| | | | | | / __| |_   _| | || | | __| | |/ /   /_\  
        |  _/  / _ \  | .` | | .` | | |_| | \__ \   | |   | __ | | _|  | ' <   / _ \ 
        |_|   /_/ \_\ |_|\_| |_|\_|  \___/  |___/   |_|   |_||_| |___| |_|\_\ /_/ \_\
        
                AN EPIC POEM                                                                        
                                                        
        
                
            PROEM
        
                Lo! The mighty function arises, its task to craft
                A file of destiny, where data shall be drafted.
                It calls upon the mesh, the points, and the name,
                To export them to a realm where they are made to claim.
        """


        # The loop now begins, as permutations arise,
        # Each one a new path, each one a new prize.   
        if export:
            for permutation in pannustheka.permutations:
                
                # The path to the file, for each permutation made,
                # Defined by *get_file_name*, where it shall be laid.
                specific_file_path = file_path + permutation.get_file_name()

                # The mesh, transformed by magic unseen,
                # *mesh_to_rhino* makes it serene.
                specific_mesh = mesh_to_rhino(permutation.mesh)

                # The points, too, must be converted,
                # *point_to_rhino* takes them to where
                # to read and write, each a shining light.
                specific_points = []
                for pt in permutation.points: specific_points.append(point_to_rhino(pt))

                # The vertices, too, must follow this path,
                # Converted to Rhinos, to avoid their wrath.
                specific_vertices = []
                for pt in permutation.vertices: specific_vertices.append(point_to_rhino(pt))

                # At last, the export function calls with great might,
                # And the file is written, to the great delight.
                export_file(specific_mesh, specific_points, specific_vertices, specific_file_path)

        ghenv.Component.Message = "Exported"

        return

    
def export_file(mesh, points, vertices, file_path_function):
    # Behold, the file to export, a vessel anew,
    # *File3dm*, empty and waiting for you.
    file_to_export = Rhino.FileIO.File3dm()
    
    # The layers shall be forged with colors bold,
    # Each object to reside in a layer of gold.
    layer_table = file_to_export.AllLayers
    
    # Mesh in black, the first to arise,
    # Points in red, a fiery surprise,
    # Bounding box, as blue as the sky,
    # These colors shall guide, where the objects lie.
    layer_table.AddLayer("mesh", System.Drawing.Color.Black)
    layer_table.AddLayer("points", System.Drawing.Color.Red)
    layer_table.AddLayer("bounding_box_points", System.Drawing.Color.Blue)
    
    # Now, the objects, like stars, must be placed,
    # In the right layer, with care and with grace.
    object_table = file_to_export.Objects
    objects_attributes = Rhino.DocObjects.ObjectAttributes()
    
    # The mesh to layer 0, where it will rest,
    # In the "mesh" layer, it will be its best.
    objects_attributes.LayerIndex = 0
    object_table.AddMesh(mesh, objects_attributes) 

    # Points to layer 1, where they will be seen,
    # Each one of red, like a fiery dream
    objects_attributes.LayerIndex = 1
    if isinstance(points, list):

        # If points are many, iterate and add them,
        # One by one, they shall be given their form.   
        for p in points:
            object_table.AddPoint(p, objects_attributes)
    else:
        # If a single point stands in the light,
        # Add it directly, without fright.
        object_table.AddPoint(points, objects_attributes)


    # Vertices to layer, blue as the sea,
    # These points of bounding boxes will forever be free.
    objects_attributes.LayerIndex = 2
    # If vertices are many, iterate through the fray,
    # Add them to the file, without delay.
    if isinstance(vertices, list):
        for p in vertices:
            object_table.AddPoint(p, objects_attributes)
    else:
        # One vertex alone shall stand in the blue,
        # Add it with care, as the code must do.
        object_table.AddPoint(points, objects_attributes)
    
    # And now, the file is ready to be sealed,
    # The write options set, the path revealed.
    # Version 8 it shall bear, a future so bright,
    # Export it, and let it take flight. 
    
    write_options = Rhino.FileIO.File3dmWriteOptions()
    write_options.Version = 8
    file_to_export.Write(file_path_function, write_options)





""" 

    EPILOGUE
    
    
            Thus ends this saga, this code's noble flight,
            A tale of creation, in the soft moonlight.
            The file now complete, its mission divine,
            Till the next great export, when the stars align.


"""
