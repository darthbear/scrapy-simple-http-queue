scrapy-simple-http-queue
========================

Scrapy Plugin to use the simple http queue as the queue for the URLs in order to allow distributed crawling.

First run simple-http-queue:

	cd externals/simple-http-queue/simple_http_queue
	python HttpQueue.py /tmp/queue.dat 8888

Example: `run_example.sh`

In settings.py:

	HTTP_HOST (default is localhost)
	HTTP_PORT (default is 8888)
	SCHEDULER_PERSIST (default is True)
	SCHEDULER_QUEUE_NAME (default is the name of the spider)
	QUEUE_TYPE: FIFO (default) or LIFO

Use FIFO if you want to do a breadth-first crawling.
Use LIFO if you want to do a depth-first crawling.

LIFO will consume less memory as it will need less elements in the queue.
