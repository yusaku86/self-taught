import re
text = """キリンは大昔から __複数名詞__ の興味の対象でした。
キリンは __複数名詞__ の中で一番背が高いですが、科学者たちは
そのような長い __体の一部__ をどうやって獲得したのか説明でき
ません。キリンの身長は __数値__ __単位__ あり、その高さのほ
とんどは脚と __体の一部__ によるものです。
"""

def mad_libs(mls):
    hints = re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q ="{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
            mls = mls.replace("\n","")
        print('\n')
        mls = mls.replace(" ","",1)
        print(mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)