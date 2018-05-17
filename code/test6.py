from pyaltmetric import Altmetric, Citation
from credentials import altmetricKey
from bs4 import BeautifulSoup
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from datetime import datetime
import time



def printSeparator(character, times):
	print(character * times)

if __name__ == '__main__':
	
	#https://github.com/wearp/pyaltmetric
	#https://api.altmetric.com/version/citations/timeframe
	#http://api.altmetric.com/docs/call_citations.html

	timeframe		='1d'
	resultsPerPage 	= 100
	resultsPage 	= 1
	doiPrefix		= '10.7202' #erudit's doi prefix
	pause			= 1
	myTime	= datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

	
	
	a = Altmetric(altmetricKey)
	
	query = a.citations(timeframe, doi_prefix=doiPrefix)
	totalResults = query['query']['total']
	print totalResults
	
	time.sleep(pause)

	
	for i, r in enumerate(range(1, totalResults, resultsPerPage), 1):
		print(i, r)
	
		query = a.citations(timeframe, num_results=resultsPerPage, page=i, doi_prefix=doiPrefix)
		print(query)
		#
		xml = dicttoxml(query, custom_root='altmetric', attr_type=False)
			
		dom = parseString(xml)
		xmlString = dom.toprettyxml()
		print(xmlString)
		
		
		soup = BeautifulSoup(xml, "lxml")
		
		dois = soup.find_all("doi")
		for d in dois:
			print(d.get_text())
		"""
		for q in query['results']:
			
			
			printSeparator('*', 50)
			
			xml = dicttoxml(q, custom_root='document', attr_type=False)
			
			dom = parseString(xml)
			xmlString = dom.toprettyxml()
			print(xmlString)
			
			
			myTime	= datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')

			filename = 'out/' + myTime + '.xml'
			f = open(filename,'w')
			f.write(xmlString.encode('utf-8'))
			f.close()
			
		
		"""
		
		filename = '/mnt/smeCode/altm/code/out/' + myTime + '.xml'
		f = open(filename,'w')
		f.write(xmlString.encode('utf-8'))
		f.close()
			
		time.sleep(pause)
		
	
	
