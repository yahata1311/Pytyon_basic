# def 関数名(引数)：/(引数1,引数2）で複数することも可能
#   実行する処理

# 引数なしの場合
def say_hello():
    print("hello world")
say_hello()
# hello world

# 引数ありの場合 引数名をgreetingにしてみる。なんでもOK。
def say_hello(greeting):
    print(greeting)
say_hello("hello world")
# hello world


def say_hello(greeting):
    print(greeting)
hello=say_hello
hello("Good Morning")
# Good Morning

# 引数を2つ使う　（printﾊﾞｰｼﾞｮﾝ）
def add(num01,num02):
    print(num01 + num02)  # 8が出力される。
add(6,2)
# 8

# 引数を2つ使う　（returnﾊﾞｰｼﾞｮﾝ）
def add(num01,num02):
   return (num01 + num02)  #returnの場合は出力されるが、目視で確認できない。
add_result=add(6,2) #目視で確認できない為、add_resultという変数に代入して表示してみる。
print(add_result)
# 8

# 練習問題
# 3つの引数を受け取る関数を作る　9，4，2の平均を出す
def add(num01,num02,num03):
    print ((num01 + num02 + num03)/3)
add(9,4,2)
# 5　正解！！



