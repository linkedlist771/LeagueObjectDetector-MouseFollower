import os

current_path = os.path.dirname(__file__)
root_path = os.path.dirname(os.path.dirname(current_path))
lol_tools_path = os.path.join(root_path, "lol_tools")
models_path = os.path.join(lol_tools_path, "models")
YOLO_MODEL_PATH = os.path.join(models_path, "best.pt")
