# 通过遍历文件写入对应的文档，进行训练
import os
from PIL import Image

dict01 = {'0': '90', '1': '91', '2': '92', '3': '93', '4': '94', '5': '95', '6': '58', '7': '59', '8': '60', '9': '61',
          'a': '64',
          'b': '65', 'c': '66', 'd': '67', 'e': '68', 'f': '69', 'g': '70', 'h': '71', 'i': '72', 'j': '73',
          'k': '74',
          'l': '75', 'm': '76', 'n': '77', 'o': '78', 'p': '79', 'q': '80', 'r': '81', 's': '82', 't': '83',
          'u': '84',
          'v': '85', 'w': '86', 'x': '87', 'y': '88', 'z': '89', 'A': '32', 'B': '33', 'C': '34', 'D': '35',
          'E': '36',
          'F': '37', 'G': '38', 'H': '39', 'I': '40', 'J': '41', 'K': '42', 'L': '43', 'M': '44', 'N': '45', 'O': '46',
          'P': '47', 'Q': '48', 'R': '49', 'S': '50', 'T': '51', 'U': '52', 'V': '53', 'W': '54', 'X': '55', 'Y': '56',
          'Z': '57'}

src = r"D:\ocr_recognition01\test_data\train_images"
fd = open(r'D:\ocr_recognition01\train_data\train.list', 'a', encoding='utf8')
for dirpath, dirnames, filenames in os.walk(src):
    for filename in filenames:
        if filename.endswith('.jpg'):
            ob = Image.open(os.path.join(src, filename))
            width = str(ob.size[0])
            height = str(ob.size[1])
            fd.write(width + " " + height + " " + filename + " ")
            print(filename)
            # 把文件名字拆分为列表
            list01 = list(filename.split('.')[0].split('_')[1])
            for number, item in enumerate(list01):
                code = dict01[item]
                if number == len(list01) - 1:
                    fd.write(code + '\n')
                else:
                    fd.write(code + ',')

fd.close()
