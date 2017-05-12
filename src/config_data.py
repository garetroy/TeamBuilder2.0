'''
@author: Alister Maguire
date: Sat May  6 11:25:50 PDT 2017

This file contains a ConfigData object which 
reads in data fron the config.json file and 
stores this data such that modules within 
TeamBuilder an access it when needed. 

'''
import json
import os
import pathlib
import io_functions
import filters

c_path = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('config.json')

class ConfigData():

    def __init__(self):
        '''
        '''
        self.filter_dictionary = {}
        self.readers = {}
        self.writers = {}
        self.email = {}

        with c_path.open() as conf:
            data = json.load(conf)
            for filt in data['filters']:
                self.filter_dictionary[filt] = [getattr(filters, data['filters'][filt][0]), 
                     data['filters'][filt][1],
                     data['filters'][filt][2]]

            for rdr in data['readers']:
                self.readers[rdr] = getattr(io_functions, data['readers'][rdr])

            for wrt in data['writers']:
                self.writers[wrt] = getattr(io_functions, data['writers'][wrt])

            for entry in data['email']:
                self.email[entry] = data['email'][entry]


#test = ConfigData()

