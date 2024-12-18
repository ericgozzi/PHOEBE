import System
import Rhino
import Grasshopper

import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
import math
from compas.geometry import Transformation, Rotation, Translation, Reflection
from compas.geometry import Vector, Point


class MyComponent(Grasshopper.Kernel.GH_ScriptInstance):
    def RunScript(self, reference, generate):

        if reference == None:
            ghenv.Component.Message = "Please provide reference"
            return
            return
        elif not generate:
            ghenv.Component.Message = "All set up: \n Let's generate all the permutations!"
            return

        if generate: 

            # The process begins, the lines are drawn,  
            # A framework of motion, from dusk to dawn. 
            x_axis = Vector(1, 0, 0)                    
            y_axis = Vector(0, 1, 0)                    
            z_axis = Vector(0, 0, 1)                    

            # The heart of the fabric, the center’s grace,  
            # Around it we twist, reshape its space.  
            centroid = reference.get_centroid()

            # Spins of the loom, rotations defined,  
            # Axis by axis, the threads realigned.
            rotations_z = Matrices.get_roatation_matrix(z_axis, centroid)
            rotations_x = Matrices.get_roatation_matrix(x_axis, centroid)
            rotations_y = Matrices.get_roatation_matrix(y_axis, centroid)

            # Mirrors are placed, reflections we see.
            reflections = Matrices.get_reflection_matrix(centroid)

            # The library is woven, its fabric complete,  
            # Each piece unique, no pattern repeats.
            pannustheka = Pannustheka(reference, rotations_x, rotations_y, rotations_z, reflections)

            # A final check, to sift and refine,  
            # Only the unique, in this laundry line.  
            pannustheka.delete_same_permutations()

        ghenv.Component.Message = "Permutations generated"
        return pannustheka




"""
____    ____        _        _________   _______      _____   ____  ____  
|_   \  /   _|      / \      |  _   _  | |_   __ \    |_   _| |_  _||_  _| 
|   \/   |       / _ \     |_/ | | \_|   | |__) |     | |     \ \  / /   
| |\  /| |      / ___ \        | |       |  __ /      | |      > `' <    
_| |_\/_| |_   _/ /   \ \_     _| |_     _| |  \ \_   _| |_   _/ /'`\ \_  
|_____||_____| |____| |____|   |_____|   |____| |___| |_____| |____||____| 
"""


class Matrices(object):

    """
    In the world of the Matrix, where reality is fake,  
    Transformation is key, as the codes shift and break.  
    Each matrix a doorway, each method a key,  
    Unlocking the truth, setting minds free.  
    """

    def get_roatation_matrix(axis, rotation_point):
        """
        A twist in the code, reality bends,  
        Around an axis, the world never ends.  
        Rotating through space, in a digital trance,  
        With each turn, we break the illusion’s dance.  
        """
        
        # The identity matrix, the ground where we stand,
        # The world unchanging, as if by some hand.
        t0 = Matrices.get_identity_matrix()
        # A 90-degree turn, reality tilts and sways,
        # A quarter-turn twist, shifting the maze.
        r1 = Rotation.from_axis_and_angle(axis, math.pi/2, rotation_point)
        # A 180-degree turn, bending the world in two,
        # The shape shifts further, revealing what's new.
        r2 = Rotation.from_axis_and_angle(axis, math.pi, rotation_point)
        # A 270-degree twist, the illusion unravels more,
        # The boundaries of space become something we explore.
        r3 = Rotation.from_axis_and_angle(axis, (math.pi/2)*3, rotation_point)
        # A collection of turns, four steps in this dance,
        # A symphony of rotation, no matter the chance.
        rotation_list = [t0, r1, r2, r3]
        # Returning the rotations, a journey through space,
        # A broken illusion, a new reality to embrace.
        return rotation_list




    def get_reflection_matrix(centroid_point):
        """
        The mirror of truth, where worlds reflect,  
        In the Matrix’s glass, what’s real we detect.  
        Flip the plane, as the code rewrites,  
        Reflections of freedom in digital lights.  
        """

        # The identity matrix, still as the world stands,
        # A place where nothing changes, as reality expands.
        t0 = Matrices.get_identity_matrix()
        # Reflection on the x-plane, the world turns, flipped,
        # A mirrored view, where the truth is equipped.
        mrx = Reflection.from_plane(([centroid_point[0], centroid_point[1], centroid_point[2]], [1,0,0]))
        # Reflection on the y-plane, bending the code,
        # A shift of perception, where light starts to explode.
        mry = Reflection.from_plane(([centroid_point[0], centroid_point[1], centroid_point[2]], [0,1,0]))
        # Reflection on the z-plane, where depth comes alive,
        # Flipping through dimensions, the Matrix starts to drive.
        mrz = Reflection.from_plane(([centroid_point[0], centroid_point[1], centroid_point[2]], [0,0,1]))
        # A collection of reflections, shifting the shape of space,
        # A new way of seeing, where truth finds its place.
        reflections_list = [t0, mrx, mry, mrz]
        # Returning the reflections, a world turned around,
        # In the mirror of the Matrix, where freedom is found.
        return reflections_list




    def get_identity_matrix(): 
        """
        The Matrix’s base, where all things begin,  
        A world unchanging, where nothing within.  
        It’s the root of all, the place we must start,  
        The code behind the code, the hidden heart.  
        """ 

        # The identity matrix, where nothing changes,  
        # A world in stasis, where time rearranges.
        identity_matrix =   [[1.0000, 0.0000, 0.0000, 0.0000], 
                            [0.0000, 1.0000, 0.0000, 0.0000], 
                            [0.0000, 0.0000, 1.0000, 0.0000], 
                            [0.0000, 0.0000, 0.0000, 1.0000]]
        # Returning the identity, the essence of the start,  
        # The silent code that holds the Matrix apart.
        return identity_matrix

