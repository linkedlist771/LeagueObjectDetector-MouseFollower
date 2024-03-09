import cv2
import dxcam
import time


class ScreenManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ScreenManager, cls).__new__(cls)
            # Initialize the DXcam instance only once
            cls._instance.camera = dxcam.create()
            cls._instance.camera.start()
        return cls._instance

    def get_latest_frame(self):
        """

        :return: 1600 x 2560 x 3
        """
        return self.camera.get_latest_frame()

    def stop_camera(self):
        if self.camera.is_capturing:
            self.camera.stop()

    @classmethod
    def destroy_instance(cls):
        if cls._instance:
            cls._instance.stop_camera()
            cls._instance = None


if __name__ == "__main__":
    # Create a DXcam instance
    camera = dxcam.create()

    # Start capturing
    camera.start()

    frame_count = 0
    start_time = time.time()

    try:
        while True:
            # Get the latest frame
            frame = camera.get_latest_frame()
            # 1600 x 2560 x 3
            if frame is not None:
                # Increment frame count
                frame_count += 1

                # Calculate elapsed time since start
                elapsed_time = time.time() - start_time

                # Calculate FPS
                fps = frame_count / elapsed_time

                # Display the frame and the FPS
                cv2.putText(
                    frame,
                    "FPS: {:.2f}".format(fps),
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                )
                # 太大了，小一点 0.5
                frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                cv2.imshow("Frame", frame)
                print("FPS: {:.2f}".format(fps))
                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        # Stop capturing
        camera.stop()

        # Destroy all OpenCV windows
        cv2.destroyAllWindows()
