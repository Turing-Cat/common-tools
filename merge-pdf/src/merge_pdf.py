# 导入PyPDF2库
from PyPDF2 import PdfMerger
import sys

# 创建一个合并器对象
merger = PdfMerger()
pdfList = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue
    pdfList.append(arg)
print(pdfList)
for item in pdfList:
    merger.append(item)

# 输出合并后的PDF文件
merger.write("merged_file.pdf")

# 关闭合并器对象
merger.close()
