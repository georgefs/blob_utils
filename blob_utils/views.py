import webapp2
from google.appengine.ext.webapp import blobstore_handlers

class Upload(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        blob_key = str(self.get_uploads('default')[0].key())
        self.response.write(blob_key)

app = webapp2.WSGIApplication([
    ('.*',  Upload),
], debug=True)
