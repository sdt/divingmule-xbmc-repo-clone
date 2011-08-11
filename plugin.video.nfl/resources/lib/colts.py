import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')

icon = 'http://farm7.static.flickr.com/6014/5994129657_d872d7f4c5_m.jpg'
fanart = 'http://farm7.static.flickr.com/6014/5994129657_ae086fa8c3_o.jpg'

def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        

def addLink(name,url,iconimage,description,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot":description } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok
        
        
def _categories():
        addDir('All Videos','http://www.colts.com/sub.cfm?page=video',38,icon,fanart)
        addDir('Cheerleaders','http://www.colts.com/sub.cfm?page=cheerleaders_dynamic&id=206',38,icon,fanart)
        addDir('Classic Radio Calls','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=203',38,icon,fanart)
        addDir('Monday Press Conf WrapUp','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=216',38,icon,fanart)
        addDir('Post Game Lockerroom','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=208',38,icon,fanart)
        addDir('Post Game Podium - Coach Caldwell','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=214',38,icon,fanart)
        addDir('Pre Game Report','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=210',38,icon,fanart)
        addDir('Sounds of the Game','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=213',38,icon,fanart)
        addDir('UpClose Online','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=212',38,icon,fanart)
        #addDir('Radio / TV Broadcast Information','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=265',38,icon,fanart)
        #addDir('Radio: Listen to the Game','http://www.colts.com/sub.cfm?page=broadcast_dynamic&id=73',38,icon,fanart)
        
        
def _index(url,name):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.colts.com/sub.cfm?page=video'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        if name =='All Videos':
            videos = videos = soup('table')[-2]('td')
        else:
            videos = soup('table', attrs={'cellpadding' : "12", 'cellspacing' : "1"})[0]('td')
        for video in videos:
            name = video('strong')[0].string
            url = video('a')[0]['href']
            desc = video('font')[1].string
            try:
                thumb = video('img')[0]['src']
            except:
                thumb = ''
            addLink(name,url,thumb,desc,39)
            
            
def _getVideoUrl(url):
        req = urllib2.Request('http://www.colts.com/'+url)
        req.addheaders = [('Referer', 'http://www.colts.com/sub.cfm?page=video'),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match = re.compile('\(\'file\',\'(.+?)\'\);\r\n').findall(link)
        item = xbmcgui.ListItem(path=match[0])
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)