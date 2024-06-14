# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CetPipeline:
    def process_item(self, item, spider):
        return item


from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class CustomFilesPipeline(FilesPipeline):

    def get_media_requests(self, item, info):

        print('get_media_requests,',item)
        url=item['file_urls']
        meta=item['filenames']
        # 这里从item中读取文件URL和文件名
        yield Request(url=url, meta={'filename': meta})

    def file_path(self, request, response=None, info=None):
        # 使用从meta中传来的文件名
        filename = request.meta['filename']
        return filename
