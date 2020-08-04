"""
读取文件夹生成文件列表
"""
import os

src = r'D:\ocr_recognition01\images\test'
fd = open(r'D:\ocr_recognition01\images\test\test.list', 'a', encoding='utf8')
for dirpath, dirnames, filenames in os.walk(src):
    for filename in filenames:
        if filename.endswith('.jpg'):
            fd.write(os.path.join(src, filename) + '\n')

fd.close()
