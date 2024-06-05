import cv2
import numpy as np
import matplotlib.pyplot as plt
from otsu import Otsu
from stroke_extract import extract_signature
from PIL import Image

class SignatureExtractor:
    def __init__(self, input_path):
        self.path = input_path
        self.thresholder = Otsu()
        self.threshold = 0.0

    def extract(self):
        img = cv2.imread(self.path)
        assert img is not None, "Image not found"
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.threshold = self.thresholder.thresholding(gray)

        _, binary_img = cv2.threshold(gray, self.threshold, 255, cv2.THRESH_BINARY)

        # Create a mask for the signature
        signature_mask = binary_img

        # Apply the mask to the original image
        result = cv2.bitwise_and(gray, signature_mask)

        pil_image = Image.fromarray(result)
        signature = extract_signature(pil_image)
        signature.save("output_image.png", "PNG")



if __name__ == '__main__':
    path = 'Signature.jpg'
    extract = SignatureExtractor(path)
    extract.extract()


