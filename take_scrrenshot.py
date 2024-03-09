from lol_tools.utils.screen_utils import ScreenManager
import cv2
import os
import time

screen_manager = ScreenManager()

output_dir = "output"
if os.path.exists(output_dir):
    pass
else:
    os.mkdir(output_dir)
while True:
    frame = screen_manager.get_latest_frame()
    # convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    path_name = os.path.join(output_dir, f"{time.time()}.png")
    cv2.imwrite(path_name, frame)
    print(f"Saved frame to {path_name}")
    time.sleep(5)
