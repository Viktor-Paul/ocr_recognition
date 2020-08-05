
## 代码结构
```
├── data_reader.py  # 下载、读取、处理数据。
├── crnn_ctc_model.py   # 定义了OCR CTC model的网络结构。
├── attention_model.py   # 定义了OCR attention model的网络结构。
├── train.py   # 用于模型的训练。
├── infer.py   # 加载训练好的模型文件，对新数据进行预测。
├── eval.py     # 评估模型在指定数据集上的效果。
├─ utils.py    # 定义通用的函数。
├── run_crnn_ctc.sh     # 执行crnn_ctc模型训练任务
└── run_attention.sh    # 执行attention模型训练任务
└── gen_train_txt.py  #用于生成训练图片的标注文档
└── gen_test_txt.py   # 用于生成测试图片的标注文档
└── read_filename_to_filename_list.py # 读图片文件名生成测试的文件
└── dataset_gen_image.py # 用于生成自定义的验证码图片
```


## 简介

本章的任务是识别验证码中的字母和数字，字母包括大小写，这里我们分别使用CTC model和attention model两种不同的模型来完成该任务。

这两种模型的有相同的编码部分，首先采用卷积将图片转为特征图, 然后使用`im2sequence op`将特征图转为序列，通过`双向GRU`学习到序列特征。

两种模型的解码部分和使用的损失函数区别如下：

- CTC model: 训练过程选用的损失函数为CTC(Connectionist Temporal Classification) loss, 预测阶段采用的是贪婪策略和CTC解码策略。
- Attention model: 训练过程选用的是带注意力机制的解码策略和交叉信息熵损失函数，预测阶段采用的是柱搜索策略。

训练以上两种模型的评估指标为样本级别的错误率。

## 数据

数据的生成可以通过dataset_gen_image.py来实现

## 训练
具体可以参考教程：
https://blog.csdn.net/weixin_44996884/article/details/107791972
