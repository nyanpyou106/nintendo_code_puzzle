class SimpleBars(list):
    def next(self):
        next_bar = [" " for i in range(len(self))]
        for index in range(len(self)):
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

        self.clear()
        self.extend(next_bar)
        return "".join(self)