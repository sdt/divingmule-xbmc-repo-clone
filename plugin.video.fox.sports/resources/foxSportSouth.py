import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.fox.sports')
home = __settings__.getAddonInfo('path')
icon = os.path.join( home, 'icon.png' )
fanart = os.path.join( home, 'fanart.jpg' )


def Categories():
        addDir('Top Videos','',icon,5)
        addDir('Braves','',icon,5)
        addDir('Falcons','',icon,5)
        addDir('ACC','',icon,5)
        addDir('SEC','',icon,5)
        addDir('New Collage Football Show','',icon,5)
        addDir('CUSA','',icon,5)
        addDir('SEC Gridiron Live','',icon,5)


def Index(name):
        url='http://www.foxsportssouth.com/pages/video'
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://www.foxsportssouth.com/pages/video'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        if name == 'Top Videos':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_0'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'Braves':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_1'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'Falcons':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_2'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'ACC':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_3'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'SEC':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_4'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'New Collage Football Show':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_5'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'CUSA':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_6'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        if name == 'SEC Gridiron Live':
            items = soup.find('div', attrs={'id' : 'horizontal_tabs_1160_tab_body_7'}).findAll('div', attrs={'class' : 'net_videohead_horo'})
        for i in items:
            vidId = i('div')[1].string
            name = i('a')[1].contents[-1]
            thumb = i.img['src']
            addLink(name,vidId,6,thumb)
            

def setVideoUrl(url):
        url='http://edge6.catalog.video.msn.com/videoByUuids.aspx?mk=&rct=1,2,3,4,5,6&uuids='+url
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://www.foxsportssouth.com/pages/video'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        print response.geturl()
        print response.info()
        response.close()
        soup = BeautifulStoneSoup(link)

        for i in soup('videofile'):
            bitrate = i['bitrate']
            formatcode = i['formatcode']
            url = i.uri
            print (formatcode, bitrate, url)
        try:
            url = soup.find('videofile', attrs={'formatcode' : "104"}).uri.string
        except:
            url = soup.find('videofile', attrs={'formatcode' : "103"}).uri.string
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

            
def addLink(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable', 'true')        
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,iconimage,mode):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok            