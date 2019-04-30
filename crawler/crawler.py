import newspaper
import nltk
import random
from models.models import Articles
from datetime import datetime 



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
				Articles.objects.create(
                            title=article.title,
                            summary=article.summary,
                            shortdesc=article.text[:200],
                            content=article.text,
							sid=random.randint(1,10),
							status=random.randint(0,1),
                            author=article.authors,
                            pubdate= datetime.now(),
                            imageurl=article.top_image,
							catid=random.randint(1,10),
							imgid=random.randint(1,10),
                        )
				print(article.url)
				print(article.authors)
				print(article.title)
				print(article.summary)	
				print(article.text)	
				print(article.top_image)	
				print(article.publish_date)
		        
				
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
