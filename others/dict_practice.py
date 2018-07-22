
# coding: utf-8

# In[27]:


# 元データ
ramen = ["醤油", "味噌", "とんこつ", "塩"]
pasta = ["ナポリタン", "ミートソース", "カルボナーラ", "ペペロンチーノ"]
mydict = {"000101" : ramen, "000102" : pasta}

# 検索ワードを指定
search_word = "とんこつ"

# 検索ワードの入ってるKeyをとってくる
for item in mydict.items():
    if search_word in item[1] :
        print(item[0])
        search_key = item[0]

# 検索ワードと一緒に入ってるlistの文字列たちをとってくる
tmp_list = mydict[search_key]
output_list = [i for i in tmp_list if i != search_word]
for output_item in output_list :
    print(output_item)

