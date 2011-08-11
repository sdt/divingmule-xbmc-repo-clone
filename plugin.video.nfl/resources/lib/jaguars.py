import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')

icon = 'http://farm7.static.flickr.com/6007/5994132885_27f73cafed_m.jpg'
fanart = 'http://farm7.static.flickr.com/6007/5994132885_732597a439_o.jpg'

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
        addDir('All Videos','http://www.jaguars.com/multimedia/list.aspx?tag=all&type=video&start=0',46,icon,fanart)
        addDir('Cheerleaders','http://www.jaguars.com/multimedia/list.aspx?tag=Cheerleaders&type=video&start=0  ',46,icon,fanart)
        addDir('Combine','http://www.jaguars.com/multimedia/list.aspx?tag=Combine&type=video&start=0',46,icon,fanart)
        addDir('Community','http://www.jaguars.com/multimedia/list.aspx?tag=Community&type=video&start=0',46,icon,fanart)
        addDir('Draft','http://www.jaguars.com/multimedia/list.aspx?tag=Draft&type=video&start=0',46,icon,fanart)
        addDir('Game Previews and Highlights','http://www.jaguars.com/multimedia/list.aspx?tag=Game-Previews-and-Highlights&type=video&start=0',46,icon,fanart)
        addDir('Interviews','http://www.jaguars.com/multimedia/list.aspx?tag=Interviews&type=video&start=0',46,icon,fanart)
        addDir('Minicamp','http://www.jaguars.com/multimedia/list.aspx?tag=Minicamp&type=video&start=0',45,icon,fanart)
        addDir('NFL Network','http://www.jaguars.com/multimedia/list.aspx?tag=NFL-Network&type=video&start=0',46,icon,fanart)
        addDir('Special Features','http://www.jaguars.com/multimedia/list.aspx?tag=Special-Features&type=video&start=0',46,icon,fanart)
        addDir('Team Teal','http://www.jaguars.com/multimedia/list.aspx?tag=Team-Teal&type=video&start=0',46,icon,fanart)
        addDir('Training Camp','http://www.jaguars.com/multimedia/list.aspx?tag=Training-Camp&type=video&start=0',46,icon,fanart)
        
        
def _index(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.jaguars.com/multimedia'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        videos = soup('div', attrs={'class' : "video-block"})
        for video in videos:
            name = video('div')[1].string.next
            name = name.replace('  ','').replace('\r\n','')
            link = video('a')[0]['href']
            thumb = video('img')[0]['src']
            date = video('div')[1].string
            addLink(name+' - '+date,link,thumb,47)
        if len(videos)==16:
            page = int(url[-1])+16
            url = url[:-1]+str(page)
            addDir('Next Page',url,46,os.path.join( home, 'resources','icons','next.png' ),fanart)


def _getVideoUrl(url):
        req = urllib2.Request('http://www.jaguars.com/multimedia/default.aspx'+url)
        req.addheaders = [('Referer', 'http://www.jaguars.com/multimedia'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        matchb=re.compile("file: \'(.+?)\',").findall(link)
        if not re.search('flv',matchb[0]):
            if matchb[0].startswith('mp4:'):
                Playpath = ' Playpath='+matchb[0]
            else:
                Playpath = ' Playpath=mp4:'+matchb[0]
        else:
            Playpath = ' Playpath='+matchb[0].replace('.flv','')
        app = ' app=ondemand/flv/'
        swfUrl = ' swfUrl=http://www.jaguars.com/multimedia/flash/player2.swf'
        tcUrl = 'rtmp://cp40749.edgefcs.net/ondemand/flv/'
        pageUrl = ' pageUrl=http://www.jaguars.com/multimedia/'+url
        url = tcUrl+swfUrl+Playpath+pageUrl+app
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)        