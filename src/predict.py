from ultralytics import YOLO
import cv2

def main():
    model = YOLO("./models/carTimer.pt")
    model.predict("./static/videos/parking_crop.mp4", show=True, stream=True)


if __name__ == "__main__":
    main()