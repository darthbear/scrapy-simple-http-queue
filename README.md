scrapy-simple-http-queue
========================

Scrapy Plugin to use the simple http queue as the queue for the URLs in order to allow distributed crawling.

First run simple-http-queue:
cd externals/simple-http-queue/simple\_http\_queue
python HttpQueue.py /tmp/queue.dat 8888

Example: run\_example.sh

In settings.py:
HTTP\_HOST (default is localhost)
HTTP\_PORT (default is 8888)
SCHEDULER\_PERSIST (default is True)
SCHEDULER\_QUEUE\_NAME (default is the name of the spider)
