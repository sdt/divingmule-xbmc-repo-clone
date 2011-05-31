import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup
try:
    import json
except:
    import simplejson as json

__settings__ = xbmcaddon.Addon(id='plugin.video.pga.tour')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
fanart1 = xbmc.translatePath( os.path.join( home, 'resources/fanart1.jpg' ) )


def categories():
        addDir('Play Latest','',6,icon)
        addDir('Highlights','',1,icon)
        addDir('Features','',2,icon)
        addDir('shows','',3,icon)
        addDir('Instruction','',4,icon)
        
        
def highlights():
        addDir('Top Shots','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=mine&sort=date&isExpired=no&csiID=csi42',5,icon)
        addDir('Morning Movers','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=movers&sort=date&isExpired=no&csiID=csi41',5,icon)
        addDir('Round Recaps','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=highs&sort=date&isExpired=no&csiID=csi40',5,icon)
        addDir('Shot of the Day','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=sod&sort=date&isExpired=no&csiID=csi39',5,icon)
        addDir('Shots of the Week','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=sotw&sort=date&isExpired=no&csiID=csi38',5,icon)
        addDir("Top 10's",'http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=top10&sort=date&isExpired=no&csiID=csi37',5,icon)
        addDir('Player Interviews','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=int&sort=date&isExpired=no&csiID=csi36',5,icon)
        addDir('Memorable Moments','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=memmom&sort=date&isExpired=no&csiID=csi35',5,icon)
        addDir('FedExCup','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=fec&sort=date&isExpired=no&csiID=csi34',5,'icon')
        addDir('Kodak Challenge','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=highlights&chnl=kodak&sort=date&isExpired=no&csiID=csi33',5,icon)

        
def features():
        addDir('19th Hole','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=clubhouse&sort=date&isExpired=no&csiID=csi31',5,icon)
        addDir('Maginnes Uncut','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=uncut&sort=date&isExpired=no&csiID=csi30',5,icon)
        addDir('In the Bag','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=itb&sort=date&isExpired=no&csiID=csi29',5,icon)
        addDir('Outside the Ropes','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=otr&sort=date&isExpired=no&csiID=csi28',5,icon)
        addDir('Celebrity Spotlight','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=celeb&sort=date&isExpired=no&csiID=csi27',5,icon)
        addDir('Flyovers','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=flyovers&sort=date&isExpired=no&csiID=csi26',5,icon)
        addDir('SwingPlex','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=swingplex&sort=date&isExpired=no&csiID=csi25',5,icon)
        addDir('Charity','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=charity&sort=date&isExpired=no&csiID=csi24',5,icon)
        addDir('Commercials','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=features&chnl=psa&sort=date&isExpired=no&csiID=csi23',5,icon)


def shows():
        addDir('INSIDE the PGA TOUR','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=shows&chnl=inside&sort=date&isExpired=no&csiID=csi21',5,icon)
        addDir('Match Play','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=shows&chnl=matchplay&sort=date&isExpired=no&csiID=csi20',5,icon)
        addDir('Fantasy Insider','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=shows&chnl=fantasy&sort=date&isExpired=no&csiID=csi19',5,icon)
        addDir('PGA TOUR Today','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=shows&chnl=tt&sort=date&isExpired=no&csiID=csi18',5,icon)
        addDir('Monday Backspin','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=shows&chnl=backspin&sort=date&isExpired=no&csiID=csi17',5,icon)


def instruction():
        addDir('Swing Coaches','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=instruction&chnl=coaches&sort=date&isExpired=no&csiID=csi15',5,icon)
        addDir('Pro Tips','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=instruction&chnl=protips&sort=date&isExpired=no&csiID=csi14',5,icon)
        addDir('Pro Fitness','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=instruction&chnl=depuy&sort=date&isExpired=no&csiID=csi13',5,icon)
        addDir('Equipment','http://searchapp.pgatour.com/pgatour-search/query.jsp?text=*&type=enhanced&start=1&npp=10&s=all&tc=r&cat=instruction&chnl=barr%20&sort=date&isExpired=no&csiID=csi12',5,icon) 


def playLatest():
        url='http://www.pgatour.com/video/'
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.pgatour.com'),
            ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.findAll('div', attrs={'id' : "latest"})[0]('ul')[0]('li')
        playlist = xbmc.PlayList(1)
        playlist.clear()
        for video in videos:
            name = video('a')[1]('span')[0].string
            urlA = video('a')[0]['href']
            thumb = video('img')[0]['src']
            url = 'http://ht.cdn.turner.com/pgatour/big/video/pga-tour/'+urlA.split('/',4)[3]+'/'+urlA.split('/',5)[5].replace('/index.html','.ws.flv')
            info = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
            playlist.add(url, info)
        play=xbmc.Player().play(playlist)            
            

def getVideos(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://www.pgatour.com'),
                          ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        data = json.loads(soup.textarea.contents[0])
        videos = data['results'][0]
        for video in videos:
            name = video['title']
            thumb = video['metadata']['media']['thumbnail']['url']
            urlid = video['id']
            desc = video['metadata']['media']['excerpt']
            duration = video['metadata']['video']['length']
            link = 'http://ht.cdn.turner.com/pgatour/big/'+urlid.split('/',2)[2]+'.ws.flv'
            addLink(name,link,desc,thumb,duration)
        if len(videos)==10:
            start = re.compile('http://searchapp.pgatour.com/pgatour-search/.+?enhanced&start=(.+?)&npp=.+?').findall(url)
            number = int(start[0])+10
            a = str(number)
            url = url.split('=',3)[0]+'='+url.split('=',3)[1]+'='+url.split('=',3)[2]+'='+a+'&'+url.split('&',3)[3]
            addDir('Next Page',url,5,icon)
        
        
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


def addLink(name,url,desc,thumb,duration):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot":desc, "Duration":duration} )
        liz.setProperty( "Fanart_Image", fanart1 )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
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
        categories()
        
if mode==1:
        print ""
        highlights()

if mode==2:
        print ""
        features()
        
if mode==3:
        print ""
        shows()
        
if mode==4:
        print ""
        instruction()
        
if mode==5:
        print ""
        getVideos(url)
        
if mode==6:
        print ""
        playLatest()
        

xbmcplugin.endOfDirectory(int(sys.argv[1]))