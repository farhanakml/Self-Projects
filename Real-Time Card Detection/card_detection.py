import cv2
from ultralytics import YOLO

# Load the trained model
model = YOLO("D:/Semester 7/Belajar Bareng/github/Belajar-Bareng/Real-Time Object Detection/train16/weights/best.pt")

cap = cv2.VideoCapture(0)  # Use webcam
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_index = int(box.cls[0])  # Convert to integer
            print("Detected classes:", result.names)  # Debugging step
            print("Box class index:", class_index)  # Debugging step

            # Ensure class exists
            if class_index in result.names:
                label = f"{result.names[class_index]}: {box.conf[0]:.2f}"
            else:
                label = f"Unknown: {box.conf[0]:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
