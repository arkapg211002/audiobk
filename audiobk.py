'''ARKAPRATIM GHOSH'''
import pyttsx3
import PyPDF2
book=open('cp.pdf','rb')
pdfread=PyPDF2.PdfFileReader(book)
pages=pdfread.numPages
print(pages)
speak=pyttsx3.init()
for num in range(2,pages+1):
    page=pdfread.getPage(num)
    text=page.extractText()
    #print(text)
    speak.say(text)
    speak.runAndWait()