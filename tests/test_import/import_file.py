import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options

from source.Tree import Tree

define("port", default=8888, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("upload.html")

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        file_request = self.request.files['file1'][0]
        original_fname = file_request['filename']

        tree = Tree('/run/media/tay/Wester_Disk/west/projects/Tree/import_file/')
        tree.insert(file_request['body'])
        
        self.finish("file" + original_fname + " is uploaded")

def main():
    app = tornado.web.Application(handlers=[
            (r"/", IndexHandler),
            (r"/upload", UploadHandler)
        ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
