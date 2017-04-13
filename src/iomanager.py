'''
@author: Alister Maguire
create: Thu Apr 13 15:21:27 PDT 2017

IOManager is an object to handle IO for the Team Builder. 
As of now, the manager accepts csv files as input. Ideally, 
this module will allow for developers to easily extend the
types of input and output data used within the Team Builder. 


'''

class IOManager(Object):
'''
    A manager for handling IO for Team Builder. 
'''

    def __init__(self, in_type, out_type):
        '''
            Initialize the manager with an in type and an out type. 

            @param: 
                in_type: the type of input to be handled
                out_type: the type of output to be created
        '''
       
        #TODO: we can scrap these lists and just use the 
        #      keys to the dictionaries below for checking.   
        self.__accepted_in  = ['csv']
        self.__accepted_out = ['txt']
       
        if (in_type not in self.__accepted_in or
            out_type not in self.__accepted_out):
            print("ERROR: invalid in or out types declared...")
            print("The following types are currently accepted:")
            print("in: ", end='') 
            for t in self.__accepted_in:
                print(t, " ")
            print("out: ", end='') 
            for t in self.__accepted_out:
                print(t, " ")
            return None

        self.__in_type  = in_type
        self.__out_type = out_type
        self.__readers  = {'csv' : self.csvReader}
        self.__writers  = {'txt' : self.txtWriter}


    def read(self, path):
        #TODO: finish the return value
        '''
            Select the appropriate reader to read a
            file for data collection.  

            @param:
                path: the path to the input file. 
            @returns:
                
        '''
        return self.__readers[self.__in_type](path)

    def csvReader(self, path):
        pass

    def txtWriter(self, path):
        pass







    
