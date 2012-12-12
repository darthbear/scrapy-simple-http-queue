from simple_http_queue.Client import Client
from scrapy.utils.reqser import request_to_dict, request_from_dict
import marshal

# default values
HTTP_HOST = 'localhost'
HTTP_PORT = 8888
SCHEDULER_PERSIST = True

class Scheduler(object):
    def __init__(self, host, port, persist, queue_key):
        self.host = host
        self.port = port
        self.queue_key = queue_key
	self.persist = persist

    def __len__(self):
        return self.client.size()

    @classmethod
    def from_crawler(cls, crawler):
	settings = crawler.settings
        host = settings.get('HTTP_HOST', HTTP_HOST)
        port = settings.get('HTTP_PORT', HTTP_PORT)
        persist = settings.get('SCHEDULER_PERSIST', SCHEDULER_PERSIST)
        queue_key = settings.get('SCHEDULER_QUEUE_NAME', None)
        return cls(host, port, persist, queue_key)

    def open(self, spider):
        self.spider = spider
	if self.queue_key is None:
	    self.queue_key = spider.name
	self.client = Client(self.host, self.port, self.queue_key)
        # notice if there are requests already in the queue
	size = self.client.size()
        if size > 0:
            spider.log("Resuming crawl (%d requests scheduled)" % size)

    def close(self, reason):
        if not self.persist:
            self.client.drop()

    def enqueue_request(self, request):
	data = marshal.dumps(request_to_dict(request, self.spider))
        self.client.push(data)

    def next_request(self):
	data = self.client.pop()
	if data is None or len(data) == 0:
	    return None
	
	request = request_from_dict(marshal.loads(data), self.spider)
        return request

    def has_pending_requests(self):
        return self.client.size() > 0
