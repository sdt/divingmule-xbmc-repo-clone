import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
import simplejson as json
from BeautifulSoup import BeautifulStoneSoup
import sys,subprocess

__settings__ = xbmcaddon.Addon(id='plugin.video.pipes')
__language__ = __settings__.getLocalizedString

__home__ = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( __home__, 'icon.png' ) )
jicon = xbmc.translatePath( os.path.join( __home__, 'resources/justin.png' ) )
uicon = xbmc.translatePath( os.path.join( __home__, 'resources/ustream.png' ) ) 
oicon = xbmc.translatePath( os.path.join( __home__, 'resources/own3d.png' ) )
zicon = xbmc.translatePath( os.path.join( __home__, 'resources/zp.png' ) )
licon = xbmc.translatePath( os.path.join( __home__, 'resources/livestream.png' ) )
vicon = xbmc.translatePath( os.path.join( __home__, 'resources/veetle.png' ) )

def CATEGORIES():
		addDir('Justin.TV Stream Search','justinSearch',4,jicon,True)
		addDir('Justin.TV Gaming','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fgaming&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Entertainment','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fentertainment&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Featured','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Ffeatured&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Mobile','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fmobile&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Social','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fsocial&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Sports','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fsports&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV News','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fnews&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Animals','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fanimals&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Science/Tech','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fscience_tech&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)
		addDir('Justin.TV Other','http://pipes.yahoo.com/pipes/pipe.run?JustinTV=http%3A%2F%2Fwww.justin.tv%2Fdirectory%2Fother&_id=1e08a1deb5004f7ecaa0976bdc86c7e9&_render=json',1,jicon,True)		
		addDir('uStream','http://pipes.yahoo.com/pipes/pipe.run?_id=6eee52f0c0dcd4f43511846e20bdb99f&_render=json',1,uicon,True)
		addDir('own3d','http://api.own3d.tv/live',5,oicon,True)
		addDir('Zero Punctuation','http://pipes.yahoo.com/pipes/pipe.run?_id=5b30a47868c3e2fe5322f347a8b0ff7c&_render=json',1,zicon,True)
		addDir('Livestream','http://pipes.yahoo.com/pipes/pipe.run?_id=6dc7445ecde7144c52343770a71359a9&_render=json',1,licon,True)
		addDir('Veetle','http://pipes.yahoo.com/pipes/pipe.run?_id=c1053538af50884c9e4976afbe107ad7&_render=json',1,vicon,True)
		addDir('Enter URL','addURL',3,icon,True)
		

def INDEX(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		data = json.loads(link)
		channels = data['value']['items']
		for channel in channels:
				try:
						title = channel['title']
						description = channel['description']
						thumbnail = channel['thumb']
						url = channel['link']
						addDir(title+' - '+description,url,2,thumbnail,False)
				except:
						pass


def searchJustin():
		searchStr = ''
		keyboard = xbmc.Keyboard(searchStr, "Search")
		keyboard.doModal()
		if (keyboard.isConfirmed() == False):
				return
		newStr = keyboard.getText()
		if len(newStr) == 0:
				return
		url =  'http://api.justin.tv/api/stream/search/'+newStr+'.xml'
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		channels = soup('stream')
		for channel in channels:
				name = channel('name')[0].string
				title = channel('title')[0].string
				if title == None:
						title = ''
				url = channel('channel_url')[0].string
				thumbnail = channel('image_url_large')[0].string
				try:
						addDir(name+' - '+title,url,2,thumbnail,True)
				except:
						pass
					

def getFeed(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()		
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		channels = soup('item')
		for channel in channels:
				url = channel('link')[0].string
				try:
						name = channel('title')[0].string
				except:
						name = '???'
				try:
						thumbnail = channel('media:thumbnail')[0]['url']
				except:
						thumbnail = ''
				addDir(name,url,2,thumbnail,True)


def addURL():
		searchStr = 'http://'
		keyboard = xbmc.Keyboard(searchStr, "Enter a URL")
		keyboard.doModal()
		if (keyboard.isConfirmed() == False):
				return
		link = keyboard.getText()
		if len(link) <= 7:
				return
		startFirefox(link)
					
					
def startFirefox(url):
		print 'os.name ---------> '+os.name
		if os.name =='posix':
				target = '/usr/bin/firefox -P XBMC '+url
				os.system(target)
		elif os.name =='nt':
				firefox = __settings__.getSetting('firefox')
				print'----------->>>>'+firefox
				if firefox == "":
						dialog = xbmcgui.Dialog()
						ok = dialog.ok('Pipes','Locate Your Firefox')
						__settings__.openSettings('firefox')
						if firefox == "":
								return
				target = '"'+firefox+'" -P "XBMC" '+url
				xbmc.executebuiltin( "System.Exec(%s)" %target )


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


def addDir(name,url,mode,iconimage,Folder):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		# liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=Folder)
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
		CATEGORIES()
		
elif mode==1:
		print ""+url
		INDEX(url)

elif mode==2:
		print ""+url
		startFirefox(url)
		
elif mode==3:
		print ""+url
		addURL()
		
elif mode==4:
		print ""+url
		searchJustin()
		
elif mode==5:
		print ""+url
		getFeed(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
