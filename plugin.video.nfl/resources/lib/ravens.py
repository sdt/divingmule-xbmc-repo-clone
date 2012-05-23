import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')

icon = 'http://farm7.static.flickr.com/6121/6009301002_16eaf2f9b4_m.jpg'
fanart = 'http://farm7.static.flickr.com/6121/6009301002_739def1079_o.jpg'

def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        

def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

        
def _categories():
        addDir('All Videos','http://www.baltimoreravens.com/Media/Video_Landing.aspx',36,icon,fanart)
        addDir('Game Day','http://www.baltimoreravens.com/Media/Video_Landing.aspx?q=Game+Day',36,icon,fanart)
        addDir('2010','http://www.baltimoreravens.com/Media/Video_Landing.aspx?q=2010',36,icon,fanart)
        addDir('Regular Season','http://www.baltimoreravens.com/Media/Video_Landing.aspx?q=Regular+Season',36,icon,fanart)
        addDir('NFL Network','http://www.baltimoreravens.com/Media/Video_Landing.aspx?q=NFL+Network',36,icon,fanart)
        addDir('Rave TV','http://www.baltimoreravens.com/Media/Video_Landing.aspx?q=Rave+TV',36,icon,fanart)
        
        
def _index(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.baltimoreravens.com/Media/Video_Landing.aspx'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.findAll('div', attrs={'class' : "videoThumbInfo"})
        for video in videos:
            name = video('a')[0]['title']
            thumb = video('img')[0]['src']
            url = thumb.replace('.tmb.jpg','.mp4')
            addLink(name,url,thumb)
            