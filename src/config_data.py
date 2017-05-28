'''
@author: Alister Maguire
date: Sat May  6 11:25:50 PDT 2017

This file contains a ConfigData object which 
reads in data fron the config.json file and 
stores this data such that modules within 
TeamBuilder an access it when needed. 

'''

import os
import sys

#grab the path to the config folder
curpth    = os.path.dirname(os.path.abspath(__file__))
targetpth = curpth + '/../config/'
sys.path.insert(0, targetpth)

import json
import pathlib
import io_functions
import filters

c_path = pathlib.Path(os.path.realpath(__file__)).parent.joinpath('../config/config.json')

class ConfigData():

    def __init__(self):
        '''
        '''
        self.filter_dictionary = {}
        self.readers = {}
        self.writers = {}
        self.email = {}
        self.defaults = {}

        with c_path.open() as conf:
            data = json.load(conf)

            #check to make sure that the weights are appropriately 
            #set while setting filters. 
            filter_count = 0
            total_weight = 0.0
            for filt in data['filters']:
                filter_count += 1
                total_weight += float(data['filters'][filt][2])
                self.filter_dictionary[filt] = [getattr(filters, data['filters'][filt][0]), 
                     data['filters'][filt][1],
                     float(data['filters'][filt][2])]

            if filter_count != int(total_weight):
                print("ERROR: the filter weights are not appropriately set!")
                print("Refer to the manual if you do not know how to set the weights")
                sys.exit(1)

            for rdr in data['readers']:
                self.readers[rdr] = getattr(io_functions, data['readers'][rdr])

            for wrt in data['writers']:
                self.writers[wrt] = getattr(io_functions, data['writers'][wrt])

            for entry in data['email']:
                self.email[entry] = data['email'][entry]

            self.defaults = data['defaults']

            if (self.defaults['rdr'] not in data['readers'] or
                self.defaults['wrtr'] not in data['writers']):
                print("ERROR: invalid in or out types declared...")
                print("The following types are currently accepted:")
                print("in: ", end='') 
                for t in data['readers']:
                    print(t, " ")
                print("out: ", end='') 
                for t in data['writers']:
                    print(t, " ")
                return None


#test = ConfigData()

