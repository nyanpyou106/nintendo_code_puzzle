class SimpleBars(list):

    # indexがリストの左端と右端を示した時の処理を入れておく必要がある
    # 入れないとlist index out of rangeでエラー
    def left(self, index):
        if index==0:
            left = self[-1]    
        else:
            left = self[index-1]
        return left

    def right(self, index):
        if index==len(self)-1:
            right = self[0]
        else:
            right = self[index+1]
        return right

    def next(self):
        next_bar = [" " for i in range(len(self))]
        for index, _ in enumerate(self):
            if self[index] == "T":
                if ((self.left(index)=="i") & (self.right(index)=="i")):
                        next_bar[index] = "i"
                elif (self.left(index)=="i"):
                    next_bar[index] = " "
                elif (self.right(index)=="i"):
                    next_bar[index] = " "
                else:
                    next_bar[index] = "i"
            elif self[index] == " ":
                if ((self.left(index)=="i") & (self.right(index)=="i")):
                    next_bar[index] = " "
                elif (self.left(index)=="i"):
                    next_bar[index] = "i"
                elif (self.right(index)=="i"):
                    next_bar[index] = "i"
                else:
                    next_bar[index] = " "
            elif self[index] == "i":
                next_bar[index] = "T"

        self.clear()
        self.extend(next_bar)
        return "".join(self)
    
    def __str__(self):
        return "".join(self)