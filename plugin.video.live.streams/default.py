# -*- coding: utf-8 -*-

import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
try:
    import json
except:
    import simplejson as json

addon = xbmcaddon.Addon('plugin.video.live.streams')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
__settings__ = xbmcaddon.Addon(id='plugin.video.live.streams')
home = __settings__.getAddonInfo('path')
favorites = os.path.join( profile, 'favorites' )
REV = xbmc.translatePath( os.path.join( profile, 'list_revision') )
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = xbmc.translatePath( os.path.join( home, 'fanart.jpg' ) )
source_file = xbmc.translatePath( os.path.join( profile, 'source_file') )
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
if os.path.exists(source_file)==True:
    SOURCES = open(source_file).read()

def getSources():
        if os.path.exists(favorites)==True:
            addDir('Favorites','url',4,xbmc.translatePath(os.path.join(home, 'resources', 'favorite.png')),fanart,'','','',False)
        if os.path.exists(source_file)==False:
            xbmc.executebuiltin("XBMC.Notification(LiveStreams,Choose type source and then select Add Source.,15000,"+icon+")")
            __settings__.openSettings()
            return
        a = open(source_file,"r").read()
        sources = json.loads(a)
        if len(sources) > 1:
            for i in sources:
                addDir(i[0],i[1],1,icon,fanart,'','','')
        else:
            getData(sources[0][1],fanart)


def addSource(new="false"):
        if __settings__.getSetting("choose_source") == "0":
           source = __settings__.getSetting('new_file_source')
        if __settings__.getSetting("choose_source") == "1":
           source = __settings__.getSetting('new_url_source')
        if source == '':
            return
        if '/' in source:
            nameStr = source.split('/')[-1].split('.')[0]
        if '\\' in source:
            nameStr = source.split('\\')[-1].split('.')[0]
        if '%' in nameStr:
            nameStr = urllib.unquote_plus(nameStr)
        keyboard = xbmc.Keyboard(nameStr,'Displayed Name, Rename?')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        newStr = keyboard.getText()
        if len(newStr) == 0:
            return
        source_list = []
        source = (newStr, source)
        if os.path.exists(source_file)==False:
            source_list.append(source)
            b = open(source_file,"w")
            b.write(json.dumps(source_list))
            b.close()
        else:
            a = open(source_file,"r").read()
            sources = json.loads(a)
            sources.append(source)
            b = open(source_file,"w")
            b.write(json.dumps(sources))
            b.close()
        __settings__.setSetting('new_url_source', "")
        __settings__.setSetting('new_file_source', "")
        xbmc.executebuiltin("XBMC.Notification(LiveStreams,New source added.,5000,"+icon+")")

def rmSource(name):
        a = open(source_file,"r").read()
        sources = json.loads(a)
        for index in range(len(sources)):
            try:
                print index
                if sources[index][0] == name:
                    del sources[index]
                b = open(source_file,"w")
                b.write(json.dumps(sources))
                b.close()
            except:
                print index


def getUpdate():
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
            if os.path.exists(__settings__.getSetting('save_location'))==False:
                try:
                    name = xbmc.makeLegalFilename(os.path.join(__settings__.getSetting('save_location'), '%s') % name)
                except:
                    print '------ Error makeLegalFilename -----'
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
        xbmc.executebuiltin("XBMC.Notification(LiveStreams,Community Lists Updated,5000,"+icon+")")


def checkForUpdate():
        url = 'http://community-links.googlecode.com/svn/trunk/'
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        revision = re.compile('<html><head><title>(.+?)/trunk</title></head>').findall(link)[0]
        try:
            R = open(REV,"r")
            rev = R.read()
            R.close()
        except:
            getUpdate()
            print "No REV file found."
            pass
        try:
            revision_check = re.compile('<html><head><title>(.+?)/trunk</title></head>').findall(rev)[0]
            if revision_check != revision:
                getUpdate()
        except:
            print '----- Error: revision_check ------'


