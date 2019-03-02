import docx
from docx import Document
path = "word.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)

#输出docx文件的内容
