# 【10.条件分岐　】
# 条件に一致する場合は処理A、一致しない場案は処理Bにする。等
# if文の書き方

# if 条件 :
#   条件を満たしたときの処理

# 例変数age 条件20才以上。YESならadult NOnならchildを表示

age = 22
if age >= 20:
    print("adult") #adult

age = 18

if age >= 20:
    print("adult") #条件を満たさないので、何も表示されない。

# ===============================================================
# if else文

# if 条件 :
#   条件を満たしたときの処理
# else:
#   条件を満たさない時の処理

age = 18

if age >= 20:
    print("adult")
else:
    print("child")

# 18は20才以下の為、childが出力される。

# ===============================================================
# if elif文

# if 条件A :
#   条件を満たしたときの処理
# elif 条件B:
#   条件Bを満たした時の処理
# else:
#   条件を満たさない時の処理A


age = 0

if age >= 20: # 20才以上ならadultと出力
    print("adult")
elif age == 0: # 0才ならbabyと出力
    print("baby")
else: # 両方の条件に一致しないなら、Childと出力
    print("child")
# 0才の為、babyと出力された。

age = 22

if age >= 20: # 20才以上ならadultと出力
    print("adult")
elif age == 0: # 0才ならbabyと出力
    print("baby")
else: # 両方の条件に一致しないなら、Childと出力
    print("child")
# 22才の為、adultと出力された。
