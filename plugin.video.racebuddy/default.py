import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

addon = xbmcaddon.Addon(id='plugin.video.racebuddy')
home = addon.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )

page_truck = 'http://www.nascar.com/multimedia/webcast/truck_racebuddy/'
page_nns = 'http://www.nascar.com/multimedia/webcast/nns_racebuddy/'
page_cup = 'http://www.nascar.com/multimedia/webcast/race_buddy/'


def getRequest(url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://www.nascar.com'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return data


def categories():
        addDir('Truck Series', page_truck, 1, xbmc.translatePath( os.path.join( home, 'resources', 'truck.png' ) ))
        addDir('Nationwide Series', page_nns, 1, xbmc.translatePath( os.path.join( home, 'resources', 'nns.png' ) ))
        addDir('Cup Series', page_cup, 1, xbmc.translatePath( os.path.join( home, 'resources', 'cup.png' ) ))
        

def index(url):
        soup = BeautifulSoup(getRequest(url))
        if 'truck_' in url:
            try:
                items = soup('div', attrs={'class' : "nscrRow"})
                for i in items:
                    name = i('div')[2].string +' - '+ i('div')[0].string +' - '+ i('div')[1].string
                    addLink(name,'url',4,os.path.join(home, 'icon.png'), False)
            except:
                getVideoLinks(page_truck+'config.xml')
        if 'nns_' in url:
            try:
                items = soup.table('tr')
                for i in items:
                    name = i('td')[0].string +' - '+ i('td')[2].string +' - '+ i('td')[1].string +' - '+i('td')[3].string
                    addLink(name,'url',4,os.path.join(home, 'icon.png'), False)
            except:
                getVideoLinks(page_nns+'config.xml')
        if 'race_' in url:
            try:
                image = soup('div', attrs={'id' : "nscrHeaderWrapper"})[0].img['src']
                xbmc.executebuiltin("XBMC.Notification(RaceBuddy,No schedule yet - Coverage expected to start in August,15000,"+icon+")")
            except:
                getVideoLinks(page_cup+'config.xml')
            
            
def getVideoLinks(url):
        soup = BeautifulStoneSoup(getRequest(url))
        items = soup('livechannels')[0]('channel')
        for i in items:
            name = i.title.string+' '+i.status.string
            url = i.url.string
            addLink(name,url,3,os.path.join(home, 'icon.png'))
            

def getSmil(url):
        soup = BeautifulSoup(getRequest(url))
        base = soup('meta', attrs={'name' : "httpBase"})[0]['content']
        path_l = []
        for i in soup('video'):
            playpath = i['src']
            bitrate = i['system-bitrate']
            add = path_l.append(playpath)
        item = xbmcgui.ListItem(path=base+path_l[0])
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

        
def setUrl(url):
        if url.endswith('.smil'):
            getSmil(url)
        else:
            tcUrl = url.split('/nascartnt')[0]
            swf = ' swfUrl=http://i.cdn.turner.com/nascar/.element/swf/3.0/video/racebuddy/truck/OverlayPlayer.swf Live=True'
            pageUrl = ' pageUrl=http://www.nascar.com/multimedia/webcast/race_buddy/'
            playpath = ' Playpath='+url.split('/')[-1]
            final_url = tcUrl+pageUrl+playpath+swf
            item = xbmcgui.ListItem(path=final_url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
            

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


def addLink(name,url,mode,iconimage,live=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        if live:
            liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)


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

if mode==None or url==None or len(url)<1:
    print ""
    categories()

elif mode==1:
    print ""
    index(url)

elif mode==2:
    print ""
    getVideoLinks(url)

elif mode==3:
    print ""
    setUrl(url)
    
elif mode==4:
    print ""
    xbmc.executebuiltin("XBMC.Notification(RaceBuddy,When RaceBuddy is live you will get a list of streams instead of the schedule,15000,"+icon+")")
    
xbmcplugin.endOfDirectory(int(sys.argv[1]))