import re
import os
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import numpy as np

wordStr = ["永远奋斗树的命运有风决定人的命运有自己手里路是创造路机会",
"泛舟沧海，立马昆仑。",
"不要用形容词形容我",
"每个人都是生活的导演",
"一半在尘土里安详，一半在风里飞扬，一半洒落阴凉，一半沐浴阳光",
"被信任是一种快乐:)",
"输了就是赢了，赢了就是输了。",
"自律带来自由",
"寻找迷失的方向",
"永远奋斗，树的命运有风决定，人的命运有自己手里路是创造路机会",
"三分天注定，七分靠大饼",
"冷冷清清的风风火火。",
"让生命活得更精彩......",
"褫其华衮，示人本相！",
"Inmethetigersniffstherose.",
"天地不仁，以万物为刍狗。",
"请相信，这个世界上真的有人过着你想过的生活",
"23的你25的我=\"2764\"/",
"瀑布的水逆流而上，蒲公英种子从远处飘回，聚成伞的模样"]

words = []

for i in wordStr:
    temp = i.replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "").replace("<","").replace(">","").replace("\"","").replace("/","")
    words.append(temp)

# 拼接字符串
text = "".join(words)
print(text)
# jieba分词
wordlist_jieba = jieba.cut(text, cut_all=True)

wl_space_split = " ".join(wordlist_jieba)
print(wl_space_split)
