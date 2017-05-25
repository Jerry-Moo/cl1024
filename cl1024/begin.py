#-*- coding:utf-8 -*-

from scrapy import cmdline
cmd = 'scrapy crawl cl1024 -s JOBDIR=crawls/somespider-1'
cmdline.execute(cmd.split(' '))
