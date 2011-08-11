WebCheck
--------

WebCheck is a Python script and plugin written to be using with Server Density.
It will check a website and scan for a specific string to see if the page is working properly.

Lets say that you want to check the website http://devin.la/blog
This page uses the database, some libs, and some other stuff.
Now lets say someone committed a change to one of the bases classes the broke this page.
Looking for &lt;/html&gt;, we can know if we got a fatal error or not.

WebCheck accepts 3 config parameters

* **url**: the url to check
* **find**: the regex to .search
* **result**: the quantifier of the result. if it is true, matching is true, otherwise false. this way you can search for either something like &lt;/html&gt;, or something like Fatal Error

You can create as many entries in the sd-agent config as you want. Here is a sample config entry


	[WebCheck]
	name: Give.mobi
	url: http://m.give.mobi/
	find: </html>
	result: True
	
	[WebCheck 2]
	name: devin.la
	url: http://devin.la/
	find: </html>
	result: True
