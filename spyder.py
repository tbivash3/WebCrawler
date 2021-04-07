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
        self.crawl_page('First Spider', Spyder.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spyder.project_name)
        create_data_files(Spyder.project_name, Spyder.base_url)
        Spyder.queue = file_to_set(Spyder.queue_file)
        Spyder.crawled = file_to_set(Spyder.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spyder.crawled:
            print(thread_name + ' crawling ' + page_url)
            print('Queue ' + str(len(Spyder.queue)) + ' | Crawled ' + str(len(Spyder.crawled)))
            Spyder.add_links_to_queue(Spyder.gather_links(page_url))
            Spyder.queue.remove(page_url)
            Spyder.crawled.add(page_url)
            Spyder.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spyder.base_url, page_url)
            finder.feed(html_string)
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url not in Spyder.queue and url not in Spyder.crawled and Spyder.domain_name not in url:
                Spyder.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spyder.queue, Spyder.queue_file)
        set_to_file(Spyder.crawled, Spyder.crawled_file)




