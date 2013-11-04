from google.appengine.ext import blobstore
from google.appengine.api import urlfetch
import urlparse
import re

__all__ = ['file_upload', 'url_upload']

def file_upload(file_name, file_content, content_type=False):
    from file_post import post_multipart
    upload_url = blobstore.create_upload_url('/blob_upload/')
    urlinfo = urlparse.urlparse(upload_url)
    path = urlinfo.path
    hostname = urlinfo.hostname
    scheme = urlinfo.scheme
    
    url = hostname
    
    files = [("default", file_name, file_content, content_type)]
    blob_key = post_multipart(url, path, {}, files)
    return blobstore.BlobInfo.get(blob_key)


def url_upload(url):
    f = urlfetch.fetch(url)   
    content_type = f.headers['content-type']
    file_name = "default"
    file_content = f.content
    return file_upload(file_name, file_content, content_type)
