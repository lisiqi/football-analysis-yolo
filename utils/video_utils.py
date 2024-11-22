import cv2
import numpy as np


def read_video(video_path: str):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(frames: list[np.ndarray], output_path: str):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(
        output_path, fourcc, 10, (frames[0].shape[1], frames[0].shape[0])
    )
    for frame in frames:
        out.write(frame)
    out.release()
