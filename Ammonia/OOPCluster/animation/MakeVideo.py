import cv2
import os


def make_video(folder, fps=60, name="animace.mp4"):

    width = 1000
    height = 957

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(name, fourcc, fps, (width, height))

    frames = os.listdir(folder)

    for frame in frames:
        if frame.endswith('.png'):
            frame_path = os.path.join(folder, frame)
            obrazek = cv2.imread(frame_path)
            video.write(obrazek)

    video.release()
