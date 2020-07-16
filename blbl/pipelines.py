# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter


class BlblPipeline:
    def __init__(self):
        self.fp = open("blbldata.json",'wb')
        self.exporters = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        self.exporters.start_exporting()

    def open_spider(self,spider):
        print("爬虫开始了")

    def process_item(self, item, spider):
        self.exporters.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporters.finish_exporting()
        self.fp.close()
        print("爬虫结束了")