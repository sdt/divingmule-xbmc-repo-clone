import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP

addon = xbmcaddon.Addon('plugin.video.live.streams')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))

__settings__ = xbmcaddon.Addon(id='plugin.video.live.streams')
home = __settings__.getAddonInfo('path')
REV = os.path.join( profile, 'list_revision')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
file = __settings__.getSetting('xml_file')
if __settings__.getSetting('community_list') == "true":
    if __settings__.getSetting('save_location') == "":
        xbmc.executebuiltin("XBMC.Notification('LiveStreams','Choose a location to save files.',30000,"+icon+")")
        __settings__.openSettings()
if __settings__.getSetting('community_list') == "false":
    if __settings__.getSetting('get_xml') != "":
        url = __settings__.getSetting('get_xml')
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        file = link
    else:
        file = __settings__.getSetting('xml_file')


def getSoup():
        req = urllib2.Request('http://community-links.googlecode.com/svn/trunk/')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        print soup
        files = soup('ul')[0]('li')[1:]
        for i in files:
            name = i('a')[0]['href']
            url = 'http://community-links.googlecode.com/svn/trunk/'+name
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            name = xbmc.makeLegalFilename(os.path.join(__settings__.getSetting('save_location'), '%s') % name)
            try:
                f = open(name,"w")
                f.write(link)
                f.close()
            except:
                print "there was a problem writing to save location."
        req = urllib2.Request('http://community-links.googlecode.com/svn/trunk/')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        try:
            R = open(REV,"w")
            R.write(link)
            R.close()
        except:
            print "there was a problem writing REV to profile."


def checkForUpdate():
        url = 'http://community-links.googlecode.com/svn/trunk/'
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        revision = re.compile('<html><head><title>(.+?)/trunk</title></head>').findall(link)
        try:
            R = open(REV,"r")
            rev = R.read()
            R.close()
        except:
            getSoup()
            print "no REV file found."
        try:
            revision_check = re.compile('<html><head><title>(.+?)/trunk</title></head>').findall(rev)
            if revision_check[0] != revision[0]:
                getSoup()
        except:
            getSoup()
            pass


if __settings__.getSetting('community_list') == "true":
        checkForUpdate()


def getStreams():
        if __settings__.getSetting('community_list') == "true":
            try:
                response = open(file, 'rb')
            except:
                xbmc.executebuiltin("XBMC.Notification('LiveStreams','Choose a file',30000,"+icon+")")
                __settings__.openSettings()
                return
            link=response.read()
            soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        elif __settings__.getSetting('get_xml') != "":
            soup = BeautifulStoneSoup(file, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        if len(soup('channels')) > 0:
                channels = soup('channel')
                for channel in channels:
                        name = channel('name')[0].string
                        thumbnail = channel('thumbnail')[0].string
                        url = ''
                        try:
                                addDir(name,url,2,thumbnail)
                        except:
                                pass
        else:
                INDEX()


def getChannels(url):
        if __settings__.getSetting('community_list') == "true":
            response = open(file, 'rb')
            link=response.read()
            soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        else:
            soup = BeautifulStoneSoup(file, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        channels = soup('channel')
        for channel in channels:
                name = channel('name')[0].string
                thumbnail = channel('thumbnail')[0].string
                try:
                        addDir(name,'',2,thumbnail)
                except:
                        pass
        else:
                INDEX()


def getChannelItems(name):
        if __settings__.getSetting('community_list') == "true":
            response = open(file, 'rb')
            link=response.read()
            soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        else:
            soup = BeautifulSOAP(file, convertEntities=BeautifulStoneSoup.XML_ENTITIES)

        channel_list = soup.find('channel', attrs={'name' : name})
        items = channel_list('item')
        for channel in channel_list('subchannel'):
                name = channel('name')[0].string
                thumb = channel('thumbnail')[0].string
                try:
                        addDir(name,'',3,thumb)
                except:
                        pass
        for item in items:
                try:
                        name = item('title')[0].string
                except:
                        pass

                try:
                        if __settings__.getSetting('mirror_link') == "true":
                                try:
                                        url = item('link')[1].string	
                                except:
                                        url = item('link')[0].string
                        if __settings__.getSetting('mirror_link_low') == "true":
                                try:
                                        url = item('link')[2].string	
                                except:
                                        try:
                                                url = item('link')[1].string
                                        except:
                                                url = item('link')[0].string
                        else:
                                url = item('link')[0].string
                except:
                        pass

                try:
                        thumbnail = item('thumbnail')[0].string
                except:
                        thumbnail = ''
                try:
                        addLink(url,name,thumbnail)
                except:
                        pass


def getSubChannelItems(name):
        if __settings__.getSetting('community_list') == "true":
            response = open(file, 'rb')
            link=response.read()
            soup = BeautifulSOAP(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        else:
            soup = BeautifulSOAP(file, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        channel_list = soup.find('subchannel', attrs={'name' : name})
        items = channel_list('subitem')
        for item in items:
                try:
                        name = item('title')[0].string
                except:
                        pass

                try:
                        if __settings__.getSetting('mirror_link') == "true":
                                try:
                                        url = item('link')[1].string	
                                except:
                                        url = item('link')[0].string
                        if __settings__.getSetting('mirror_link_low') == "true":
                                try:
                                        url = item('link')[2].string	
                                except:
                                        try:
                                                url = item('link')[1].string
                                        except:
                                                url = item('link')[0].string
                        else:
                                url = item('link')[0].string
                except:
                        pass

                try:
                        thumbnail = item('thumbnail')[0].string
                except:
                        thumbnail = ''
                try:
                        addLink(url,name,thumbnail)
                except:
                        pass


def INDEX():
        if __settings__.getSetting('community_list') == "true":
            response = open(file, 'rb')
            link=response.read()
            soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        else:
            soup = BeautifulStoneSoup(file, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        items = soup('item')
        for item in items:
                try:
                        name = item('title')[0].string
                except:
                        pass
                        name = ''
                try:
                        if __settings__.getSetting('mirror_link') == "true":
                                try:
                                        url = item('link')[1].string	
                                except:
                                        url = item('link')[0].string
                        if __settings__.getSetting('mirror_link_low') == "true":
                                try:
                                        url = item('link')[2].string	
                                except:
                                        try:
                                                url = item('link')[1].string
                                        except:
                                                url = item('link')[0].string
                        else:
                                url = item('link')[0].string
                except:
                        pass#url = item('link')[0].string
                try:
                        thumbnail = item('thumbnail')[0].string
                except:
                        thumbnail = ''
                try:
                        addLink(url,name,thumbnail)
                except:
                        pass	


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


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(url,name,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
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
        getStreams()

elif mode==1:
        print ""+url
        getChannels()

elif mode==2:
        print ""+url
        getChannelItems(name)

elif mode==3:
        print ""+url
        getSubChannelItems(name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
