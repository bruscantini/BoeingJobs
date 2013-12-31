from urllib2 import urlopen
import json 

def getAllBoeingCompanies(companyName):
	apiCall = "http://api.crunchbase.com/v/1/search.js?query="+companyName+"&entity=company&field=name&api_key=9c89zr2f8a2zdxrgrwmupuwx"
	jsonObjects = urlopen(apiCall).read()
	page_results = json.loads(jsonObjects)
	total_pages = (((page_results['total'])/10)+1) #might be missing a page
	boeingCompanies = []

	for page in range(1, total_pages):
		newAPIcall = apiCall + '&page=' + `page`
		boeingCompanies.extend(parseCompaniesPage(newAPIcall, companyName))

	return boeingCompanies

def parseCompaniesPage(apiCall, companyName):
	jsonObjects = urlopen(apiCall).read()
	page_results = json.loads(jsonObjects)
	companiesOnPage = []
    
    #API not working well, need to filter for companies with boeing in their name
	for cbEntity in page_results['results'] :
		if 'name' in cbEntity and cbEntity['namespace'] == "company":
			if(cbEntity['name'].lower().find(companyName) != -1):
				company = BoeingCompany(cbEntity['name'], cbEntity['overview'], cbEntity['homepage_url'], cbEntity['permalink'])
				companiesOnPage.append(company)

	return companiesOnPage


class BoeingCompany(object):
	"""docstring for BoeingCompany"""
	def __init__(self, companyName, overview , homePageURL , cbPermalink ):
		#converting to str to avoid None Type error
		self.companyName = str(companyName)
		self.overview = str(overview)
		self.homePageURL = str(homePageURL)
		self.cbPermalink = str(cbPermalink)

	

		
			
