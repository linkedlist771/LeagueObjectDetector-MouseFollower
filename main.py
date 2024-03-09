from lol_tools.utils.screen_utils import ScreenManager
from lol_tools.utils.input_utils import InputManager
from lol_tools.yolo_detect import YoloManager
from lol_tools.schemas import HeroPosition, EnemyStatus, BaseHero, HeroType
import json
import cv2
from typing import List
import keyboard
import argparse
from loguru import logger

running = False  # 定义一个标志，用于控制循环


def toggle():
    global running
    running = not running
    if running:
        logger.info("Started.")
    else:
        logger.info("Paused.")


parser = argparse.ArgumentParser(description="Run the program")
parser.add_argument(
    "--invoke_key", type=str, default="ctrl+x", help="The key to invoke the program"
)


if __name__ == "__main__":
    input_image = None
    args = parser.parse_args()
    key = args.invoke_key
    logger.info(f"Press {key} to start the program.")
    keyboard.add_hotkey(key, toggle)  # 绑定ctrl+c到toggle函数

    try:
        while True:
            if running:  # 只有当ctrl+x被按下时，才执行循环内的代码
                hero_positions: List[HeroPosition] = []
                yolo_manager = YoloManager()
                input_manager = InputManager()
                screen_manager = ScreenManager()
                input_image = screen_manager.get_latest_frame()
                input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
                detect_results = yolo_manager(input_image)
                detect_results = detect_results[0]
                # detect_results.plot(show=True)
                detect_results = detect_results.tojson()
                if len(eval(detect_results)) == 0:
                    logger.info("No hero detected.")
                    continue
                detect_results = json.loads(detect_results)

                for result_json in detect_results:
                    name = result_json["name"]
                    x1 = result_json["box"]["x1"]
                    y1 = result_json["box"]["y1"]
                    x2 = result_json["box"]["x2"]
                    y2 = result_json["box"]["y2"]
                    enemy_status = None
                    if name == "Enemy_High_Health":
                        enemy_status = EnemyStatus.EnemyHighHealth
                    elif name == "Enemy_Low_Health":
                        enemy_status = EnemyStatus.EnemyLowHealth
                    elif name == "Enemy_Medium_Health":
                        enemy_status = EnemyStatus.EnemyMediumHealth

                    hero_position = HeroPosition(
                        x1=x1,
                        y1=y1,
                        x2=x2,
                        y2=y2,
                        hero=BaseHero(name=name, type=HeroType.ENEMY),
                        health_type=enemy_status,
                    )
                    x1 = int(result_json["box"]["x1"])
                    y1 = int(result_json["box"]["y1"])
                    x2 = int(result_json["box"]["x2"])
                    y2 = int(result_json["box"]["y2"])
                    hero_positions.append(hero_position)

                if hero_positions:
                    hero_pos0 = hero_positions[0]
                    x, y = hero_pos0.get_center()

                    input_manager.move_mouse(x, y)

    except KeyboardInterrupt:
        # cv2.destroyAllWindows()  # Close all OpenCV windows
        logger.info("Program terminated.")
