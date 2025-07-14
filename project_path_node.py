import os
import folder_paths

class ProjectPathNode:
    """
    A node that provides the project path for file operations
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "subfolder": ("STRING", {
                    "default": "outputs",
                    "multiline": False
                }),
            },
            "optional": {
                "create_folder": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("path",)
    FUNCTION = "get_project_path"
    CATEGORY = "utils"
    
    def get_project_path(self, subfolder="outputs", create_folder=True):
        # Get ComfyUI's base directory
        base_path = folder_paths.get_directory_by_type("output")
        
        # If subfolder is specified, join it with base path
        if subfolder:
            full_path = os.path.join(base_path, subfolder)
        else:
            full_path = base_path
            
        # Create folder if it doesn't exist and create_folder is True
        if create_folder and not os.path.exists(full_path):
            os.makedirs(full_path, exist_ok=True)
            
        return (full_path,)

# Required for ComfyUI to recognize the node
NODE_CLASS_MAPPINGS = {
    "ProjectPathNode": ProjectPathNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ProjectPathNode": "Project Path"
}