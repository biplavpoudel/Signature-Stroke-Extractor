from PIL import Image


def extract_signature(image):

    # Convert the image to RGBA (if not already in RGBA format)
    image = image.convert("RGBA")

    # Create a mask for the signature
    signature_mask = Image.new("L", image.size, 0)
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = image.getpixel((x, y))
            if r < 100 and g < 100 and b < 100:
                signature_mask.putpixel((x, y), 255)

    # Apply the mask to the image
    signature = Image.composite(image, Image.new("RGBA", image.size, (255, 255, 255, 0)), signature_mask)
    return signature


