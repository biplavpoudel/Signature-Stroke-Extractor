import cv2
import numpy as np

class Otsu:
    def __init__(self, bins=256):
        self.bins = bins

    def thresholding(self, img, is_normalized=True) -> float:
        # Set total number of bins in the histogram
        bins_num = self.bins

        # Get the image histogram
        hist, bin_edges = np.histogram(img, bins=bins_num)

        # Get normalized histogram if it is required
        if is_normalized:
            hist = np.divide(hist.ravel(), hist.max())

        # Calculate centers of bins
        bin_mids = (bin_edges[:-1] + bin_edges[1:]) / 2.

        # Iterate over all thresholds (indices) and get the probabilities w1(t), w2(t)

        # weight1 represents the probability of a pixel intensity being in the foreground for each threshold
        # If hist is [h0, h1, h2, h3, ...], then weight1 will be [h0, h0+h1, h0+h1+h2, h0+h1+h2+h3, ...]
        weight1 = np.cumsum(hist)

        # weight2 represents the probability of a pixel intensity being in the background for each threshold.
        # If hist is [h0, h1, h2, h3], then hist[::-1] will be [h3, h2, h1, h0].
        # The cumulative sum of this reversed array will be [h3, h3+h2, h3+h2+h1, h3+h2+h1+h0].
        # Reversing this result back to the original order gives
        # weight2 = [h3+h2+h1+h0, h3+h2+h1, h3+h2, h3]
        weight2 = np.cumsum(hist[::-1])[::-1]

        # Get the class means mu0(t)
        mean1 = np.cumsum(hist * bin_mids) / weight1
        # Get the class means mu1(t)
        mean2 = (np.cumsum((hist * bin_mids)[::-1]) / weight2[::-1])[::-1]

        inter_class_variance = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

        # Maximize the inter_class_variance function val
        index_of_max_val = np.argmax(inter_class_variance)

        threshold = float(bin_mids[:-1][index_of_max_val])
        # print("Otsu's algorithm implementation thresholding result: ", threshold)
        return threshold

if __name__ == '__main__':
    img = cv2.imread('images/test.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    otsu = Otsu()
    threshold = otsu.thresholding(img)
    _, binary_img = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binarized Image', binary_img)
    cv2.waitKey(0)