#　クラスとはﾃﾞｰﾀと処理をまとめたもの
# アトリビュート・・・ﾃﾞｰﾀの事
# メソッド・・・処理の事
# アトリビュートはクラス内で定義された変数の事
# アトリビュートは変数と同じように代入したり、参したりできる。
# 変数はクラスの外にある。
# アトリビュートはクラスの中にある。
# ﾒｿｯﾄﾞ
# 関数＝処理
# ﾒｿｯﾄﾞ＝処理
# 関数はクラスの外
# ﾒｿｯﾄﾞはクラスの中
# ﾒｿｯﾄﾞも関数と同じdef で作(る。
# =======================================================--
class Student:
# ﾒｿｯﾄﾞの場合必ず引数が必要。通常はselfと書く。
    def avg(self):
        print((80 + 70)/2)
# クラスからつくられたｲﾝｽﾀﾝｽを変数に代入する必要がある。
# クラスはｲﾝｽﾀﾝｽになって初めて使える。
a001 = Student()# a学級の1番の生徒とする。
a001.avg()#ﾒｿｯﾄﾞの実行

# ================================================================-
class Student:
# ﾒｿｯﾄﾞの場合必ず引数が必要。通常はselfと書く。
# 生徒が変わるごとに書き換えが必要な為、引数を渡す。書き換えが不要になる。
# 例えば、math,englishを使う
    def avg(self,math,english):
        print((math + english)/2)
a001 = Student()
a001.avg(80,70)

a001.name = "sato" #アトリビュート　（クラスに定義された変数）
print(a001.name)

# =====================================================================-
class Student:
    def __init__(self):#ｺﾝｽﾄﾗｸﾀ
        self.name = "" #""で空　初期化　#ｱﾄﾘﾋﾞｭｰﾄ(初期化ﾒｿｯﾄﾞ）

    def avg(self,math,english): # ﾒｿｯﾄﾞ
        print((math + english)/2)
a001 = Student() #001=ｲﾝｽﾗﾝｽ　student()=クラス
a001.name = "sato" #アトリビュート　（クラスに定義された変数）
print(a001.name)

a002 = Student()
a002.name = "tanaka"
print(a002.name)

# ====================================================================-
class Student:
    def __init__(self,name):#第二関数のnameが
        self.name = name# 初期化ﾒｿｯﾄﾞ内のnameが受けてself.nameに代入する

    def avg(self,math,english):
        print((math + english)/2)

a001 = Student("sato")
print(a001.name)

a002 = Student("tanaka")
print(a002.name)

