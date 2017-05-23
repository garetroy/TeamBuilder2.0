



class SwapList(list):

    def swapPop(self, idx):
        end    = self[-1]        
        target = self[idx]
        self[-1]  = target
        self[idx] = end
        return self.pop()



