# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class BlblPipeline:
    def process_item(self, item, spider):

        #连接本地数据库，并指定数据库名为blblspider
        db = pymysql.connect(host='localhost', user='root', password='zkw981206', db='blblspider', charset='utf8')
        cursor = db.cursor() # 获取db的游标

        # 进行数据清洗
        title = item['title'][0]
        author = item['author'][0]
        author_url = item['author_url'][0]
        time = item['time'][0]
        length = item['length'][0]
        url = item['url'][0]
        plays = int(item['plays'][0].strip('总播放数'))
        barrages = int(item['barrages'][0].strip('历史累计弹幕数'))
        likes = int(item['likes'][0].strip('点赞数'))
        description = ''.join(item['description'])
        labels_list = [label.strip('\n').strip().strip('\n') for label in item['labels']]
        labels = '/'.join(labels_list) # 把各个label连接为一个字符串
        # comments = int(item['comments'][0])
        #comments = ''

        # 对数据库进行插入操作
        cursor.execute(
            'INSERT INTO blblsearch(title, author, time, length, plays, labels, description, url, author_url, barrages, likes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (title, author, time, length, plays, labels, description, url, author_url, barrages, likes))
        
        # 对事务进行提交
        db.commit()
        
        # 关闭游标对象及数据库对象
        cursor.close()
        db.close()
        return item
