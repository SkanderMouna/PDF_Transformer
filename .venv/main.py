import fitz  # PyMuPDF
from PIL import Image
import os


def take_screenshot(pdf_path, output_folder, rectangle):
    doc = fitz.open(pdf_path)
    for page_num in range(doc.page_count):
        page = doc[page_num]

        x, y, width, height = rectangle
        pix1 = page.get_pixmap(matrix=fitz.Matrix(200 / 72, 200 / 72))  # Set resolution (adjust as needed)
        pix1.set_origin(0, 50)
        pix1.save(output_folder + '/' + str(page_num) + '.png')

        # pix2 = fitz.Pixmap(fitz.csRGB, fitz.Rect(0, 0, 800, 600))
        # # pix2.set_origin(0, 0)
        # pix2.copy(pix1, rectangle)
        #
        # pix2.save(output_folder + '/' + str(page_num) + '.png')
        pix1 = None
        pix2 = None
    doc.close()

# f
def delete_first_two_documents(folder_path):
    # Get a list of files in the folder
    files = os.listdir(folder_path)

    # Sort the files to ensure a consistent order
    files.sort()

    # Delete the first two files
    for i in range(2):
        if files:
            file_to_delete = os.path.join(folder_path, files[i])
            try:
                os.remove(file_to_delete)
                print(f"Deleted: {file_to_delete}")
            except Exception as e:
                print(f"Error deleting {file_to_delete}: {e}")

def insert_image_inPage_documents(page,image_file,image_folder_path,x_up, y_up, x_down, y_down):
    # Open the image using Pillow
    image_path = os.path.join(image_folder_path, image_file)
    image = Image.open(image_path)


    # Convert the image to a Pixmap

    with open(image_path) as image_file:
        img_pixmap = fitz.Pixmap(image_file)


    # Insert the image into the PDF page
    page.insert_image(fitz.Rect(x_up, y_up, x_down, y_down), pixmap=img_pixmap)

def insert_images_into_pdf(image_folder_path):
    # Create a new PDF document
    pdf_document = fitz.open()

    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(image_folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Iterate through each image in the folder
    index = 0
    while index < len(image_files):
        x_up=20
        x_down=350
        y_up = 5
        y_down = 260
        # Create a new page for each image
        page = pdf_document.new_page(width=600, height=800)
        add_stripped_line(page,width=600, height=800)


        index2=1
        while (index < len(image_files))&(index2<=3):
            image_file = image_files[index]
            insert_image_inPage_documents(page, image_file,image_folder_path,x_up, y_up, x_down, y_down)
            index2+=1
            index += 1
            y_up = y_down
            y_down =y_up+ 260


    # Save the generated PDF
    output_pdf_path = "output.pdf"  # You can change the output PDF path as needed
    pdf_document.save(output_pdf_path)
    pdf_document.close()

def add_stripped_line(page,width, height):
    stripe_height = 1  # Adjust the height of each stripe as needed
    num_stripes = height
    y_position=0

    for i in range(num_stripes):
        stripe_rect = fitz.Rect(0, y_position, width, y_position + stripe_height)
        x=1
        page.draw_rect(stripe_rect, color=fitz.utils.getColor('snow'))
        y_position=stripe_height*(15*i)



############ MAIN
# generate the screenshots
images_folder = "output_folder"
rectangle_values = (100, 200, 2816, 1386)
take_screenshot("./input.pdf", images_folder, rectangle_values)

# delete the first two screenshots
folder_path = "./output_folder"
delete_first_two_documents(folder_path)

# insert images in a pdf file compressed
insert_images_into_pdf(images_folder)
