from django.db import models

class Companies(models.Model):
	companyName = models.CharField(max_length = 80)
	overview = models.CharField(max_length = 1000, null = True)
	homePageURL =  models.CharField(max_length = 150, null = True )
	cbPermalink =  models.CharField(max_length = 100, unique = True, null = True)
	founded_year = models.IntegerField(null = True)
	Number_of_Employees = models.IntegerField(null = True)
	Last_Updated = models.DateField(null = True)


	def __unicode__(self):
		return self.companyName

