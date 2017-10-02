# coding=utf-8
import jieba
file = raw_input("請輸入演講文稿的檔案名稱(含副檔名)")
ret = open(file, "r").read()
seglist = jieba.cut(ret, cut_all=False)

import json
hash = {}
for item in seglist: 
  if item in hash:
    hash[item] += 1
  else:
    hash[item] = 1

temp = file.split('.')

json.dump(hash,open(temp[0]+"_count.json","w"))

fd = open(temp[0]+"_count.csv","w")
fd.write("word,count\n")
for k in hash:
  fd.write("%s,%d\n"%(k.encode("utf8"),hash[k]))
