import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')

icon = 'http://farm7.static.flickr.com/6021/5987940049_a057f154d0_m.jpg'
fanart = 'http://farm7.static.flickr.com/6021/5987940049_4254a6a03e_o.jpg'

def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        

def addLink(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
        
def _categories():
        addDir('Most Recent','http://www.chicagobears.com/multimedia/MostRecentArchives.asp',41,icon,fanart)
        addDir('CBTV','http://www.chicagobears.com/multimedia/CBTVArchives.asp',41,icon,fanart)
        addDir('Game Highlights','http://www.chicagobears.com/multimedia/HighlightsArchives.asp',41,icon,fanart)
        addDir('Features','http://www.chicagobears.com/multimedia/FeaturesArchives.asp',41,icon,fanart)
        addDir('Press Conferences','http://www.chicagobears.com/multimedia/PressArchives.asp',41,icon,fanart)
        addDir('Bears History','http://www.chicagobears.com/multimedia/BearsArchives.asp',41,icon,fanart)
        addDir('Staley','http://www.chicagobears.com/multimedia/StaleyArchives.asp',41,icon,fanart)
        addDir('Community','http://www.chicagobears.com/multimedia/CommunityArchives.asp',41,icon,fanart)
        addDir('CB Network','http://www.chicagobears.com/multimedia/CBNetworkArchive.asp',41,icon,fanart)
        
        
def _index(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.chicagobears.com/multimedia'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        videos = soup.find('ul', attrs={'class' : "list_mod"})('li')
        for video in videos:
            name = video('a')[0].string
            url = video('a')[0]['href'].split('=')[1].split('&')[0]
            date = video('span')[0].string
            thumb = 'http://assets.chicagobears.com/uploads/multimedia/stills/teasers/'+url+'.jpg'
            addLink(name+' - '+date,url,thumb,42)
            
            
def _getVideoUrl(url):
        url = 'http://www.chicagobears.com//flash/popup/data/playlist.xml.asp?MM_FILE_ID='+url
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.chicagobears.com/multimedia'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        Playpath = ' Playpath='+soup.video['featurevideo']
        pageUrl  = ' pageUrl=http://www.chicagobears.com/multimedia/'
        swfUrl = ' swfUrl=http://www.chicagobears.com/flash/popup/bears_hd_main_video_072010.swf'
        tcUrl = 'rtmp://65.216.161.102:1935/ondemand?_fcs_vhost=cp52544.edgefcs.net'
        url = tcUrl+swfUrl+Playpath+pageUrl
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)        