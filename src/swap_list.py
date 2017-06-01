'''
@author: Alister Maguire

SwapList is a simple extension of a basic python
list which allows users to pop a random index without
the overhead generally associated with this action. 
NOTE: order is NOT maintained with swapPop. 

'''

class SwapList(list):

    def swapPop(self, idx):
        '''
           Swap the last element in this list with
           the target element to be popped, and then 
           pop of the last element. 
           
           @args: idx -> the index of the element to be
                      removed. 
                      
        '''
        end    = self[-1]        
        target = self[idx]
        self[-1]  = target
        self[idx] = end
        return self.pop()



