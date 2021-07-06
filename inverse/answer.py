from second_code import Bars
from third_code import decode_morse

# HINTを見ると恐らく.next()を連発すると循環するので、
# 適当な数.next()を繰り返して循環する直前のbarを取り出す。
bs = Bars("ITT TI I T TIii")
previous_bar = ""
last_bar = ""
for i in range(1000):
    previous_bar = str(bs)
    now_bar = str(bs.next())
    if now_bar=="ITT TI I T TIii":
        print("HIT!")
        print("previous_bar is ")
        print(previous_bar)
        last_bar = previous_bar

print(decode_morse(last_bar))