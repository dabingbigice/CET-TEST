import scrapy

import time

class CetSpiderSpider(scrapy.Spider):
    name = "cet-spider"
    allowed_domains = ["pan.uvooc.com","uvooc-my.sharepoint.cn"]
    def start_requests(self):
        url = 'https://pan.uvooc.com/api/fs/list'

        data = {
            'page': '1',
            'password': "",
            'path': '/Learn/CET/CET4',
            'per_page': '30',
            'refresh': 'false'
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self,response):
        data = response.json()
        content_list=data['data']['content']
        list_name = []
        for i in content_list:
            name =i['name']
            list_name.append(name)
        # 再次发送请求
        list_next_name=[]
        for j in list_name:
            data_name = {
                'page': '1',
                'password': "",
                'path': '/Learn/CET/CET4/'+j,
                'per_page': '30',
                'refresh': 'false'
            }
            list_next_name.append(data_name['path'])
            # url = 'https://pan.uvooc.com/api/fs/list'
            # custom_info = {'path':data_name['path']}
            # yield scrapy.FormRequest(url=url,formdata=data_name,callback=self.parse_threed,dont_filter=True
            #                          ,  meta={'custom_info': custom_info},  # 使用 meta 字典传递自定义参数
            #  )
        # print(list_next_name)

        paths = list_next_name[1:]
        print('paths = ', paths)
        for p in paths:
            data_next_name = {
                'page': '1',
                'password': "",
                'path': p,
                'per_page': '30',
                'refresh': 'false'
            }

            time.sleep(0.1)  # 程序将在这里暂停5秒
            url = 'https://pan.uvooc.com/api/fs/list'
            print('parse_second_path',data_next_name['path'])
            yield scrapy.FormRequest(url=url,formdata=data_next_name,callback=self.parse_four,dont_filter=True
                                     ,  meta={'custom_info': data_next_name['path']},  # 使用 meta 字典传递自定义参数
             )


    def parse_four(self, response):
        # print('parse_four')
        # print(response.json())
        path = response.meta['custom_info']

        data = response.json()
        # 筛选年龄大于 28 岁的用户
        content_list = data['data']['content']
        list_name = []
        for i in content_list:
            name = i['name']
            list_name.append(name)
        url_path =[]

        for j in list_name:
            name = path+'/'+j
            url_path.append(name)

        # 测试一个
        for p in url_path:
            data_next_next_name = {
                'password': '',
                'path': p
            }
            print('parse_four-path=,',data_next_next_name['path'])
            url = 'https://pan.uvooc.com/api/fs/get'
            time.sleep(0.1)  # 程序将在这里暂停5秒
            yield scrapy.FormRequest(url=url, formdata=data_next_next_name, callback=self.parse_five, dont_filter=True
                                     )

    def parse_five(self, response):
        pass
        print("parse-five")
        data = response.json()
        raw_url = data['data']['raw_url']
        name = data['data']['name']
        time.sleep(0.1)  # 程序将在这里暂停5秒

        # 假设从网页中提取文件URL和文件名
        # file_url = response.urljoin('path/to/file.pdf')
        # filename = 'my_custom_name.pdf'

        yield {
            'file_urls': raw_url,
            'filenames': name
        }
        # yield scrapy.Request(raw_url, callback=self.parse_page,
        #                      meta={'name': name})







    #
    # def parse_page(self, response):
    #     pass
    #     print('parse_page_parse_page_parse_page')
    #     name = response.meta['name']
    #     # 使用传递的参数
    #     filename = name['name']
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {filename}')
    #
    #
    #
    # def parse_threed(self, response):
    #         # 从 meta 字典中取出自定义信息
    #         path = response.meta['custom_info']
    #         # print('parse_threed.response',response.json())
    #         # 继续你的处理逻辑
    #
    #         print("Received param1:", path)
    #         # 需要循环path
    #         data_next_next_name = {
    #             'page': '1',
    #             'password': "",
    #             'path': path,
    #             'per_page': '30',
    #             'refresh': 'false'
    #         }
    #         print('parse_threed-path=', data_next_next_name['path'])
    #         time.sleep(1)  # 程序将在这里暂停5秒
    #         url = 'https://pan.uvooc.com/api/fs/list'
    #         yield scrapy.FormRequest(url=url, formdata=data_next_next_name, callback=self.parse_four, dont_filter=True
    #                                  , meta={'custom_info': data_next_next_name['path']},  # 使用 meta 字典传递自定义参数
    #                                  )
