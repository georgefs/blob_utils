from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import blobstore_handlers
import logging


class Upload(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        logging.info('test')
        blob_key = str(self.get_uploads('default')[0].key())
        logging.info(blob_key)
        self.response.write(blob_key)

app = webapp.WSGIApplication([
    ('.*',  Upload),
], debug=True)

if __name__ == "__main__":
    run_wsgi_app(app)
