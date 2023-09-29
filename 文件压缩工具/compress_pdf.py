"""
Author: Lns-XueFeng
Create Time: 2023.9.17
Version: Python3.9
Libray: PyMuPDF==1.23.3
Why write it: 买了Unix网络编程电子书PDF，结果超过了微信读书支持导入的300MB以内，而且市面上的PDF压缩工具普遍要开会员，因此自己实现一个
"""


import os
import fitz


class Compress:
    """ 压缩文件 """
    def __init__(self):
        self.__total_page = None   # 用于指向该document对象的页数

    def __covert_to_pic(self, document, zoom):
        """
          作用：先将pdf文件转换成一张张的jpg图片，存在.pdf文件夹之中
          document: fitz.open()打开源文件得到的对象
          zoom: 清晰度设置，值越大，分辨率越高，文件越清晰
        """
        if os.path.exists(".pdf"):   # 临时文件，需为空
            os.removedirs(".pdf")
        os.mkdir('.pdf')

        for pg in range(self.__total_page):
            page = document[pg]
            zoom = int(zoom)
            rotate = int(0)
            print(page)
            trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            lurl = ".pdf/%s.jpg" % str(pg + 1)
            pm.save(lurl)

        document.close()

    def __pic_to_pdf(self, goal_pdf):
        """
          作用：将.pdf文件夹之中的jpg文件合并为新的pdf文件
          goal_pdf: 最终压缩完成pdf文件的名称
        """
        document = fitz.open()

        for pg in range(self.__total_page):
            img = '.pdf/%s.jpg' % str(pg + 1)
            img_doc = fitz.open(img)   # 打开图片
            pdf_bytes = img_doc.convert_to_pdf()   # 使用图片创建单页的 PDF
            os.remove(img)
            img_pdf = fitz.open("pdf", pdf_bytes)
            document.insert_pdf(img_pdf)   # 将当前页插入文档

        if os.path.exists(goal_pdf):   # 若文件存在先删除
            os.remove(goal_pdf)

        document.save(goal_pdf)   # 保存pdf文件
        document.close()

    def to_pdf(self, source_pdf, goal_pdf, zoom=200):
        """
          作用：将pdf文件进行一定程度的压缩并生成一个新的已压缩pdf文件
          source_pdf: 待压缩的pdf文件名称
          goal_pdf: 压缩完成的pdf文件名称
          zoom: 清晰度设置，值越大，分辨率越高，文件越清晰
        """
        document = fitz.open(source_pdf)
        self.__total_page = document.page_count

        self.__covert_to_pic(document, zoom)
        self.__pic_to_pdf(goal_pdf)

        os.removedirs('.pdf')


if __name__ == "__main__":
    compress = Compress()
    compressed_pdf = compress.to_pdf("UNIX网络编程卷1.pdf", "cUNIX网络编程卷1.pdf")

# Happy ending: 最终得到了一个小于300MB的pdf文件(250MB)，可以愉快的导入微信读书了
