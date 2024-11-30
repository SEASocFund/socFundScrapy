keywords = ['东南亚', '东盟']

if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute('scrapy crawl socFund -o SEAASEAN.csv'.split())