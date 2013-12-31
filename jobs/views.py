from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from urllib2 import urlopen
from jobs import cbParser
from jobs.models import Companies
from django.forms.models import model_to_dict
#from django.utils import simplejson 
import json 
# Create your views here.

def allJobs(request):

	if Companies.objects.all().count() == 0:
		boeingCompanies = cbParser.getAllBoeingCompanies('boeing')
		for company in boeingCompanies:
			dbCompany = Companies(companyName = company.companyName, overview = company.overview , homePageURL = company.homePageURL , cbPermalink = company.cbPermalink ) 
			dbCompany.save()
				
	allCompanies = Companies.objects.all()

	context = {'allCompanies' : allCompanies}
	return render(request, 'jobs/jobs_all.html', context)

def deleteAll(request):
	if request.POST.get('delete'):
		Companies.objects.all().delete()
		return HttpResponse("All Items Deleted")

def getCompanyInfo(request, permalink):
	try:
		company = Companies.objects.get(cbPermalink = permalink)
		#Not able to send whole object
		context = {'companyName' : company.companyName,
					'companyURL:':  company.homePageURL	,
					'overview'	 : company.overview }
		return render(request, 'jobs/jobs_details.html', context)
	except Companies.DoesNotExist:
		return HttpResponse("NO Deatails Found")

def checkForNewCompanies(request):
	#empty condition should not be handled by this method
	newCompanies = ""	
	if Companies.objects.all().count() > 0:
		boeingCompanies = cbParser.getAllBoeingCompanies('boeing')
		for company in boeingCompanies:
			if not Companies.objects.filter(companyName = company.companyName).exists():
				dbCompany = Companies(companyName = company.companyName, overview = company.overview , homePageURL = company.homePageURL , cbPermalink = company.cbPermalink ) 
				dbCompany.save()
				newCompanies = newCompanies + "<div class = 'row'><div class = 'col-md-3'> COMP"+ company.companyName +" </div><div class = 'col-md-2'><a href = /company/"+ company.cbPermalink + "/details>Details</a></div>"
	return HttpResponse(newCompanies)



			
