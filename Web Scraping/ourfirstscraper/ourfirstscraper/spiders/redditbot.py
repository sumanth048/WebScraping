# -*- coding: utf-8 -*-
import scrapy

class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.djQeMY').extract()
        votes = response.css('.bLdsNs').extract()
        times = response.css('._3jOxDPIQ0KaOWpzvSQo-1s').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,votes,times,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'comments' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info