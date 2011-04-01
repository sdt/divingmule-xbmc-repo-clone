import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.program.piratebay')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )

def Categories():
		addDir('Video','video',1,icon)
		addDir('Audio','audio',1,icon)
		addDir('Applications','apps',1,icon)
		addDir('Games','games',1,icon)
		addDir('Other','other',1,icon)
		addDir('Search','',4,icon)


def getSubcate(url):
		base_url = 'http://thepiratebay.org/top'
		req = urllib2.Request(base_url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		if url == 'video':
				items = soup.findAll('td', attrs={'class' : "categoriesContainer"})[0]('dd')[1]('a')
		elif url == 'audio':
				items = soup.findAll('td', attrs={'class' : "categoriesContainer"})[0]('dd')[0]('a')
		elif url == 'apps':
				items = soup.findAll('td', attrs={'class' : "categoriesContainer"})[0]('dd')[2]('a')
		elif url == 'games':
				items = soup.findAll('td', attrs={'class' : "categoriesContainer"})[1]('dd')[0]('a')
		elif url == 'other':
				items = soup.findAll('td', attrs={'class' : "categoriesContainer"})[1]('dd')[1]('a')
		for item in items:
				name = item['title']
				url = item['href']
				addDir('Top 100 - '+name,'http://thepiratebay.org'+url,2,icon)


def Search():
		searchStr = ''
		keyboard = xbmc.Keyboard(searchStr, "Search")
		keyboard.doModal()
		if (keyboard.isConfirmed() == False):
				return
		searchstring = keyboard.getText()
		if len(searchstring) == 0:
				return
		newStr = searchstring.replace(' ','%20')
		url = 'http://thepiratebay.org/search/'+newStr
		getTorrents(url)
				
				
def getTorrents(url):
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)		
		torrents = soup.find('table', attrs={'id' : "searchResult"})('tr')
		for torrent in torrents:
				try:
						name = torrent('td')[1]('a')[0]['title']
						url = torrent('td')[1]('a')[1]['href']
						size = torrent('font')[0].contents[0].split(', ')[1]
						se = torrent('td')[2].string
						le = torrent('td')[3].string
						addDir(name[12:]+' | se:'+se+' le:'+le,url,3,'')
				except:
						pass

						
def Download(url):
		filename = str(url).split('/')[4]
		def download(url, dest):
				dialog = xbmcgui.DialogProgress()
				dialog.create('Downloading Torrent File','From the PirateBay', filename)
				urllib.urlretrieve(url, dest, lambda nb, bs, fs, url = url: _pbhook(nb, bs, fs, url, dialog))
		def _pbhook(numblocks, blocksize, filesize, url = None,dialog = None):
				try:
						percent = min((numblocks * blocksize * 100) / filesize, 100)
						dialog.update(percent)
				except:
						percent = 100
						dialog.update(percent)
				if dialog.iscanceled():
						dialog.close()
		if (__settings__.getSetting('download') == ''):
				__settings__.openSettings('download')
		filepath = xbmc.translatePath(os.path.join(__settings__.getSetting('download'),filename))
		download(url, filepath)
						
						
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


def addLink(name,url,iconimage):
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
		return ok


def addDir(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
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
		Categories()
		
elif mode==1:
		print""
		getSubcate(url)
		
elif mode==2:
		print""
		getTorrents(url)
		
elif mode==3:
		print""
		Download(url)
		
elif mode==4:
		print""
		Search()
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))
