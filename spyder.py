from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spyder:

    # Class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spyder.project_name = project_name
        Spyder.base_url = base_url
        Spyder.domain_name = domain_name
        Spyder.queue_file = Spyder.project_name + '/queue.txt'
        Spyder.crawled_file = Spyder.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page()


