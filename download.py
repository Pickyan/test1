from lxml.html import fromstring,tostring
import requests

def download(url,user_agent):
	headers = {'User-Agent':user_agent}
	try:
		got_html = requests.get(url,headers=headers)
		html = got_html.text
	except requests.exceptions.RequestsException as e:
		print("download error:",e.reason)
	return html