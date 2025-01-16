import cv2 as cv
import os

def main():
    media = cv.VideoCapture("./static/videos/prefeitura_static_04.mp4")
    
    if not media.isOpened():
        print("Error: Could not open media file")
        return
    
    fps = media.get(cv.CAP_PROP_FPS)

    total_frames = int(media.get(cv.CAP_PROP_FRAME_COUNT))
    frame_interval = int(fps / 2)

    frame_number = 0
    saved_frames = 0

    while media.isOpened():
        ret, frame = media.read()
        
        

        if not ret:
            print("Error: Could not read frame")
            break

        if frame_number % frame_interval == 0:
            cv.imwrite(f"./static/images/prefeitura_static_04_{frame_number}.jpg", frame)
            saved_frames += 1
        
        frame_number += 1


if __name__ == "__main__":
    main()