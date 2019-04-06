import urllib2
#note : urllib is urllib2 when in linux

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
