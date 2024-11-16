from ultralytics import YOLO

model = YOLO("yolo11l.pt")
# model = YOLO("models/best.pt")

results = model.predict("input_videos/football.mp4", save=True, conf=0.5, iou=0.5)

print(results[0])
print("================")

for box in results[0].boxes:
    print(box)
