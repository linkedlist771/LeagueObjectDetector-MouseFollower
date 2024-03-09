from lol_tools.schemas import HeroPosition
from typing import List
import numpy as np
import cv2


def detect_hero_position(frame: np.array) -> List[HeroPosition]:
    pass


image = cv2.imread("img.png")
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
