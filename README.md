## Signature Extraction
![Binariz(1)](https://github.com/biplavpoudel/Signature-Stroke-Extractor/assets/60846036/5dfcbce2-c045-44ba-9cfc-316be39c836a)

1. This small code binarizes the signature image using ![Otsu's](https://en.wikipedia.org/wiki/Otsu%27s_method) global threhold algorithm.
2. The signature stroke from the binarized image is extracted using PIL (![Pillow](https://pypi.org/project/pillow/)) Library.
3. The image is loaded as RGBA and the alpha value of background is set to 0 using masking and image merging. 
