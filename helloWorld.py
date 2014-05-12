__author__ = 'apple'

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

	def get(self, *args, **kwargs):
		print(self.request)
		#self.write("hello,world\n")
		#self.set_status(1000, "this not")
		self.write_error(1000,"this not")
	#def post(self, *args, **kwargs):
		#print(self.request)
application = tornado.web.Application([(r"/", MainHandler)])

if "__main__" == __name__:
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()





