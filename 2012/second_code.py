class SimpleBars(list):
    def next(self):
        next_bar = [" " for i in range(len(self))]
        for index, _ in enumerate(self):
            if self[index] == "T":
                if index == len(self)-1:
                    if ((self[index-1]=="i") & (self[index]=="T")):
                        next_bar[index] = " "
                    elif (self[index]=="T"):
                        next_bar[index] = "i"
                else:
                    if ((self[index-1]=="i") & (self[index]=="T") & (self[index+1]=="i")):
                            next_bar[index] = "i"
                    elif ((self[index-1]=="i") & (self[index]=="T")):
                        next_bar[index] = " "
                    elif ((self[index]=="T") & (self[index+1]=="i")):
                        next_bar[index] = " "
                    elif (self[index]=="T"):
                        next_bar[index] = "i"
            elif self[index] == " ":
                if index == len(self)-1:
                    if ((self[index-1]=="i") & (self[index]==" ")):
                        next_bar[index] = "i"
                    elif (self[index]==" "):
                        next_bar[index] = " "
                else:
                    if ((self[index-1]=="i") & (self[index]==" ") & (self[index+1]=="i")):
                        next_bar[index] = " "
                    elif ((self[index-1]=="i") & (self[index]==" ")):
                        next_bar[index] = "i"
                    elif ((self[index]==" ") & (self[index+1]=="i")):
                        next_bar[index] = "i"
                    elif (self[index]==" "):
                        next_bar[index] = " "
            elif self[index] == "i":
                next_bar[index] = "T"
            
            if ((self[0]=="i") & (self[-1]=="T")):
                next_bar[0]="T"
                next_bar[-1]=" "
            if ((self[0]=="i") & (self[1]=="T")):
                next_bar[0]="T"
                next_bar[-1]="i"

        self.clear()
        self.extend(next_bar)
        return "".join(self)
    
    def __str__(self):
        return "".join(self)