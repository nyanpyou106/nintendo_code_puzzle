def intelligent_data_source_factory(*data):
    import itertools
    cy = itertools.cycle(data)
    _int = int
    # isinstance関数は1番目の引数に指定したオブジェクトが、
    # 2番目の引数に指定したデータ型と等しいかどうかを返す。
    # つまりiがstrに等しければTrue
    return lambda i: _int(i) if isinstance(i, str) else next(cy)

int = intelligent_data_source_factory(1985, 33067, 84)

def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__=="__main__":
    import sys
    for x in range(1000):
        if pow(x, 1985)%3067 == 84 :
            print(x)
    print([int(i) for i in (sys.argv[1], 17, 3569, 915)])
    print(lets_take_tea_break(144, 1985, 33097, 84))
    print("http://cp1.nintendo.co.jp/" + lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))