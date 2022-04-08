import falcon

class HelloResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("DevOPSing So Hard BruH!")

class Page2Resource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ("SSS-SSS")

app = falcon.API()

hello = HelloResource()

page2 = Page2Resource()

app.add_route('/', hello)
app.add_route('/sss-sss', page2)