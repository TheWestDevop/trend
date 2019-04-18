import newspaper
import nltk



class Crawler:
	def __init__(self,url):
		try:
			nltk.download('punkt')
		except Exception as ex:
			print(ex)
		self.url = url
		self.isstarted=False
		self.ispaused = False
		self.newspaper = newspaper.build(url)
		
	#start the crawler
	def start(self):
		if self.isstarted:
			print("crawler already started")
		else:
			self.isstarted=True
			
			for article in self.newspaper.articles:
				article.download()
				article.parse()
				article.nlp()
				print(article.url)
				print(article.authors)
				article.title
				article.text
			
		pass
		
	#stop the crawler
	def stop(self):
		pass
		
	#pause the crawler
	def pause(self):
		pass
	
	
if __name__=="__main__":
	url="https://www.vogue.com"
	crawler = Crawler(url)
	crawler.start()
