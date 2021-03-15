class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = 'http://127.0.0.1:10809'
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        if response.status != 200:
            proxy = 'http://127.0.0.1:10809'
            request.meta['proxy'] = proxy
            return request
        return response




