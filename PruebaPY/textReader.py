
def text_recognize(namePDF):
    text_pages = []
    reader = PdfReader(namePDF)
    for number_page in range(len(reader.pages)):
        page = reader.pages[number_page]
        text_pages.append(page.extract_text().strip())

    if all(all(not letter.strip() for letter in text_page) for text_page in text_pages):
        print('Se procede a utilziar la herramienta de OCR')
        text_pages = OCR_Tool(namePDF)
    return text_pages

#Funcion de OCR del PDF


def OCR_Tool(namePDF):
    ruta_carpeta_img = '/content/OCRNombramiento/Image Test'
    # Transforma cada una de las paginas del PDF en una imagen formato JPEG
    i = 1
    pages = convert_from_path(namePDF)
    for page in pages:
        img_name = f"img-{i},jpeg"
        page.save(os.path.join(ruta_carpeta_img, img_name), 'JPEG')
        i += 1
    # Se aplica el OCR a cada una de las imagenes
    text_pages = []
    for img_file in os.listdir(ruta_carpeta_img):
        image = cv2.imread(os.path.join(ruta_carpeta_img, img_file))
        text_pages.append(imageOCR(image))
    return text_pages


def imageOCR(image):
    image_gris_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text_OCR_image = pytesseract.image_to_string(image_gris_scale)
    return text_OCR_image
