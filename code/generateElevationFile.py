from bs4 import BeautifulSoup
from datetime import datetime
from lxml import etree
import time
import codecs
import pickle
import os


def printSeparator(character, times):
	print(character * times)

if __name__ == '__main__':
	
	doiPrefix		= '10.7202' #erudit's doi prefix
	myTime			= datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
	referencedDocs 		= '/mnt/smeCode/altm/code/out/' + '2017-10-13_22-44-03-672976' + '.xml'
	pickleFile		= '/mnt/smeCode/parseMe2/code/pickles/keywords.p'	
	outputPath 		= '/mnt/smeCode/altm/code/elevation.files/'
	outputFile 		= 'test.xml'

	
	
	printSeparator('*',50)
	print('loading pickle...')
	keywords = pickle.load( open( pickleFile, "rb" ) )
	print('pickle loaded!')	
	printSeparator('*',50)
	
	
	#elevation file
	rootElement = etree.Element("elevate")

	
	
	
	f = codecs.open(referencedDocs,'r','utf-8')
	markup = f.read()
	f.close()
			
	soup = BeautifulSoup(markup, "lxml-xml")
	documents = soup.find_all('doi')		
	for d in documents:
	
		doi = d.get_text().split('/')[1]
		print(doi)	
		#print(d.get_text())
		
		if doi in keywords.keys():
			print(keywords[doi])
			
			queryElement = etree.SubElement(rootElement, "query")
			queryElement.set("text", ' '. join(list(keywords[doi]['terms'])))
		
			docElement = etree.SubElement(queryElement, "doc")
			docElement.set("id", doi)
		
		printSeparator('*',50)
		
		

	printSeparator('*', 50)		
			
	print 'Elevation - Saving xml file...'		
	xmlString = etree.tostring(rootElement, pretty_print=True, encoding='UTF-8')
	fh = codecs.open(os.path.join(outputPath, myTime + '.xml'),'w', encoding='utf-8' )
	fh.write(xmlString.decode('utf-8'))
	fh.close()
	print 'done'	
			
	printSeparator('*', 50)
	
	print(xmlString)
	
	print('bye')
