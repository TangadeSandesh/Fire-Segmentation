from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(source=0 , show=True, save=True, hide_labels=True,hide_conf=True, conf=0.5, save_txt=False, save_crop=False, line_thickness=2, boxes=False)