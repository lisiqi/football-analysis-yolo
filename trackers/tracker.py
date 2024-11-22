import numpy as np
from ultralytics import YOLO


class Tracker:
    def __init__(self):
        pass

    def detect_frames(self, frames: list[np.ndarray]):
        detections = self.model.predict(frames, save=False)
        return detections

    def get_object_tracks(self, frames: list[np.ndarray]):
        detections = self.detect_frames(frames)
