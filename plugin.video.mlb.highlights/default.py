import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
import simplejson as json
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.mlb.highlights')
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )


def categories():
		addDir('Play Latest Videos','',3,icon)
		addDir('Videos by Team','',4,icon)
		addDir('Latest Videos','http://mlb.mlb.com/ws/search/MediaSearchService?type=json&src=vpp&start=0&src=vpp&&hitsPerPage=60&sort=desc&sort_type=custom&src=vpp&hitsPerPage=60&src=vpp',1,icon)
		addDir('FastCast','http://mlb.mlb.com/ws/search/MediaSearchService?mlbtax_key=fastcast&sort=desc&sort_type=date&hitsPerPage=200&src=vpp',1,icon)
		addDir('Must C','http://mlb.mlb.com/ws/search/MediaSearchService?mlbtax_key=must_c&sort=desc&sort_type=date&hitsPerPage=200&src=vpp',1,icon)
		addDir('Game Recaps','http://mlb.mlb.com/ws/search/MediaSearchService?&sort=desc&sort_type=date&subject=MLBCOM_GAME_RECAP&hitsPerPage=60&src=vpp',1,icon)
		addDir('MLB Network','http://mlb.mlb.com/ws/search/MediaSearchService?mlbtax_key=mlb_network&sort=desc&sort_type=date&hitsPerPage=360&src=vpp',1,icon)
		addDir('Top Plays','http://mlb.mlb.com/ws/search/MediaSearchService?&sort=desc&sort_type=date&subject=MLBCOM_TOP_PLAY&hitsPerPage=60&src=vpp',1,icon)


def getTeams():
		url='http://mlb.mlb.com/video/index.jsp'
		req = urllib2.Request(url)
		req.addheaders = [('Referer', ''),
				('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		teams = soup.find('ul', attrs={'id' : "teamVlpNav"})('li')
		for team in teams:
				name = team('a')[0]['title']
				url = str(team('a')[0]['href'])[-3:].replace('=','')
				addDir(name,url,5,icon)
				
				
def getTeamVideo(url):
		url='http://mlb.mlb.com/gen/'+url+'/components/multimedia/topvideos.xml'
		req = urllib2.Request(url)
		req.addheaders = [('Referer', ''),
				('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
		videos = soup('item')
		for video in videos:
				name = video('title')[0].string
				thumb = video('picture', attrs={'type' : "dam-raw-thumb"})[0]('url')[0].string
				if video('url', attrs={'speed' : "1200"}):
						url = video('url', attrs={'speed' : "1200"})[0].string
				elif video('url', attrs={'speed' : "1000"}):
						url = video('url', attrs={'speed' : "1000"})[0].string
				elif video('url', attrs={'speed' : "800"}):
						url = video('url', attrs={'speed' : "800"})[0].string
				duration = video('duration')[0].string
				desc = video('big_blurb')[0].string
				addTeamLink(name,url,desc,duration,thumb)
		
		
def playLatest():
		req = urllib2.Request('http://mlb.mlb.com/ws/search/MediaSearchService?type=json&src=vpp&start=0&src=vpp&&hitsPerPage=60&sort=desc&sort_type=custom&src=vpp&hitsPerPage=60&src=vpp')
		req.addheaders = [('Referer', 'http://mlb.mlb.com/video/play.jsp?cid=mlb'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		data = json.loads(link)
		videos = data['mediaContent']
		playlist = xbmc.PlayList(1)
		playlist.clear()
		for video in videos:
				name = video['blurb']
				link = video['url']
				thumb = video['thumbnails'][2]['src']
				url = getVideoURL(link)
				info = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
				playlist.add(url, info)
		play=xbmc.Player().play(playlist)


def getVideos(url):
		req = urllib2.Request(url)
		req.addheaders = [('Referer', 'http://mlb.mlb.com/video/play.jsp?cid=mlb'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		data = json.loads(link)
		videos = data['mediaContent']
		for video in videos:
				name = video['blurb']
				desc = video['bigBlurb']
				url = video['url']
				thumb = video['thumbnails'][2]['src']
				addLink(name,url,desc,2,thumb)


def setVideoURL(url):
		url = getVideoURL(url)
		item = xbmcgui.ListItem(path=url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

		
def getVideoURL(url):
		req = urllib2.Request(url)
		req.addheaders = [('Referer', 'http://mlb.mlb.com/video/play.jsp?cid=mlb'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulStoneSoup(link)
		if soup.find('url', attrs={'playback_scenario' : "FLASH_1200K_640X360"}):
				url = soup.find('url', attrs={'playback_scenario' : "FLASH_1200K_640X360"}).string
		elif soup.find('url', attrs={'playback_scenario' : "FLASH_1000K_640X360"}):
				url = soup.find('url', attrs={'playback_scenario' : "FLASH_1000K_640X360"}).string
		elif soup.find('url', attrs={'playback_scenario' : "FLASH_600K_400X224"}):
				url = soup.find('url', attrs={'playback_scenario' : "FLASH_600K_400X224"}).string
		return url

	
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


def addLink(name,url,desc,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc } )
		liz.setProperty('IsPlayable', 'true')
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
		return ok


def addDir(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok
		

def addTeamLink(name,url,desc,duration,iconimage):
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc, "Duration": duration } )
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
		categories()
		
if mode==1:
		print""
		getVideos(url)

if mode==2:
		print""
		setVideoURL(url)
		
if mode==3:
		print""
		playLatest()
		
if mode==4:
		print""
		getTeams()

if mode==5:
		print""		
		getTeamVideo(url)
		
xbmcplugin.endOfDirectory(int(sys.argv[1]))
