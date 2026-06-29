import cv2

def test_sharpness():
    """Tests camera focus and displays the sharpness value on the screen."""
    # Initialize camera (0 is default, change to 1 if using Iriun/DroidCam)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    print("--- SHARPNESS TEST ---")
    print("Look at the number on the screen.")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Calculate sharpness (Laplacian variance)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        focus_value = cv2.Laplacian(gray, cv2.CV_64F).var()

        # 2. Display the result on the image stream
        color = (0, 255, 0) if focus_value > 20 else (0, 0, 255)
        text = f"Sharpness: {focus_value:.2f}"
        cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow('Sharpness Calibration', frame)

        # Quit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_sharpness()