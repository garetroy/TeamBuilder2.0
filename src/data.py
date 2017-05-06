'''

'''
import json
import os
import pathlib

#TODO: is this really necessary?
c_path = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('config.json')


#TODO: lets make a better name for this class
class Data():

    def __init__(self):
        '''
        '''
        self.__filter_dictionary = {}
        with c_path.open() as conf:
            data = json.load(conf)
            for filt in data['filters']:
#                self.__filter_dictionary[ 
                print(filt)
                print(data['filters'][filt])


d = Data()
