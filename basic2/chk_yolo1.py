from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

cv2.namedWindow("Cone Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Cone Detection", 800, 600)
cv2.setWindowProperty("Cone Detection", cv2.WND_PROP_TOPMOST, 1)

model = YOLO("AIA_XT131_01_v3.pt")

# from PIL
im1 = Image.open(r"chk_yolo1.jpg")
# save=True：存檔
results = model.predict(source=im1, save=False, save_txt=False, conf=0.5, verbose=False)
#results = model.predict(source=im1, save=True, save_txt=True, conf=0.5)

for result in results:
    # Detection
    print("box xyxy:", result.boxes.xyxy)   # box with xyxy format, (N, 4)
    print("box xywh:", result.boxes.xywh)   # box with xywh format, (N, 4)
    print("box xyxyn:", result.boxes.xyxyn)  # box with xyxy format but normalized, (N, 4)
    print("box xywhn:", result.boxes.xywhn)  # box with xywh format but normalized, (N, 4)
    print("box conf:", result.boxes.conf)   # confidence score, (N, 1)
    print("box cls:", result.boxes.cls)    # cls, (N, 1)

    # Classification
    print("cls probs:", result.probs)     # cls prob, (num_class, )

with open("result.txt", '+w') as file:
    for idx, prediction in enumerate(results[0].boxes.xyxy): # change final attribute to desired box format
        cls = int(results[0].boxes.cls[idx].item())
        # Write line to file in YOLO label format : cls x y x y
        file.write(f"{cls} {int(prediction[0].item())} {int(prediction[1].item())} {int(prediction[2].item())} {int(prediction[3].item())}\n")
          

# Visualize the results on the frame
annotated_frame = results[0].plot()
cv2.imshow("Cone Detection", annotated_frame)
cv2.waitKey(5000) # wait ms
cv2.destroyAllWindows()   
