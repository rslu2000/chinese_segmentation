#coding=utf-8

#python3
import jieba
import jieba.analyse
import sys
sys.path.append('./')
#jieba.analyse.set_stop_words("./stop_words.txt")
file = input("請輸入演講文稿的檔案名稱(含副檔名)")
content = open(file, "r").read()

jieba.analyse.set_stop_words('stop_words.txt')
tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
for item in tags:
    print(item[0]+'\t'+str(int(item[1]*1000)))

