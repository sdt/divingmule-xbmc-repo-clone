import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulStoneSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.live.streams')
home = __settings__.getAddonInfo('path')
file = __settings__.getSetting('xml_file')
if file == "":
		file = xbmc.translatePath( os.path.join( home, 'example_streams.xml' ) )


def INDEX():
		# url = ''
		# req = urllib2.Request(url)
		# response = urllib2.urlopen(req)
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

if mode==None or url==None or len(url)<1:
		print ""
		INDEX()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
