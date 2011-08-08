import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')
fanart = 'http://farm7.static.flickr.com/6021/5995834962_f0ed81dfd4_o.jpg'
icon = 'http://farm7.static.flickr.com/6021/5995834962_78ff72f058_m.jpg'
base_url = 'http://www.dallascowboys.com/multimedia/multimedia_archives.cfm?'

def _categories():
        addDir('Recent','',16,icon)
        addDir('Players','cat=4',16,icon)
        addDir('Coaches, Execs','cat=5',16,icon)
        addDir('Highlights','cat=1',16,icon)
        addDir('NFL','cat=8',16,icon)
        
        
def _index(url):
        req = urllib2.Request(base_url+url)
        req.addheaders = [('Referer', 'http://www.dallascowboys.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        videos = soup.findAll('li', attrs={'class' : "archiveColumn"})
        for video in videos:
            name = video('div')[0].string
            url = video('a')[0]['href'].split('?')[1]
            thumb = video('img')[0]['src'].replace('..','http://www.dallascowboys.com')
            addLink(name,url,thumb,17)
            
def _getVideoUrl(url):
        req = urllib2.Request(base_url+url)
        req.addheaders = [('Referer', 'http://www.dallascowboys.com/'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        url=re.compile("createPlayer\('(.+?)','.+?','.+?','.+?'\)").findall(link)  
        item = xbmcgui.ListItem(path='http://www.dallascowboys.com/flv/'+url[0])
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
        


def addLink(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