"""
██████╗  █████╗ ███╗   ██╗███╗   ██╗██╗   ██╗███████╗
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██║   ██║██╔════╝
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║██║   ██║███████╗
██╔═══╝ ██╔══██║██║╚██╗██║██║╚██╗██║██║   ██║╚════██║
██║     ██║  ██║██║ ╚████║██║ ╚████║╚██████╔╝███████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
"""

class Pannus(object):
    """
    A garment in the code, woven from points and threads,  
    Each point a stitch, each change a shift.  
    Like clothes hung out, blowing in the breeze,  
    The fabric shifts and flows with each gentle spin.
    """

    def __init__(self, reference, rotation_x, rotation_y, rotation_z, reflection, transformed_points):
        """
        The washing begins—spinning, turning, and pressing,  
        The cloth gets cleaned, its shape confessing.  
        Points are turned, stretched, and renewed,  
        A new fabric appears, in a fresh point of view.
        """
        # The threads of the fabric, reshaped and defined,
        # Each transformed point forms a new design.
        self.points = transformed_points
        self.points_count = len(self.points)
        # The cloth before the wash, unaltered and plain,
        # The original form, before shifts begin their reign.
        self.original_mesh = reference.mesh
        self.rotation_z = rotation_z
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.reflection = reflection
        
        # A fabric transformed, each fold and crease,
        # Spun through reflections and rotations, to find release.
        mesh = self.original_mesh.copy()
        mesh.transform(reflection)
        mesh.transform(rotation_z)
        mesh.transform(rotation_x)
        mesh.transform(rotation_y)
        self.mesh = mesh
        
        # Stitches of memory, marking where points align,
        # A rule emerges from the cloth’s woven design.
        rule_string = []
        
        # The garment’s frame, its corners precise,
        # A box that contains its vertices, so nice.
        self.box = reference.box
        self.vertices = reference.box.points

        # Generating the fabric's unique passport,
        # Where points meet the frame, their positions report.   
        for vertex in self.vertices:
            i = 0
            gate = True
            for point in self.points:
                # Checking if a thread aligns with the frame,
                # Marking its position in this geometric game.
                if round(point.x, 3) == round(vertex.x, 3) and round(point.y, 3) == round(vertex.y, 3) and round(point.z, 3) == round(vertex.z, 3):
                    rule_string.append(1)
                    gate = False
                # If no alignment, a gap appears,
                # A void in the weave, like forgotten years.    
                if i == self.points_count -1 and gate:
                    rule_string.append(0)
                i += 1
        # The unique pattern of the cloth is set,
        # Its rule defined, like a tailored silhouette.
        self.rule = rule_string
        self.function = reference.function




    def generate_all_pemutations(reference, rotations_x, rotations_y, rotations_z, reflections):
        """
        The cloth, stretched wide, hung on many lines,  
        Each fold, each twist, in the wind it climbs.  
        The fabric reshapes, new patterns are born,  
        Spinning in the breeze, like clothes on a morn.
        """
        # A collection of garments, each with a new face,
        # Twisting and turning, reshaped in their place
        pannustheka = []
        # Through reflections, the mirror bends the cloth,
        # Folding its shape, like a washer's froth.
        for mr in reflections:                    
            for rz in rotations_z:
                for rx in rotations_x:
                    for ry in rotations_y:
                        # The cloth spins, its threads take new forms,
                        # Rotated and mirrored, reshaping the norms.
                        transformed_points = Pannus.transform_points(reference.points, mr, rx, ry, rz)
                        pannus = Pannus(reference, rx, ry, rz, mr, transformed_points)
                        pannustheka.append(pannus)
        # Each garment reborn, a new design revealed,
        # Hung in the pannustheka, its fate is sealed.          
        return pannustheka




    def transform_points(points, reflection, rotation_x, rotation_y, rotation_z):
        """
        Each point a thread, spun and twisted around,  
        The fabric reshaped, turning, spinning, unbound.  
        Like clothes swaying, each point takes flight,  
        In a fresh new direction, changing its sight.
        """
        # A new thread begins, a journey to weave,  
        # Each point reshaped, its form to perceive.
        point_group = []
        for point in points:
            # The thread is copied, its essence retained,  
            # Ready for transformation, its shape unchained
            pt = point.copy()
            # A reflection in glass, a reversal so clear,  
            # Flipping the thread to a view more near.
            pt.transform(reflection)
            # Twisting through angles, like cloth in the breeze,  
            # Each rotation a fold, a moment to seize.
            pt.transform(rotation_z)
            pt.transform(rotation_x)
            pt.transform(rotation_y)
            # The thread joins the group, a stitch in the seam,  
            # Completing the pattern, like cloth in a dream.
            point_group.append(pt)
        # The fabric returns, reshaped and refined,  
        # A collection of points, with purpose aligned.
        return point_group


    def get_file_name(self):
        """
        A label stitched into the cloth, its name so true,  
        A pattern formed from the rules, a design to view.  
        The file is the garment, marked for all to see,  
        With a name that tells the story of its fabric’s decree.
        """
        file_name = self.function + "_" + str(self.rule) + ".3dm"
        return file_name

