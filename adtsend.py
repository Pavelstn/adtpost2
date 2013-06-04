#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import hmac

class Adtsend:
	def __init__(self):
		self.token= "*************"
		self.url= "***************"
		#

	def send_post(self, post):
		sendpost={
			"user_id":"1",
			"request":"save_post",
			"postdata":post,
		}
		serial_data= self.to_serial(sendpost)
		response= self.send_json(self.url, self.sign_data(sendpost, serial_data, self.token))
		if 201== response.getcode():
			result = json.load(response)
			return result["id"]
		else:
			return 0

	def send_image(self, post_id, umg_url):
		image={
			"post_id":post_id,
			"url":umg_url,
			}
		senddata={
			"user_id":'1',
			"request":"save_image",
			"postdata":image,
			}
		serial_data= self.to_serial(senddata)
		response= self.send_json(self.url, self.sign_data(senddata, serial_data, self.token))
		if 201== response.getcode():
			result = json.load(response)
			return result["id"]
		else:
			return 0

	#######private####
	def to_serial(self,sendpost):
		string= "user_id_"+str(sendpost["user_id"])
		string= string+ "_request_"+sendpost["request"]
		postdata= sendpost["postdata"]
		postdata= sorted(postdata.iteritems())
		string= string+  "".join("_%s_%s" % tup for tup in postdata)
		#print string
		return string

	def send_json(self,url, sign_data):
		headers = {"Content-Type": "application/json", "Accept": "*/*"}
		req = urllib2.Request(url,headers=headers, data= json.dumps(sign_data))
		response=urllib2.urlopen(req)
		return response

	def sign_data(self,send_data, plain_data, token):
		sign = hmac.new(token, plain_data).hexdigest()
		#print sign
		sign_data={
					"data":{
							"send_data":send_data,
							"sign":sign
							}
					}
		return sign_data

