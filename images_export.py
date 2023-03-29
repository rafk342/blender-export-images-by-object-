import bpy 
import os 
 
save_path = r"F:\folder123\path\models" 
 
selected_objects = bpy.context.selected_objects 
 
for obj in selected_objects: 
    materials = obj.data.materials
 
    obj_path = os.path.join(save_path, obj.name)   
    os.makedirs(obj_path, exist_ok=True) 
 
    for mat in materials: 
        if mat is None: 
            continue 
 
        node_tree = mat.node_tree 
 
        for node in node_tree.nodes: 
            if node.type == 'TEX_IMAGE': 
                tex = node.image 
 
                if tex is not None and tex.filepath is not None and tex.packed_file is None: 
                     
                    tex_path = bpy.path.abspath(tex.filepath) 
                    new_tex_name = tex.name.split('.')[0] + os.path.splitext(tex.filepath)[-1] 
 
                    tex.save_render(os.path.join(obj_path, new_tex_name))
