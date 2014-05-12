__author__ = 'apple'

import tornado.httpclient
import tornado.ioloop
import json
#remote_url = raw_input("please input request url:")
#request_method = raw_input("set the request method:")
#request_parameters = dict
base_url = "http://192.168.3.144/"
tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
proxy_config = {"proxy_host":"192.168.3.21", "proxy_port": 8888}
#has_parameters = raw_input("do you have requset parameters?y/n:")
token = ""
http_client = tornado.httpclient.AsyncHTTPClient()
command_map = {"authorize":True,"GET":True,"POST":True,"PUT":True,"DELETE":True}
#authorize = raw_input("whether need authorized(y/n)?:")
def handle_requset(resp):
	if resp.error:
		print resp.error
	else:
		response_data = json.loads(resp.body)
		response_data = response_data.encode("utf-8")
		print "the response body:"
		print "##################################"
		print json.dumps(response_data,indent=2)
		print "##################################"
	tornado.ioloop.IOLoop.instance().stop()
def handle_authorize(authorize_response):
	global token
	if authorize_response.error:
		print authorize_response.error
	else:
		response_data = json.loads(authorize_response.body)
		token = response_data.get("accesstoken",None);
		if token:
			print "Authorize success with token %s" %token
		else:
			print "Authorize fail,please retry!"
		tornado.ioloop.IOLoop.instance().stop()

def make_authorize():
	global http_client
	username = raw_input("username:")
	password = raw_input("password:")
	post_data = {"mobile": username, "password": password}
	authorize_url = base_url+"user/login"
	body = json.dumps(post_data)
	request = tornado.httpclient.HTTPRequest(authorize_url, method="POST", body=body)
	#request.proxy_host = proxy_config["proxy_host"]
	#request.proxy_port = proxy_config["proxy_port"]
	http_client.fetch(request, handle_authorize)
	tornado.ioloop.IOLoop.instance().start()

def main():
	global http_client
	print "START TEST"
	print "---------------------------------"
	while True:
		print "+++++++++++++++++++++++++++++++"
		command = raw_input("please input request method:")
		command_isVaild = command_map.get(command,False)
		if not command_isVaild:
			continue
		if command == "authorize":
			make_authorize()
		else:
			is_set_token = raw_input("is it with token(y/n)?:")
			request_url = raw_input("please input the request url:")
			body_string = raw_input("please input the body:")
			body_compenents = body_string.rsplit(',')
			post_dictionary = {}
			if len(body_string)>2:
				for compenent in body_compenents:
					key_values = compenent.split('=')
					post_dictionary[key_values[0]]=key_values[1]

			completion_url = base_url+request_url
			body = json.dumps(post_dictionary)
			request = tornado.httpclient.HTTPRequest(completion_url,method=command,body=body)
			if is_set_token.lower()=='y':
				request.headers["accesstoken"]=token
			http_client.fetch(request,handle_requset)
			tornado.ioloop.IOLoop.instance().start()



if __name__ == "__main__":
	main()
