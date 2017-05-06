'''

'''
import json
import os
import pathlib
import io_functions

c_path = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('config.json')

class ConfigData():

    def __init__(self):
        '''
        '''
        self.filter_dictionary = {}
        self.readers = {}
        self.writers = {}

        with c_path.open() as conf:
            data = json.load(conf)
#            for filt in data['filters']:
#                print(filt)
#                print(data['filters'][filt])
            for rdr in data['readers']:
                self.readers[rdr] = getattr(io_functions, data['readers'][rdr])

            for wrt in data['writers']:
                self.writers[wrt] = getattr(io_functions, data['writers'][wrt])


#create a data object containing all of the config 
#file info that can be passed around through various modules. 
c_data = ConfigData()
