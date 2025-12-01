# blurmecam/main.py
import cv2
import argparse
import pyvirtualcam
from pyvirtualcam import PixelFormat

from uniface import RetinaFace  # Only detection

def run(blur_strength: int = 51, blur_sigma: int = 30, show_preview: bool = True):
    # Kernel size must be odd
    if blur_strength % 2 == 0:
        blur_strength += 1

    detector = RetinaFace()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Could not read from webcam")

    h, w, _ = frame.shape

    cam = pyvirtualcam.Camera(
        width=w,
        height=h,
        fps=30,
        fmt=PixelFormat.BGR,
        backend='obs'
    )
    print(f"[BlurMeCam] Virtual camera started: {cam.device}")
    print("[BlurMeCam] Press 'b' to toggle blur, 'q' to quit")

    blur_enabled = True

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output = frame.copy()

        if blur_enabled:
            faces = detector.detect(frame)

            if faces:
                for face in faces:
                    x1, y1, x2, y2 = map(int, face["bbox"])

                    x1 = max(0, x1)
                    y1 = max(0, y1)
                    x2 = min(w, x2)
                    y2 = min(h, y2)

                    if x2 <= x1 or y2 <= y1:
                        continue

                    face_roi = output[y1:y2, x1:x2]
                    face_roi = cv2.GaussianBlur(
                        face_roi,
                        (blur_strength, blur_strength),
                        blur_sigma
                    )
                    output[y1:y2, x1:x2] = face_roi

        if show_preview:
            cv2.imshow("BlurMeCam (B=toggle blur, Q=quit)", output)

        cam.send(output)
        cam.sleep_until_next_frame()

        if show_preview:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            elif key == ord("b"):
                blur_enabled = not blur_enabled
                print("[BlurMeCam] Blur enabled:", blur_enabled)
        else:
            # no preview → still allow Ctrl+C in terminal to stop
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()
    cam.close()
    print("[BlurMeCam] Stopped.")


def cli():
    parser = argparse.ArgumentParser(
        description="Blur faces from your webcam and output to a virtual camera."
    )
    parser.add_argument(
        "--strength",
        type=int,
        default=51,
        help="Gaussian blur kernel size (odd number, e.g. 31, 51).",
    )
    parser.add_argument(
        "--sigma",
        type=int,
        default=30,
        help="Gaussian blur sigma value.",
    )
    parser.add_argument(
        "--no-preview",
        action="store_true",
        help="Disable local preview window.",
    )

    args = parser.parse_args()
    run(
        blur_strength=args.strength,
        blur_sigma=args.sigma,
        show_preview=not args.no_preview,
    )


if __name__ == "__main__":
    cli()
