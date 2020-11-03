# for文　
# 条件を満たしていれば、同じ処理を繰り返す。
# 条件を満たさなくなった時点で繰り返しをやめる。

# for 変数(i)　in range(繰り返す回数):
#   繰り返し中に実行する処理

for i in range(5):# [0,1,2,3,4,]のイメージ iに順番に0,1,2,3,4が代入される。
    print(i)
# 0
# 1
# 2
# 3
# 4

# ====================================================================
# break文 0
for i in range(5): #0から1ずつ実行して
    if i == 3:# 3回目が代入された時点でﾙｰﾌﾟ抜ける
        break
    print(i)
# 0
# 1
# 2

# ====================================================================
# continue文
# for i in range(5):
#   if条件
#       continue スキップ
#    print(i)

for i in range(5): # iに5回代入する
    if i == 3:# 3回目をスキップさせる。
        continue
    print(i)
# 0
# 1
# 2
# 4

#for文の中にfor文（ﾈｽﾄ）

for i in range(3):#外側　0から2まで回す
    for j in range(3): #内側　0から2まで回す
        print(i,j,sep="-")
#まず外側0番目で内側が0から3が回る。次に外側が1回目になり内側がまた0から3まで回る。
# 0-0
# 0-1
# 0-2
# 1-0
# 1-1
# 1-2
# 2-0
# 2-1
# 2-2

# 変数を使ってﾘｽﾄの中身を表示
arr = [2,4,6,8,10]
for i in arr: #inの後にﾘｽﾄを書く事で、ﾘｽﾄの中身が変数に1つすつ格納される。
    print(i)

# 変数を使って足しあげる。
arr = [2,4,6,8,10]
sum = 0 #sumの変数を定義
for i in arr:
    sum += i# ﾘｽﾄの値を複合代入演算子
    print(sum)

# i=2の時 0+2=2
# i=4   　2+4=6
# i=6   　6+6=12
# i=8   　12+8=20
# i=10 　 20+10=30