if __settings__.getSetting('community_list') == "true":
    if __settings__.getSetting('save_location') == "":
        xbmc.executebuiltin("XBMC.Notification('LiveStreams','Choose a location to save files and select OK to save.',15000,"+icon+")")
        __settings__.openSettings()
    else:
        try:
            checkForUpdate()
        except urllib2.URLError, e:
            errorStr = str(e.read())
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            if hasattr(e, 'code'):
                print 'We failed with error code - %s.' % e.code


def getSoup(url):
        print 'getSoup(): '+url
        if url.startswith('http://'):
            try:
                req = urllib2.Request(url)
                response = urllib2.urlopen(req)
                data = response.read()
                response.close()
            except urllib2.URLError, e:
                # errorStr = str(e.read())
                if hasattr(e, 'code'):
                    print 'We failed with error code - %s.' % e.code
                    xbmc.executebuiltin("XBMC.Notification(LiveStreams,We failed with error code - "+str(e.code)+",10000,"+icon+")")
                elif hasattr(e, 'reason'):
                    print 'We failed to reach a server.'
                    print 'Reason: ', e.reason
                    xbmc.executebuiltin("XBMC.Notification(LiveStreams,We failed to reach a server. - "+str(e.reason)+",10000,"+icon+")")
        else:
            data = open(url, 'r').read()
        soup = BeautifulSOAP(data, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        return soup


def getData(url,fanart):
        soup = getSoup(url)
        if len(soup('channels')) > 0:
            channels = soup('channel')
            for channel in channels:
                name = channel('name')[0].string
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    thumbnail = ''
                    
                try:    
                    if not channel('fanart'):
                        if __settings__.getSetting('use_thumb') == "true":
                            fanArt = thumbnail
                        else:
                            fanArt = fanart
                    else:
                        fanArt = channel('fanart')[0].string
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart
                    
                try:
                    desc = channel('info')[0].string
                except:
                    desc = ''

                try:
                    genre = channel('genre')[0].string
                except:
                    genre = ''

                try:
                    date = channel('date')[0].string
                except:
                    date = ''
                try:
                    addDir(name.encode('utf-8', 'ignore'),url,2,thumbnail,fanArt,desc,genre,date)
                except:
                    print 'There was a problem adding directory from getData(): '+name.encode('utf-8', 'ignore')
        else:
            fanArt = fanart
            getItems(soup('item'),fanArt)


def getChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('channel', attrs={'name' : name})
        items = channel_list('item')
        try:
            fanArt = channel_list('fanart')[0].string
            if fanArt == None:
                raise
        except:
            fanArt = fanart
        for channel in channel_list('subchannel'):
            name = channel('name')[0].string
            try:
                thumbnail = channel('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:    
                if not channel('fanart'):
                    if __settings__.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                else:
                    fanArt = channel('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                pass
            try:
                desc = channel('info')[0].string
            except:
                desc = ''

            try:
                genre = channel('genre')[0].string
            except:
                genre = ''

            try:
                date = channel('date')[0].string
            except:
                date = ''
            try:
                addDir(name.encode('utf-8', 'ignore'),url,3,thumbnail,fanArt,desc,genre,date)
            except:
                print 'There was a problem adding directory - '+name.encode('utf-8', 'ignore')
        print fanArt
        getItems(items,fanArt)


def getSubChannelItems(name,url,fanart):
        soup = getSoup(url)
        channel_list = soup.find('subchannel', attrs={'name' : name})
        items = channel_list('subitem')
        getItems(items,fanart)


def getItems(items,fanart):
        for item in items:
            try:
                name = item('title')[0].string
            except:
                print '-----Name Error----'
                name = ''
            try:
                if item('epg'):
                    if item('epg')[0].string > 1:
                        name += getepg(item('epg')[0].string)
                else:
                    pass
            except:
                print '----- EPG Error ----'

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
                print '---- URL Error Passing ----'+name
                pass

            try:
                thumbnail = item('thumbnail')[0].string
                if thumbnail == None:
                    raise
            except:
                thumbnail = ''
            try:    
                if not item('fanart'):
                    if __settings__.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                    else:
                        fanArt = fanart
                else:
                    fanArt = item('fanart')[0].string
                if fanArt == None:
                    raise
            except:
                fanArt = fanart
            try:
                desc = item('info')[0].string
            except:
                desc = ''

            try:
                genre = item('genre')[0].string
            except:
                genre = ''

            try:
                date = item('date')[0].string
            except:
                date = ''
            try:
                addLink(url,name.encode('utf-8', 'ignore'),thumbnail,fanArt,desc,genre,date,True)
            except:
                print 'There was a problem adding link - '+name.encode('utf-8', 'ignore')


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


def getFavorites():
        for i in json.loads(open(favorites).read()):
            name = i[0]
            url = i[1]
            iconimage = i[2]
            if __settings__.getSetting('use_thumb') == "true":
                fanArt = iconimage
            else:
                try:
                    fanArt = i[3]
                    if fanArt == None:
                        raise
                except:
                    fanArt = fanart
            addLink(url,name,iconimage,fanArt,'','','')


def addFavorite(name,url,iconimage,fanart):
        favList = []
        if os.path.exists(favorites)==False:
            print 'Making Favorites File'
            favList.append((name,url,iconimage,fanart))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            print 'Appending Favorites'
            a = open(favorites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart))
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()


def rmFavorite(name):
        print 'Remove Favorite'
        a = open(favorites).read()
        data = json.loads(a)
        for index in range(len(data)):
            try:
                if data[index][0]==name:
                    del data[index]
                    b = open(favorites, "w")
                    b.write(json.dumps(data))
                    b.close()
            except:
                pass


def addDir(name,url,mode,iconimage,fanart,description,genre,date,showcontext=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "Date": date } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext == True:
            try:
                if name in SOURCES:
                    contextMenu = [('Remove from Sources','XBMC.Container.Update(%s?mode=8&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
                    liz.addContextMenuItems(contextMenu, True)
            except:
                pass
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addLink(url,name,iconimage,fanart,description,genre,date,showcontext=True):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "Date": date } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            try:
                if name in FAV:
                    contextMenu = [('Remove from LiveStreams Favorites','XBMC.Container.Update(%s?mode=6&name=%s&url=%s&iconimage=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage)))]
                else:
                    contextMenu = [('Add to LiveStreams Favorites','XBMC.Container.Update(%s?mode=5&name=%s&url=%s&iconimage=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage)))]
            except:
                contextMenu = [('Add to LiveStreams Favorites','XBMC.Container.Update(%s?mode=5&name=%s&url=%s&iconimage=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage)))]
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


  # Thanks to daschacka, an epg scraper for http://i.teleboy.ch/programm/station_select.php - http://forum.xbmc.org/showpost.php?p=936228&postcount=1076
def getepg(link):
        url=urllib.urlopen(link)
        source=url.read()
        url.close()
        source2 = source.split("Jetzt")
        source3 = source2[1].split('programm/detail.php?const_id=')
        sourceuhrzeit = source3[1].split('<br /><a href="/')
        nowtime = sourceuhrzeit[0][40:len(sourceuhrzeit[0])]
        sourcetitle = source3[2].split("</a></p></div>")
        nowtitle = sourcetitle[0][17:len(sourcetitle[0])]
        nowtitle = nowtitle.replace("ö","oe")
        nowtitle = nowtitle.replace("ä","ae")
        nowtitle = nowtitle.replace("ü","ue")
        return "  - "+nowtitle+" - "+nowtime


xbmcplugin.setContent(int(sys.argv[1]), 'movies')
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
except:
    pass

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
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
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
    print "getSources"
    getSources()

elif mode==1:
    print "getData"
    getData(url,fanart)

elif mode==2:
    print "getChannelItems"
    getChannelItems(name,url,fanart)

elif mode==3:
    print ""
    getSubChannelItems(name,url,fanart)

elif mode==4:
    print ""
    getFavorites()

elif mode==5:
    print ""
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart)
    getFavorites()

elif mode==6:
    print ""
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
    getFavorites()
    
elif mode==7:
    print "addSource"
    addSource(url)

elif mode==8:
    print "rmSource"
    rmSource(name)

elif mode==9:
    print "getUpdate"
    getUpdate()

xbmcplugin.endOfDirectory(int(sys.argv[1]))