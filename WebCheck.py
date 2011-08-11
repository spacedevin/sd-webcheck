# WebCheck
# https://github.com/arzynik/sd-webcheck

# WebCheck is a Python script and plugin written to be using with Server Density.
# It will check a website and scan for a specific string to see if the page is working properly.

# Lets say that you want to check the website http://devin.la/blog
# This page uses the database, some libs, and some other stuff.
# Now lets say someone committed a change to one of the base classes and broke the blog page.
# Looking for </html>, we can know if we got a fatal error or not.

# this accepts 3 config paramaters
# url: the url to check
# find: the regex to .search
# result: the quantifier of the result. if it is true, matching is true, otherwise false
# 	this way you can search for either something like </html>, or somethng like Fatal Error


from urllib import urlopen
import re

class WebCheck:
	def __init__(self, agentConfig, checksLogger, rawConfig):
		self.agentConfig = agentConfig
		self.checksLogger = checksLogger
		self.rawConfig = rawConfig
		self.cfgField = '^WebCheck'
		
	def run(self):
		cfgre = re.compile(self.cfgField)
		data = {}

		for field in self.rawConfig:
			if cfgre.match(field):

				try:
					response = urlopen(self.rawConfig[field]['url']).read()
					if re.search(self.rawConfig[field]['find'],response) :
						if self.rawConfig[field]['result'] :
							result = True
						else :
							result = False
					else:
						if self.rawConfig[field]['result'] :
							result = False
						else :
							result = True
		
				except Exception:
					result = False
				
				if result :
					ret = 1
				else :
					ret = 0

				data[self.rawConfig[field]['name'].replace('.','_')] = ret

		return data