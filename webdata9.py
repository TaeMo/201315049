
# coding: utf-8

# In[13]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_data_textpost.py', u'import scrapy\n\nclass TextPostItem(scrapy.item.Item):\n    title = scrapy.item.Field()\n    url = scrapy.item.Field()\n    submitted = scrapy.item.Field()\n\nclass RedditCrawler(scrapy.spiders.CrawlSpider):\n    name = \'reddit_crawler\'\n    allowed_domains = [\'reddit.com\']\n    start_urls = [\'https://www.reddit.com/r/learnpython/new\']\n    custom_settings = {\n        \'BOT_NAME\': \'reddit-scraper\',\n        \'DEPTH_LIMIT\': 3,\n        \'DOWNLOAD_DELAY\': 3\n    }\n    def parse(self, response):\n        s = scrapy.selector.Selector(response)\n        next_link = s.xpath(\'//span[@class="nextprev"]//a/@href\').extract()[0]\n        if len(next_link):\n            print "--> visiting ",next_link\n            yield self.make_requests_from_url(next_link)\n        posts = scrapy.selector.Selector(response).xpath(\'//div[@id="siteTable"]/div[@onclick="click_thing(this)"]\')\n        for post in posts:\n            i = TextPostItem()\n            i[\'title\'] = post.xpath(\'div[2]/p[1]/a/text()\').extract()[0]\n            i[\'url\'] = post.xpath(\'div[2]/ul/li[1]/a/@href\').extract()[0]\n            i[\'submitted\'] = post.xpath(\'div[2]/p[2]/time/@title\').extract()[0]\n            print "crawling ",i[\'title\']\n            yield i')


# In[14]:

get_ipython().system(u'scrapy runspider src/ds_web_data_textpost.py -o src/ds_web_data_textpost.json -t json --logfile src/ds_web_data_textpost.logfile')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



