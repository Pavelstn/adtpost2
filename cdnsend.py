#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import cloudfiles

class Cdnsend:
    def __init__(self):
        self.username = '*******'
        self.apikey = '******'
        self.authurl= '******'
        
    def sendImage(self,filename):
        fname=os.path.split(filename)[1]
        conn = cloudfiles.get_connection(self.username, self.apikey,servicenet = False,authurl = self.authurl,timeout = 15)
        container= conn.get_container('public')
        my_dog = container.create_object('***/*****/'+fname)
        my_dog.load_from_filename(filename)
        print "OK"
        #print my_dog
        return "http://******************************"+my_dog.name