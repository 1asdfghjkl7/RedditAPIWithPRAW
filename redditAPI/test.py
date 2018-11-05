import falcon
from redditAPI.redditFunctions import *


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        parse = req.query_string
        if parse:
            res = parse.split("=")[1]
            back = grabapi(res)

        if not parse:
            back = grabapi()

        resp.media = back


api = falcon.API()
api.add_route('/quote', QuoteResource())
