import urllib,urllib2,re,os,cookielib
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.steam')
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = 'http://www.deviantart.com/download/245134540/steam_logo_by_thegreatjug-d41y30s.png'

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def Categories():
        addDir('Newest Videos','http://store.steampowered.com/freestuff/videos',1,icon)
        addDir('Most Watched (past 48 hours)','',3,icon)
        addDir('Search','',4,xbmc.translatePath( os.path.join( home, 'resources', 'search.png' ) ))


def Index(url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        newVideos = soup.findAll('div', attrs={'class' : "tab_video_desc"})
        for video in newVideos:
            name = video('a')[0].string
            vidUrl = video('a')[0]['href']
            Id = vidUrl.split('?')[0].split('/')[-1]
            thumb = 'http://cdn.steampowered.com/v/gfx/apps/'+Id+'/movie.184x123.jpg'
            addDir(name.encode("ascii", "ignore") ,vidUrl,2,thumb)
        try:
            page = soup.find('div', attrs={'id' : "tab_NewVideos_next"}).a['href']
            navcontext = 'navcontext='+page.split('{')[1].split(':')[-1].split('"')[1]
            start = 'start='+str(int(page.split(',')[1])+10)
            url = 'http://store.steampowered.com/search/tab?style=video&'+navcontext+'&tab=NewVideos&'+start+'&count=10'
        except:
            url = 'http://store.steampowered.com/search/tab?style=video&navcontext=1_220_225_&tab=NewVideos&start='+str(int(url.split('&')[-2].split('=')[1])+10)+'&count=10'
        addDir('Next Page',url,1,xbmc.translatePath( os.path.join( home, 'resources', 'next.png' ) ))


def mostWatched():
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        url='http://store.steampowered.com/freestuff/videos'
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link)
        videos = soup.findAll('div', attrs={'class' : "top_video_capsule"})
        for video in videos:
            name = video('a')[1].string
            url = video('a')[1]['href']
            thumb = video('img')[0]['src']
            addDir(name.encode("ascii", "ignore") ,url,2,thumb)


def getVideos(url):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        if soup.find('div', attrs={'id' : "agegate_box"}):
            print 'AGE CHECK'
            headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
            data = '/?ageDay=1&ageMonth=January&ageYear=1980&snr=1_agecheck_agecheck__age-gate'
            newUrl = url.replace('video','agecheck/video').split('?')[0]+data
            req = urllib2.Request(newUrl,None,headers)
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
        match = re.compile("javascript:showGotSteamModal\('gotSteamModal', '(.+?)', '(.+?)'\)").findall(link)
        for vidId,name in match:
            vidId = vidId.split('/')[-1]
            name = name.replace('&quot;','"').decode("utf-8")
            thumb = 'http://cdn.steampowered.com/v/gfx/apps/'+vidId+'/movie.184x123.jpg'
            url = 'http://cdn.steampowered.com/v/gfx/apps/'+vidId+'/movie940.flv'
            addLink(name,url,thumb)


def Search():
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr,'Search')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        newStr = keyboard.getText().replace(' ','+')
        if len(newStr) == 0:
            return
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
        url='http://store.steampowered.com/search/?term='+newStr
        req = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(req)
        link=response.read()
        soup = BeautifulSoup(link)
        items = soup.find('div', attrs={'id' : "search_result_container"})('a')
        for i in items:
            if re.search('video', i['href']):
                name = i.h4.string
                url = i['href']
                thumb = i('img')[1]['src']
                addDir(name,url,2,thumb)


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


def addLink(name,url,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name })
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
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
    Categories()

elif mode==1:
    print ""+url
    Index(url)

elif mode==2:
    print ""+url
    getVideos(url)

elif mode==3:
    print ""
    mostWatched()

elif mode==4:
    print ""
    Search()

xbmcplugin.endOfDirectory(int(sys.argv[1]))