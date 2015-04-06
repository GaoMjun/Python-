
import tornado.httpclient

def fetch(url):
    http_header = {'User-Agent':'Chrome'}
    http_request = tornado.httpclient.HTTPRequest(url = url, method = 'GET', headers = http_header, connect_timeout = 20)

    http_client = tornado.httpclient.HTTPClient()
    http_response = http_client.fetch(http_request)
    print http_response.code

    all_fileds = http_response.headers.get_all()
    for filed in all_fileds:
        print filed

    print http_response.body

if __name__ == '__main__':
    fetch('http://www.baidu.com')