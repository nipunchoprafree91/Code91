from PIL import Image
import pytesseract

# Load the image
image_path = "/Users/nipun/Documents/automation/Pythonforreal/tests/AI/Images/azureclicmd.png"
img = Image.open(image_path)

# Use Tesseract to extract the text
extracted_text = pytesseract.image_to_string(img)

extracted_text.strip()  # Return the extracted text
