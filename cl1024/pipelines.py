# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy import log

class Cl1024Pipeline(object):
    def process_item(self, item, spider):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='wuchujie', charset='utf8', db='cl1024')
        cur = conn.cursor()
        sql = 'insert into cl1024_torrent(cl_name, cl_url, cl_bankuai, posted, torrent_url, torrent_downloaded, torrent_download_urls) values(%s, %s, %s, %s, %s, %s, %s)'
        keys = ['cl_title', 'cl_url', 'cl_bankuai', 'posted', 'torrent_url', 'torrent_downloaded', 'torrent_download_urls']
        # for i in item.keys():
        #     try:
        #         item[i] = str(item.get(i).encode('utf-8'))
        #     except:
        #         item[i] = str(item.get(i))
        #     finally:
        #         pass
        values = [item.get(x) for x in keys]
        try:
            cur.execute(sql, values)
        except MySQLdb.IntegrityError:
            pass
        conn.commit()
        cur.close()
        conn.close()
        return item
