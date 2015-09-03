import urllib.request
import urllib.parse

from bs4 import BeautifulSoup as bs


class HtmlAnalysis(object):
    """
    Defines routines to analyze a URL and extract various resources to support a skeptical analysis of it.
    """

    def __init__(self, url, html=None):
        """
        :param url: string
        :param html: html content (string) for testing, or None, which means connect to the URL for content
        :return:
        """
        self.url = url
        # set the soup
        if not html:
            # pass user_agent because some sites require spoofing
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            req = urllib.request.Request(url, headers={'User-Agent': user_agent})
            httpResponse = urllib.request.urlopen(req)
            self.soup = bs(httpResponse.read(), "lxml")  # todo encoding?
        else:
            self.soup = bs(html, "lxml")
        self.title = self.soup.title.string

    def is_offsite_link(self, a):
        """
        :param a: the tag to examine
        :return: True if a's href is non-null and links to a domain that is not mine in self.url, False o/w
        """
        site_netloc = urllib.parse.urlparse(self.url).netloc
        link_netloc = urllib.parse.urlparse(a.get('href')).netloc
        return link_netloc and (link_netloc != site_netloc)     # NB: link_netloc is None for roots, e.g., <a href="/">Home</a>

    def outgoing_links(self, only_offsite):
        """
        :param only_offsite: controls whether only offsite links are included (if True) or all links (False)
        :return: list of <a> tags, excluding ones that have no text, and optionally excluding onsite ones if only_offsite
        """
        all_links = [a for a in self.soup.find_all('a') if a.string]
        return [a for a in all_links if self.is_offsite_link(a)] if only_offsite else all_links
