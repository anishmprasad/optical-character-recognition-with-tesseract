from PIL import Image
im = Image.open("./input_images/sample_input.jpg")
im.rotate(45).show()