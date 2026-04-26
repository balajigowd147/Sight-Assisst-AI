import cv2

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return None

    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        return None

    cap.release()

    return frame


# img = capture_image()

# if img is not None:
#     cv2.imshow("Captured Image", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()