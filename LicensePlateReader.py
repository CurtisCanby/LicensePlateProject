import cv2
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_plate_number(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found")

    # Show original image
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 100, 200)

    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    plate_contour = None

    # Find a 4-sided contour
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            plate_contour = approx
            break

    if plate_contour is None:
        return "No plate contour found"

    # Extract plate region
    x, y, w, h = cv2.boundingRect(plate_contour)
    plateimage = gray[y:y + h, x:x + w]

    # Threshold for OCR
    _ , thresh = cv2.threshold(plateimage, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # OCR
    plate_number = pytesseract.image_to_string(thresh, config='--psm 8')

    return plate_number.strip()
