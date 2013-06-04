#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, filecmp
import Image
import sys

class Imageresize:
    def __init__(self):
        self.bigimage_name=""
        self.smallimage_name=""
        self.img_name=""
        
    def processimage(self,filename, newfilepath):
        fname=os.path.split(filename)[1].encode("UTF-8")
    
        print fname
        img = Image.open(filename)
        bigimage = img.resize((620, 465), Image.BICUBIC)
        smallimage = img.resize((140, 130), Image.BICUBIC)
        
        self.bigimage_name=newfilepath+"/620x400_"+fname
        self.smallimage_name=newfilepath+"/140x130_"+fname
        self.img_name=newfilepath+"/original_"+fname
        
        bigimage.save(self.bigimage_name.encode("UTF-8"))
        smallimage.save(self.smallimage_name.encode("UTF-8"))
        img.save(self.img_name.encode("UTF-8"))
    

        