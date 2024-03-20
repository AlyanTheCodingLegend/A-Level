import cv2
import numpy as np

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Gaussian blur to reduce noise
    # image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Apply adaptive thresholding to binarize the image
    _, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    
    return thresholded

def main():
    # Load the reference fingerprint template
    reference_template = preprocess_image('reference_fingerprint.jpg')

    # Initialize the camera (you may need to change the index)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Preprocess the captured frame
        processed_frame = preprocess_image(gray)

        # Match the template with the processed frame using template matching
        result = cv2.matchTemplate(processed_frame, reference_template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold for matching (adjust as needed)
        threshold = 0.8

        # Get the locations where the template matches the frame
        locations = np.where(result >= threshold)

        # Draw rectangles around the matching regions
        for pt in zip(*locations[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + reference_template.shape[1], pt[1] + reference_template.shape[0]), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Fingerprint Scanner', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
        