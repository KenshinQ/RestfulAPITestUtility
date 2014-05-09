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
authorize = raw_input("whether need authorized(y/n)?")
def handle_requset(resp):
	if resp.error:
		print resp.error
	else:
		response_data = json.loads(resp.body)
		print json.dumps(response_data,indent=2)
	tornado.ioloop.IOLoop.instance().stop()
def handle_authorize(authorize_response):
	global token
	if authorize_response.error:
		print authorize_response.error
	else:
		response_data = json.loads(authorize_response.body)
		token = response_data["accesstoken"];
		print "Authorize success"

def make_authorize:
	username = raw_input("username:")
	password = raw_input("password:")
	post_data = {"mobile": username, "password": password}
	body = json.dumps(post_data)
	request = tornado.httpclient.HTTPRequest(base_url, method="POST", body=body)
	request.proxy_host = proxy_config["proxy_host"]
	request.proxy_port = proxy_config["proxy_port"]

if authorize == 'y':




	if isinstance(http_client,tornado.httpclient.AsyncHTTPClient):
		http_client.fetch(request, handle_requset, **proxy_config)
		tornado.ioloop.IOLoop.instance().start()