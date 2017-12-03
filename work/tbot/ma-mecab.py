import MeCab

mecab = MeCab.Tagger("-Ochasen") #MeCabオブジェクトを生成
malist = mecab.parse("庭には２羽鶏がいる。") #形態解析を行う
print(malist)