"""
██████╗  █████╗ ███╗   ██╗███╗   ██╗██╗   ██╗███████╗████████╗██╗  ██╗███████╗██╗  ██╗ █████╗ 
██╔══██╗██╔══██╗████╗  ██║████╗  ██║██║   ██║██╔════╝╚══██╔══╝██║  ██║██╔════╝██║ ██╝ ██╔══██╗
██████╔╝███████║██╔██╗ ██║██╔██╗ ██║██║   ██║███████╗   ██║   ███████║█████╗  █████║  ███████║
██╔═══╝ ██╔══██║██║╚██╗██║██║╚██╗██║██║   ██║╚════██║   ██║   ██╔══██║██╔══╝  ██╔═██╗ ██╔══██║
██║     ██║  ██║██║ ╚████║██║ ╚████║╚██████╔╝███████║   ██║   ██║  ██║███████╗██║  ██║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

"""

class Pannustheka(object):
    """
    A library of wonders, where fabrics combine,  
    Permutations of cloth, in threads they align.  
    Each twist, each turn, a new piece unfolds,  
    The library overflows with stories untold.
    """
    def __init__(self, reference, rotations_x, rotations_y, rotations_z, reflections):
        """
        The basket is empty, awaiting its fill,  
        Garments of wonder, shaped by the will.  
        Each fold and twist, a dance of delight,  
        As the cloth transforms in the morning light.
        """
        # The permutations begin, each one unique,  
        # Threads interwoven, a form to seek.
        self.permutations = []

        for mr in reflections:                    
            for rz in rotations_z:
                for rx in rotations_x:
                    for ry in rotations_y:

                        # The fabric is spun through mirrors and turns,  
                        # Each pannus a story, a craft to discern.
                        transformed_points = Pannus.transform_points(reference.points, mr, rx, ry, rz)
                        pannus = Pannus(reference, rx, ry, rz, mr, transformed_points)

                        # The library receives this freshly woven piece,  
                        # A permutation created, its work to release.
                        self.permutations.append(pannus)




    def delete_same_permutations(self):
        """
        The basket is full, yet order must reign,  
        Sorting through garments, we strive to sustain.  
        Each fold inspected, each thread aligned,  
        Removing duplicates, a clearer desig
        """
        # A new collection begins, fresh and refined,  
        # Only unique patterns, a treasure to find.
        reduced_pannustheka = []
        identity_list = []
        
        for pannus in self.permutations:
            # If this garment’s pattern is one of a kind,  
            # Into the collection, it’s lovingly assigned
            if pannus.rule not in identity_list:
                reduced_pannustheka.append(pannus)
                identity_list.append(pannus.rule)  

        # The library now holds a more perfect selection,  
        # A wardrobe of harmony, free from imperfection.
        self.permutations = reduced_pannustheka