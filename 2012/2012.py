from second_code import SimpleBars
bs = SimpleBars(" "*24)
bs[8] = "T"
for i in range(30):
    print(bs.next())
    #bs.next()を実行するとbs(リスト)が書き変わる