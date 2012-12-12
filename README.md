scrapy-simple-http-queue
========================

Scrapy Plugin to use the simple http queue as the queue for the URLs in order to allow distributed crawling.

First run simple-http-queue:
cd externals/simple-http-queue/simple_http_queue
python HttpQueue.py /tmp/queue.dat 8888

Example: run_example.sh

In settings.py:
HTTP_HOST
HTTP_PORT
SCHEDULER_PERSIST
SCHEDULER_QUEUE_NAME (optional, will be the name of the spider if not specified)
