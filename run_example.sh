#!/bin/sh

export PYTHONPATH=$PYTHONPATH:$PWD:$PWD/externals/simple-http-queue
(cd example-project; scrapy crawl dealsplus)
