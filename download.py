import requests

def download(url,user_agent):
	headers = {'User-Agent':user_agent}
	try:
		got_html = requests.get(url,headers=headers)
		html = got_html.text
	except requests.exceptions.RequestsException as e:
		print("download error:",e.reason)
	return html


if __name__ == '__main__':
	url = input("请输入您要下载的网页地址：")
	headers = input("请输入user-agent:")
	html-date = download(url,user_agent)
	print(html)