import falcon

class HelloResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("DevOpsing_Like_There_Is_No_Tomorrow!")

class Page2Resource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("Bruh!")

app = falcon.API()

hello = HelloResource()

page2 = Page2Resource()

app.add_route('/', hello)
app.add_route('/page2', page2)
