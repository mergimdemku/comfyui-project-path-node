from comfy.model_management import register_node

class ProjectPathNode:
    @staticmethod
    def INPUT_TYPES():
        return {}  # No inputs needed
    
    RETURN_TYPES = ("STRING",)  # Output is a string
    FUNCTION = "get_project_path"
    CATEGORY = "Custom"

    @staticmethod
    def get_project_path():
        # Set your project folder path here (change as needed)
        project_path = "E:/MyAIProject/"
        return (project_path,)

register_node(ProjectPathNode)
