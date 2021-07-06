class SimpleBars(list):
    def next(self):
        next_bar = [" " for i in range(len(self))]
        index = 0
        while index<len(self):
            """
            if ((index-1>=0) & (index+1<len(self))):
                if ((self[index-1]=="i") & (self[index]=="T") & (self[index+1]=="i")):
                    next_bar[index] = "i"
                elif ((self[index-1]=="i") & (self[index]=="T")):
                    next_bar[index] = " "
                elif ((self[index]=="T") & (self[index+1]=="i")):
                    next_bar[index] = " "
                elif (self[index]=="T"):
                    next_bar[index] = "i"
                
                if ((self[index-1]=="i") & (self[index]==" ") & (self[index+1]=="i")):
                    next_bar[index] = " "
                elif ((self[index-1]=="i") & (self[index]==" ")):
                    next_bar[index] = "i"
                elif ((self[index]==" ") & (self[index+1]=="i")):
                    next_bar[index] = "i"
                elif (self[index]==" "):
                    next_bar[index] = " "

                if self[index]=="i":
                    next_bar[index] = "T"
            """
            if (self[index]=="T"):
                next_bar[index] = "i"
            if (self[index]==" "):
                next_bar[index] = " "
            if self[index]=="i":
                next_bar[index] = "T"

            if index-1<0:
                if ((self[index]==" ") & (self[index+1]=="i")):
                    next_bar[index] = "i"
                if ((self[index]=="T") & (self[index+1]=="i")):
                    next_bar[index] = " "
            elif index+1>len(self)-1:
                if ((self[index-1]=="i") & (self[index]==" ")):
                    next_bar[index] = "i"
                if ((self[index-1]=="i") & (self[index]=="T")):
                    next_bar[index] = " "
            else:
                if ((self[index]==" ") & (self[index+1]=="i")):
                    next_bar[index] = "i"
                if ((self[index-1]=="i") & (self[index]==" ")):
                    next_bar[index] = "i"
                if ((self[index-1]=="i") & (self[index]==" ") & (self[index+1]=="i")):
                    next_bar[index] = " "
                if ((self[index]=="T") & (self[index+1]=="i")):
                    next_bar[index] = " "
                if ((self[index-1]=="i") & (self[index]=="T")):
                    next_bar[index] = " "
                if ((self[index-1]=="i") & (self[index]=="T") & (self[index+1]=="i")):
                    next_bar[index] = "i"
            
            index+=1

        self.clear()
        self.extend(next_bar)
        return "".join(self)

        # next_bar[0]が!=" "の時にloop処理を入れる？
    
    def __str__(self):
        return "".join(self)