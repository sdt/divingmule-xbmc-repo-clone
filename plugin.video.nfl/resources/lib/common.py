import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup
try:
    import json
except:
    import simplejson as json

__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')
next = os.path.join( home, 'resources','icons','next.png' )

def _index(url,fanart):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', url.split('cda')[0]),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link)
        videos = soup.findAll('div', attrs={'class' : 'bd'})[0]('ul')[0]('li')
        for video in videos:
            title = video('a')[0]['title']
            link = video('a')[0]['href'].split('/')[-1]
            thumb = video('img')[0]['src']
            try:
                duration = video('span')[3].string.replace('(','').replace(')','')
                if not video('span')[4].string==None:
                    desc = video('span')[4].string
                else:
                    desc = video('span')[5].string
            except:
                duration =''
                try:
                    desc = video('span')[-1].string
                except:
                    desc =''
            try:        
                addLink(title+' - '+desc,url.split('cda')[0]+'cda-web/audio-video-module.htm?dataMode=singleMediaContent&id='+link,thumb,duration,8,fanart)
            except:
                pass
        page = int(url[-1])
        url = url[:-1]+str(page+1)
        addDir('Next Page',url,7,next,fanart)

def _getVideoUrl(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', url.split('cda')[0]),
                    ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        data = json.loads(link)
        print data
        if not data['MediaPlayList'][0]['cdnData'][0]['paths']['high']=='':
            url = data['MediaPlayList'][0]['cdnData'][0]['paths']['high']
        elif not data['MediaPlayList'][0]['cdnData'][0]['paths']['medium']=='':
            url = data['MediaPlayList'][0]['cdnData'][0]['paths']['medium']
        else:
            url = data['MediaPlayList'][0]['cdnData'][0]['paths']['low']
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

def addLink(name,url,iconimage,duration,mode,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "duration": duration } )
        liz.setProperty('IsPlayable', 'true')
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok