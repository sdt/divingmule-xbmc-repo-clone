import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.live.streams')
home = __settings__.getAddonInfo('path')
file = __settings__.getSetting('xml_file')
if file == "":
		file = xbmc.translatePath( os.path.join( home, 'example_streams.xml' ) )

def getChannels():
		if __settings__.getSetting('community_list') == "true":
				req = urllib2.Request('http://community-links.googlecode.com/svn/trunk/')
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
				files = soup('ul')[0]('li')[1:]
				for i in files:
						url = i('a')[0]['href']
						name = url.replace('.xml','')
						addDir(name,'http://community-links.googlecode.com/svn/trunk/'+url,2,xbmc.translatePath( os.path.join( home, 'icon.png' ) ))
		if __settings__.getSetting('get_xml') != "":
				addDir(__settings__.getSetting('get_xml_name'),__settings__.getSetting('get_xml'),2,xbmc.translatePath( os.path.join( home, 'icon.png' ) ))		
		if __settings__.getSetting('local_file') == "true":
				response = open(file, 'rb')
				link=response.read()
				response.close()
				soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
				if len(soup('channels')) > 0:
						channels = soup('channel')
						for channel in channels:
								name = channel('name')[0].string
								thumbnail = channel('thumbnail')[0].string
								url = ''
								addDir(name,url,1,thumbnail)
				else:
						INDEX()
		
				
def getXML(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		if len(soup('channels')) > 0:
				channels = soup('channel')
				for channel in channels:
						name = channel('name')[0].string
						thumbnail = channel('thumbnail')[0].string
						addDir(name,url,3,thumbnail)
		else:
				indexXML(url)				

				
def getChannelItems_xml(url,name):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		channel_list = soup('name', text=name)[0].next.next.next.next.next
		items = channel_list('item')
		for item in items:
				try:
						name = item('title')[0].string
				except:
						pass
				try:
						if __settings__.getSetting('mirror_link') == "true":
								try:
										url = item('link')[1].string	
								except:
										url = item('link')[0].string
						if __settings__.getSetting('mirror_link_low') == "true":
								try:
										url = item('link')[2].string	
								except:
										try:
												url = item('link')[1].string
										except:
												url = item('link')[0].string
						else:
								url = item('link')[0].string
				except:
						pass
				try:
						thumbnail = item('thumbnail')[0].string
				except:
						pass
				addLink(url,name,thumbnail)


def getChannelItems(name):
		response = open(file, 'rb')
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		channel_list = soup('name', text=name)[0].next.next.next.next.next
		items = channel_list('item')
		for item in items:
				try:
						name = item('title')[0].string
				except:
						pass
				try:
						if __settings__.getSetting('mirror_link') == "true":
								try:
										url = item('link')[1].string	
								except:
										url = item('link')[0].string
						if __settings__.getSetting('mirror_link_low') == "true":
								try:
										url = item('link')[2].string	
								except:
										try:
												url = item('link')[1].string
										except:
												url = item('link')[0].string
						else:
								url = item('link')[0].string
				except:
						pass
				try:
						thumbnail = item('thumbnail')[0].string
				except:
						pass
				addLink(url,name,thumbnail)


def INDEX():
		response = open(file, 'rb')
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		items = soup('item')
		for item in items:
				try:
						name = item('title')[0].string
				except:
						pass
				try:
						if __settings__.getSetting('mirror_link') == "true":
								try:
										url = item('link')[1].string	
								except:
										url = item('link')[0].string
						if __settings__.getSetting('mirror_link_low') == "true":
								try:
										url = item('link')[2].string	
								except:
										try:
												url = item('link')[1].string
										except:
												url = item('link')[0].string
						else:
								url = item('link')[0].string
				except:
						pass
				try:
						thumbnail = item('thumbnail')[0].string
				except:
						pass
				addLink(url,name,thumbnail)
				

def indexXML(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		items = soup('item')
		for item in items:
				try:
						name = item('title')[0].string
				except:
						pass
				try:
						if __settings__.getSetting('mirror_link') == "true":
								try:
										url = item('link')[1].string	
								except:
										url = item('link')[0].string
						if __settings__.getSetting('mirror_link_low') == "true":
								try:
										url = item('link')[2].string	
								except:
										try:
												url = item('link')[1].string
										except:
												url = item('link')[0].string
						else:
								url = item('link')[0].string
				except:
						pass
				try:
						thumbnail = item('thumbnail')[0].string
				except:
						pass
				addLink(url,name,thumbnail)		


def get_params():
		param=[]
		paramstring=sys.argv[2]
		if len(paramstring)>=2:
				params=sys.argv[2]
				cleanedparams=params.replace('?','')
				if (params[len(params)-1]=='/'):
						params=params[0:len(params)-2]
				pairsofparams=cleanedparams.split('&')
				param={}
				for i in range(len(pairsofparams)):
						splitparams={}
						splitparams=pairsofparams[i].split('=')
						if (len(splitparams))==2:
								param[splitparams[0]]=splitparams[1]
								
		return param


def addDir(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok

def addLink(url,name,iconimage):
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
		return ok

			
params=get_params()
url=None
name=None
mode=None

try:
		url=urllib.unquote_plus(params["url"])
except:
		pass
try:
		name=urllib.unquote_plus(params["name"])
except:
		pass
try:
		mode=int(params["mode"])
except:
		pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None:
		print ""
		getChannels()

elif mode==1:
		print ""+url
		getChannelItems(name)

elif mode==2:
		print ""+url
		getXML(url)

elif mode==3:
		print ""+url
		getChannelItems_xml(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
