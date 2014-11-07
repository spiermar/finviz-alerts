import requests
from HTMLParser import HTMLParser

class FinvizParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.ischart = 0
	def handle_starttag(self, tag, attrs):
		if self.ischart:
			if tag == 'a':
				for attr in attrs:
					 if attr[0] == 'href':
					 	print "Link:", attr[1]
				return
			if tag == 'img':
				for attr in attrs:
					 if attr[0] == 'src':
					 	print "Image:", attr[1]
				return
		if tag == 'span':
			if self.ischart:
				self.ischart += 1
			for attr in attrs:
				if attr[0] == 'title':
					if attr[1].startswith("cssbody=[chrtbdy]"):
						self.ischart += 1
						print "Found chart:", attr[1]
	def handle_endtag(self, tag):
		if tag == 'span' and self.ischart:
			self.ischart -= 1

url = "http://finviz.com/screener.ashx?v=211&f=cap_smallover,ta_highlow20d_nh,ta_pattern_doubletop,ta_sma20_sa50,ta_sma50_sa200&ft=4"
r = requests.get(url)
parser = FinvizParser()
parser.feed(r.text)