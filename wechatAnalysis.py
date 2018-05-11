import itchat
import re
import os
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import numpy as np

itchat.auto_login(hotReload=True)

#itchat.send('Hello, filehelper', toUserName='filehelper')

friends = itchat.get_friends()
print(friends)


# tList = []
# for i in friends:
#     signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "").replace("<","").replace(">","").replace("\"","").replace("/","")
#     rep = re.compile("1f\d.+")
#     signature = rep.sub("", signature)
#     print(signature)
#     tList.append(signature)

# # 拼接字符串
# text = "".join(tList)

# # print(text)
# # jieba分词
# wordlist_jieba = jieba.cut(text, cut_all=True)
# wl_space_split = " ".join(wordlist_jieba)

# #print(wl_space_split)

# # my_wordcloud = WordCloud(background_color="white", max_words=2000, 
# #                          max_font_size=40, random_state=42,
# #                          font_path='C:\Windows\Fonts\AdobeHeitiStd-Regular.otf').generate(wl_space_split)

# # plt.imshow(my_wordcloud)
# # plt.axis("off")
# # plt.show()



# d = os.path.dirname(__file__)
# alice_coloring = np.array(Image.open(os.path.join(d, "weixin2.jpg")))
# my_wordcloud = WordCloud(background_color="white", max_words=3000, mask=alice_coloring,
#                          max_font_size=60, random_state=42,
#                          font_path='C:\Windows\Fonts\AdobeHeitiStd-Regular.otf').generate(wl_space_split)

# image_colors = ImageColorGenerator(alice_coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()

# # 保存图片 并发送到手机
# my_wordcloud.to_file(os.path.join(d, "wechat_cloud6.png"))
# itchat.send_image("wechat_cloud6.png", 'filehelper')


# # 初始化计数器，有男有女，当然，有些人是不填的
# male = female = other = 0

# # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# # 1表示男性，2女性
# for i in friends[1:]:
#     sex = i["Sex"]
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other += 1

# # 总数算上，好计算比例啊～
# total = len(friends[1:])

# print(total)

# # 好了，打印结果
# print(u"男性好友：%.2f%%" % (float(male) / total * 100))
# print(u"女性好友：%.2f%%" % (float(female) / total * 100))
# print(u"其他：%.2f%%" % (float(other) / total * 100))