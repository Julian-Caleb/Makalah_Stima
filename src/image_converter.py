from PIL import Image, ImageDraw

# Crop the image at a specific location to a size of 80x80 pixels.
def crop_image_to_80x80(input_image_path, output_image_path):
    image = Image.open(input_image_path)

    if image.size == (80, 80):
        print("Image is already 80x80 pixels.")
        return

    width, height = image.size
    left = 60
    top = 500
    right = left + 80
    bottom = top + 80
    cropped_image = image.crop((left, top, right, bottom))
    
    cropped_image.save(output_image_path)
    print("Image cropped successfully to 80x80 pixels.")

# Crop the image at the center to a size of 1 pixel by the width of the image.
def crop_middle_row(input_image_path, output_image_path):
    image = Image.open(input_image_path)
   
    width, height = image.size

    row_index = height // 2

    cropped_image = image.crop((0, row_index, width, row_index + 1))

    cropped_image.save(output_image_path)

# Convert the image to binary.
def image_to_binary(input_image_path):
    image = Image.open(input_image_path)

    image = image.convert("L")

    width, height = image.size

    binary_data = ""
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            binary_data += "1" if pixel < 128 else "0"

    return binary_data

# Convert the image format to bitmap.
def image_to_bmp(input_image_path, output_image_path):
    image = Image.open(input_image_path)

    bitmap = image.convert('1')

    bitmap.save(output_image_path)

# Draw a square on the image around a specific index that is converted to x and y positions.
def draw_square_around_index(image_path, n):
    image = Image.open(image_path)
    width, height = image.size
    
    draw = ImageDraw.Draw(image)
    
    row = n // width
    col = n % width
    
    square_size = 60
    thickness = 15
    
    top_left_x = max(0, col - square_size)
    top_left_y = max(0, row - square_size)
    bottom_right_x = min(width - 1, col + square_size)
    bottom_right_y = min(height - 1, row + square_size)
    
    for i in range(thickness):
        draw.rectangle(
            [top_left_x - i, top_left_y - i, bottom_right_x + i, bottom_right_y + i],
            outline="black"
        )
    
    image.save('./result/image_with_square.bmp')
    image.show()
    
    
# image_to_bmp("./tc/2.jpg", "./db/2_waldo.bmp")
# crop_image_to_80x80("./db/2_waldo.bmp", "./db/2_waldo.bmp")
