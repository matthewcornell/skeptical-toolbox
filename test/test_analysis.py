import unittest

from analysis.HtmlAnalysis import HtmlAnalysis


class TestAnalysis(unittest.TestCase):
    url_file_title_all_off_measure = \
        [('http://dailycaller.com/2015/04/24/global-warming-pause/',
          'warming.html',
          'Global Warming ‘Pause’ Extends Nearly 18 And A Half Years | The Daily Caller',
          74,
          7,
          7 / 16),  # num links / num paras
         ('http://qz.com/488851/buying-organic-veggies-at-the-supermarket-is-basically-a-waste-of-money/',
          'organic.html',
          'Buying organic veggies at the supermarket is a waste of money - Quartz',
          22,
          13,
          13 / 22)]

    def test_title_and_outgoing_links(self):
        for url, filename, title, num_all_links, num_offsite_links, links_to_paras in self.url_file_title_all_off_measure:
            with open(filename) as file:
                analysis = HtmlAnalysis(url, file.read())
                self.assertEqual(title, analysis.title)

                analysis = HtmlAnalysis(url, file.read())
                outgoing_links_all = analysis.outgoing_links(False)     # on and offsite
                outgoing_links_offsite = analysis.outgoing_links(True)  # only offsite
                self.assertEqual(num_all_links, len(outgoing_links_all))
                self.assertEqual(num_offsite_links, len(outgoing_links_offsite))
                self.assertEqual(links_to_paras, analysis.outgoing_link_to_para_ratio())