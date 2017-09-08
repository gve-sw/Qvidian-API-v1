import zeep
import logging.config
from lxml import etree
import sys
from HTMLParser import HTMLParser
import os

QvidianAuthenticationWSDL = './wsdl/QvidianAuthentication.wsdl'
CommonWSDL ='./wsdl/Common.wsdl'
ContentLibraryWSDL='./wsdl/ContentLibrary.wsdl'

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s:: %(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': '/tmp/qvidianapi.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
	    },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console','file'],
        },
    }
})

class MyHTMLParser(HTMLParser):
	def __init__(self):
		self.text = ''
		self.start = False
		self.end   = False
		HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):
		if ( not self.end):
			if  (tag == 'div') :
				self.start = True

	def handle_endtag(self, tag):
		if ( not self.end):
			if  (tag == 'div') :
				self.end = True

	def handle_data(self, data):
		if ( not self.end) and self.start :
			self.text += data

def update_endpoint(file,newurl):
	try :
		tree = etree.parse(file)
		namespaces = {'soap':'http://schemas.xmlsoap.org/wsdl/soap/'}
		tree.findall('.//soap:address',namespaces)[0].attrib['location']=newurl
		with open(file, 'w') as file_handle:
		    file_handle.write(etree.tostring(tree, pretty_print=True, encoding='utf8'))		
	except:
		e = sys.exc_info()[0]
		print e
		return False
	else:
		return True


class QvidianAuthentication:
	def __init__( self, endpoint_url = 'https://qpalogin.qvidian.com/QvidianAuthentication.asmx' , wsdl_file = os.path.join(os.path.dirname(__file__), "QvidianAuthentication.wsdl") ):
		update_endpoint(wsdl_file,endpoint_url)
		self.client = zeep.Client(wsdl=wsdl_file)
		self.ConnectResult = None
	def Connect(self, userName, password):
		self.ConnectResult = self.client.service.Connect(userName=userName, password=password)['body']['ConnectResult']

class Common():
	def __init__( self , auth , wsdl_file = os.path.join(os.path.dirname(__file__), "Common.wsdl") ):
		endpoint_url = auth.ConnectResult['CommonURL']
		update_endpoint(wsdl_file,endpoint_url)
		self.client = zeep.Client(wsdl=wsdl_file)
		self.HasPermissionsResponse = None
		self.HeaderType = self.client.get_element('ns0:QvidianCredentialHeader')
		self.AuthenticationToken = auth.ConnectResult['AuthToken']
		
	def HasPermissions(self , Permission ):
		AuthenticationToken = self.AuthenticationToken
		QvidianCredentialHeader = self.HeaderType(AuthenticationToken=AuthenticationToken)
		self.HasPermissionsResponse=self.client.service.HasPermissions(_soapheaders=[QvidianCredentialHeader],Permission=Permission)['body']['HasPermissionsResult']

class ContentLibrary():
	def __init__( self, endpoint_url , wsdl_file = os.path.join(os.path.dirname(__file__), "QvidianAuthentication.wsdl") ):
		update_endpoint(wsdl_file,endpoint_url)
		self.client = zeep.Client(wsdl=wsdl_file)
		self.librarySearchRequestsInitResponse    = None
		self.librarySearchesAsListsResponse       = None
		self.libraryContentPreviewHTMLGetResponse = None
		self.HeaderType = self.client.get_element('ns0:QvidianCredentialHeader')

	def librarySearchRequestsInit(self, AuthenticationToken , requestCount):
		QvidianCredentialHeader = self.HeaderType(AuthenticationToken=AuthenticationToken)
		self.librarySearchRequestsInitResponse=self.client.service.librarySearchRequestsInit(_soapheaders=[QvidianCredentialHeader],requestCount=requestCount)['body']['librarySearchRequestsInitResult']		

	def librarySearchesAsLists(self, AuthenticationToken , searchRequestList):
		QvidianCredentialHeader = self.HeaderType(AuthenticationToken=AuthenticationToken)
		self.librarySearchesAsListsResponse=self.client.service.librarySearchesAsLists(_soapheaders=[QvidianCredentialHeader],searchRequestList=searchRequestList)['body']['librarySearchesAsListsResult']		

	def libraryContentPreviewHTMLGet(self, AuthenticationToken , ContentID):
		QvidianCredentialHeader = self.HeaderType(AuthenticationToken=AuthenticationToken)
		self.libraryContentPreviewHTMLGetResponse=self.client.service.libraryContentPreviewHTMLGet(_soapheaders=[QvidianCredentialHeader],contentID=ContentID,revision='-1')['body']['libraryContentPreviewHTMLGetResult']		


 













