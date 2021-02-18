from gtts import gTTS       # convert text-to-speech
import PyPDF2               # convert pdf-to-text
from PIL import Image       # process images
import pytesseract          # convert image to text
import os                   # play audio file


def convertTextToSpeech(textFile, audioFile, language):
    fullText = ""
    with open(textFile, 'r') as file:
        for line in file.readlines():
            fullText = f"{fullText} {line.strip()}"     # read all the text from the file

    obj = gTTS(text=fullText, lang=language)
    obj.save(audioFile)


def convertPDFToSpeech(pdfFile, audioFile, language):
    # extract text from pdf file:
    fullText = ""
    with open(pdfFile, 'rb') as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        for pageNumber in range(pdfReader.getNumPages()):
            page = pdfReader.getPage(pageNumber)
            fullText = f"{fullText} {page.extractText()}"

    # save text into a dummy text file:
    textFile = 'dummy-text.txt'
    with open(textFile, 'w') as file:
        file.write(fullText)

    # convert dummy text file into audio file:
    convertTextToSpeech(textFile, audioFile, language)

    # remove created dummy files:
    os.remove(textFile)


def convertImageToSpeech(jpgFile, audioFile, language, tesseractPath):
    pytesseract.pytesseract.tesseract_cmd = tesseractPath

    img = Image.open(jpgFile)
    fullText = pytesseract.image_to_string(img)

    # save text into a dummy text file:
    textFile = 'dummy-text.txt'
    with open(textFile, 'w') as file:
        file.write(fullText)

    # convert dummy text file into audio file:
    convertTextToSpeech(textFile, audioFile, language)

    # remove created dummy files:
    os.remove(textFile)