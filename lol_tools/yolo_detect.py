from ultralytics import YOLO
import cv2
from ultralytics.engine.results import Results
from lol_tools.configs.yolo_configs import YOLO_MODEL_PATH


class YoloManager:
    _instance = None

    def __new__(cls, model_path: str = YOLO_MODEL_PATH):
        if cls._instance is None:
            cls._instance = super(YoloManager, cls).__new__(cls)
            # 现在，初始化该实例
            cls._instance._init(model_path)
        return cls._instance

    def _init(self, model_path):
        self.model = YOLO(model_path)

    def __call__(self, frame) -> list[Results]:
        return self.model(frame)


# make it dryrun
if __name__ == "__main__":
    model = YoloManager()  # load a pretrained model (recommended for training)
    res = model("../output/1709881264.1948593.png")
    # show results
    res[0].plot(show=True, save=True)  # save as results.png
