
from docx import *
# 参考网址 https://blog.csdn.net/ibiao/article/details/78595295
document = Document()
table = document.add_table(3, 3, style="Medium Grid 1 Accent 1")
heading_cells = table.rows[0].cells
heading_cells[0].text = '第一列内容'
heading_cells[1].text = '第二列内容'
heading_cells[2].text = '第三列内容'
document.save(r"demo.docx")
