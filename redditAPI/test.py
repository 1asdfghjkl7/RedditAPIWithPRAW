import falcon
from redditAPI.redditFunctions import *


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        if req.get_param("q"):
            res = req.get_param("q")
            back = grabapi(res)
        elif req.get_param("tag"):
            res = req.get_param("tag")
            back = grabapi(res)
        else:
            back = grabapi()

        resp.media = back


api = falcon.API()
api.add_route('/quote', QuoteResource())
