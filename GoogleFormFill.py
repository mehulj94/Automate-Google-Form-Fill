import urllib,urllib2

data = "" #Text you have to fill in the form. You can also read a file and fill its content in a google form.

url="https://docs.google.com/forms/d/XXXXXXXXXXXXXXXXXXXXXXX/formResponse" #URL to the form you want to fill. FormResponse should be used instead of ViewForm

text_entry_field={'entry.XXXXXXX':data} #Specify the Field Name here

"""
Hop to your form page, and click Responses > Get pre-filled URL. It'll ask you to do a sample fill-out of your form. I'd suggest putting in responses that easily let you see what question you're answering. Once you hit submit, it's going to give you a URL in the form of...
https://docs.google.com/forms/d/<form_id>/viewform?entry.XXXXXXX=____&entry.YYYYYY=____...
Now, change viewform to formResponse within the URL.
"""

try:
	dataenc=urllib.urlencode(text_entry_field)
	req=urllib2.Request(url,dataenc)
	response=urllib2.urlopen(req)
	data=''
except Exception as e:
	print e