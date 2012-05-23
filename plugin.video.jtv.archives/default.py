''' Credit to Stacked for the original plugin.'''

import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
try:
    import json
except:
    import simplejson as json
try:
    import StorageServer
except:
    import storageserverdummy as StorageServer

addon = xbmcaddon.Addon('plugin.video.jtv.archives')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
settings = xbmcaddon.Addon(id='plugin.video.jtv.archives')
home = settings.getAddonInfo('path')
ICON = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
fanart = os.path.join( home, 'fanart.jpg' )
user = settings.getSetting('j_user')
debug = settings.getSetting('debug')
cache = StorageServer.StorageServer("Jtv_Archives", 24)
profile_dir = xbmcvfs.exists(profile)
if not profile_dir:
    profile_dir = xbmcvfs.mkdir(profile)
favorites = xbmc.translatePath( os.path.join( profile, 'favorites' ) )
try:
    FAV = open(favorites).read()
except:
    FAV = None
search_q = xbmc.translatePath( os.path.join( profile, 'search_queries' ) )
try:
    SEARCH_LIST = open(search_q).read()
except:
    SEARCH_LIST = None
if debug == 'false':
    cache.dbg = False

LANGUAGES = {
    "sq" : "Albanian",
    "ar" : "Arabic",
    "hy" : "Belarusian",
    "bs" : "Bosnian",
    "bg" : "Bulgarian",
    "ca" : "Catalan",
    "zh" : "Chinese",
    "zh-TW" : "ChineseTW",
    "tl" : "Tagalog",
    "hr" : "Croatian",
    "cs" : "Czech",
    "da" : "Danish",
    "nl" : "Dutch",
    "en" : "English",
    "et" : "Estonian",
    "fa" : "Persian",
    "fi" : "Finnish",
    "fr" : "French",
    "de" : "German",
    "el" : "Greek",
    "he" : "Hebrew",
    "iw" : "Hebrew",
    "hi" : "Hindi",
    "hu" : "Hungarian",
    "is" : "Icelandic",
    "id" : "Indonesian",
    "it" : "Italian",
    "ja" : "Japanese",
    "ko" : "Korean",
    "lv" : "Latvian",
    "lt" : "Lithuanian",
    "mk" : "Macedonian",
    "no" : "Norwegian",
    "pl" : "Polish",
    "pt" : "Portuguese",
    "pt-br" : "PortugueseBrazil",
    "ro" : "Romanian",
    "ru" : "Russian",
    "sr" : "Serbian",
    "sk" : "Slovak",
    "sl" : "Slovenian",
    "es" : "Spanish",
    "sv" : "Swedish",
    "th" : "Thai",
    "tr" : "Turkish",
    "uk" : "Ukrainian",
    "vi" : "Vietnamese",
    "fa" : "Farsi",
    "pb" : "Portuguese",
    "pb" : "Brazilian"
    }


def get_request(url, headers=None):
        try:
            if headers is None:
                headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                           'Referer' : 'http://www.justin.tv/'}
            req = urllib2.Request(url,None,headers)
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            return link
        except urllib2.URLError, e:
            errorStr = str(e.read())
            if debug == 'true':
                print 'We failed to open "%s".' % url
            if hasattr(e, 'reason'):
                if debug == 'true':
                    print 'We failed to reach a server.'
                    print 'Reason: ', e.reason
            if hasattr(e, 'code'):
                if str(e.code) == '403':
                    if 'archive' in url:
                        xbmc.executebuiltin("XBMC.Notification(Jtv,No archives found for "+name+",5000,"+ICON+")")
                if debug == 'true':
                    print 'We failed with error code - %s.' % e.code
                xbmc.executebuiltin("XBMC.Notification(Jtv,HTTP ERROR: "+str(e.code)+",5000,"+ICON+")")


def getLanguageCode(language):
        for i in LANGUAGES.items():
            if i[1] == language:
                lang_code = i[0]
                return lang_code


def get_json():
        url = 'http://api.justin.tv/api/category/list.json'
        data = get_request(url)
        return(data, 200)


def Categories():
        if not FAV is None:
            addDir('Favorites','',5,xbmc.translatePath( os.path.join( home, 'resources', 'icons','fav.png' ) ),'','','')
        if not user == "":
            addDir(user+' Favorites / Follows','',11,xbmc.translatePath( os.path.join( home, 'resources', 'icons','jfav.png' ) ),'','','')
        addDir('All', '', 1, xbmc.translatePath( os.path.join( home, 'resources', 'icons','all.png' ) ),'','',1)
        result = cache.cacheFunction(get_json)
        data = json.loads(result[0])
        for i in data.keys():
            catId = i
            icon = xbmc.translatePath( os.path.join( home, 'resources', 'icons', data[i]['icon'].split('/')[-1]))
            name = data[i]['name']
            addDir(name, '', 6, icon,catId,'','')
        addDir('Search','',3,xbmc.translatePath( os.path.join( home, 'resources', 'icons', 'search.png' ) ),'','','')
        addDir('Enter Channel Name', '', 4, xbmc.translatePath( os.path.join( home, 'resources', 'icons','all.png' ) ),'','','')


def getSubcategories(catId, iconimage):
        addDir('All', '', 1, iconimage,catId,'',1)
        result = cache.cacheFunction(get_json)
        data = json.loads(result[0])
        for i in data[catId]['subcategories'].keys():
            name = data[catId]['subcategories'][i]['name']
            subCat = i
            addDir(name,'',1,iconimage,catId,subCat,1)


def getLiveData(subCat,catId,page):
        url = 'http://api.justin.tv/api/stream/list.json?'
        if not catId == '':
            url += 'category='+catId
            if not subCat == '':
                url +='&subcategory='+subCat
        if not settings.getSetting('lang') == "None":
            url += '&language='+getLanguageCode(settings.getSetting('lang'))
            if not settings.getSetting('lang1') == "None":
                url += ','+getLanguageCode(settings.getSetting('lang1'))
        if not page is None or page == '':
            url += '&limit=20&offset='+str((page -1) * 20)
        if debug == 'true':
            print '----LiveData: '+url
        Index(get_request(url), subCat, catId, page)


def getUserFavorites(user):
        url = 'http://api.justin.tv/api/user/favorites/'+user+'.json?limit=100'
        Index(get_request(url), '', '', None)


def Index(data, subCat, catId, page):
        if debug == 'true':
            print '--- json data ---'
            print data
        data = json.loads(data)
        if debug == 'true':
            print '----- Len Data = '+str(len(data))+' -----'
            print '----- page = '+str(page)+' -----'

        if len(data) == 20:
            if not page is None:
                addPage = page + 1
            else:
                addPage = 1
        else:
            addPage = None

        for i in data:
            try:
                subcat = i['channel']['subcategory_title']
                if subcat is None or subcat == '':
                    raise
            except:
                try:
                    subcat = i['subcategory']
                    if subcat is None:
                        raise
                except:
                    subcat = ''
            try:
                name = i['channel']['login']
                if name is None or name == '':
                    raise
            except:
                try:
                    name =  i['name'].split('user_')[-1]
                    if name is None or name == '':
                        raise
                except:
                    name = str(i['image_url_medium']).split('/')[-1].split('-')[0]
            try:
                title = i['channel']['status']
                if title is None or title == '':
                    raise
            except:
                try:
                    title = i['channel']['title']
                    if title is None or title == '':
                        raise
                except:
                    try:
                        title = i['title']
                        if title is None or title == '':
                            raise
                    except:
                        title = name
            try:
                timezone = i['channel']['timezone']
            except:
                timezone = ''
            try:
                bitrate = str(i['video_bitrate']).split('.')[0]
            except:
                bitrate = ''
            try:
                views = i['channel']['views_count']
            except:
                try:
                    views = i['channel_view_count']
                except:
                    views = ''
            try:
                lang = LANGUAGES[i['language']]
            except:
                lang = ''

            if settings.getSetting('fanart') == "true":
                try:
                    fanart = i['channel']['image_url_huge']
                except:
                    try:
                        fanart = i['image_url_huge']
                    except:
                        fanart = os.path.join( home, 'fanart.jpg' )
                if settings.getSetting('use_channel_icon') == "0":
                    thumb = fanart
                else:
                    try:
                        thumb = i['channel']['screen_cap_url_medium']
                    except:
                        try:
                            thumb = i['screen_cap_url_medium']
                        except:
                            thumb = ''
            else:
                fanart = os.path.join( home, 'fanart.jpg' )
                if settings.getSetting('use_channel_icon') == "0":
                    try:
                        thumb = i['channel']['image_url_medium']
                    except:
                        try:
                            thumb = i['image_url_medium']
                        except:
                            thumb = ''
                else:
                    try:
                        thumb = i['channel']['screen_cap_url_medium']
                    except:
                        try:
                            thumb = i['screen_cap_url_medium']
                        except:
                            thumb = ''

            try:
                description = i['channel']['title'].encode('ascii', 'ignore')
            except:
                try:
                    description = i['title'].encode('ascii', 'ignore')
                except:
                    description = ''
            description += '\n Channel Name: '+name.encode('ascii', 'ignore')+'\n Timezone: '+timezone+'\n Subcategory: '+subcat+'\n Bitrate: '+bitrate+'\n Language: '+lang+'\n Views: '+views
            addLiveLink(name,title,'',2,thumb,fanart,description)
        if not addPage is None:
            if addPage > page:
                addDir('Next Page', '', 1, xbmc.translatePath( os.path.join( home, 'resources', 'icons','next.png' ) ), catId, subCat, addPage)


def getVideos(name):
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://www.justin.tv/'+name}
        url = 'http://api.justin.tv/api/channel/archives/'+name+'.json'
        data = json.loads(get_request(url,headers))
        for i in data:
            url = i['video_file_url']
            title = i['title']
            part = 'Part: '+i['broadcast_part']
            if 'last_part' in i.keys():
                if i['last_part'] == 'true':
                    part += ' - Last Part'
            started = i['start_time']
            created = i['created_on']
            thumb = i['image_url_medium']
            duration = i['length']
            desc = part+'\nStarted: '+started+'\nCreated: '+created
            addLink(title+' - '+part,url,desc,duration,thumb)


def playLive(name, play=False, password=None):
        swf_url = getSwfUrl(name)
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : swf_url}
        url = 'http://usher.justin.tv/find/'+name+'.json?type=live&group='
        data = json.loads(get_request(url,headers))
        if data == []:
            if debug == 'true':
                print '---- No Data, Live? ----'
            xbmc.executebuiltin("XBMC.Notification(Jtv,Live Data Not Found,5000,"+ICON+")")
            return
        elif data[0]['needed_info'] == 'private':
            password = getPassword()
            if password is None:
                return
            url += '&private_code='+password
            data = json.loads(get_request(url,headers))
        try:
            token = ' jtv='+data[0]['token'].replace('\\','\\5c').replace(' ','\\20').replace('"','\\22')
        except:
            if debug == 'true':
                print '---- User Token Error ----'
            xbmc.executebuiltin("XBMC.Notification(Jtv,User Token Error ,5000,"+ICON+")")
            return
        rtmp = data[0]['connect']+'/'+data[0]['play']
        swf = ' swfUrl=%s swfVfy=1 live=1' % swf_url
        Pageurl = ' Pageurl=http://www.justin.tv/'+name
        url = rtmp+token+swf+Pageurl
        if play == True:
            info = xbmcgui.ListItem(name)
            playlist = xbmc.PlayList(1)
            playlist.clear()
            playlist.add(url, info)
            xbmc.executebuiltin('playlist.playoffset(video,0)')
        else:
            item = xbmcgui.ListItem(path=url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


def getSwfUrl(channel_name):
        """Helper method to grab the swf url, resolving HTTP 301/302 along the way"""
        base_url = 'http://www.justin.tv/widgets/live_embed_player.swf?channel=%s' % channel_name
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                   'Referer' : 'http://www.justin.tv/'+channel_name}
        req = urllib2.Request(base_url, None, headers)
        response = urllib2.urlopen(req)
        return response.geturl()


def getPassword():
        keyboard = xbmc.Keyboard('','Enter Password')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        password = keyboard.getText()
        if len(password) == 0:
            return None
        else:
            return password


def Search(name):
        if name == 'New Search':
            searchStr = ''
            keyboard = xbmc.Keyboard(searchStr,'Search')
            keyboard.doModal()
            if (keyboard.isConfirmed() == False):
                return
            newStr = keyboard.getText().replace(' ','+')
            if len(newStr) == 0:
                return
            if settings.getSetting('save_search') == 'true':
                search_file = xbmcvfs.exists(search_q)
                if not search_file:
                    search_file = xbmc.makeLegalFilename(search_q)
                    search_list = []
                else:
                    search_list = json.loads(open(search_q).read())
                search_list.append(newStr)
                a = open(search_q, "w")
                a.write(json.dumps(search_list))
                a.close()
            url =  'http://api.justin.tv/api/stream/search/'+newStr+'.json?limit=100'
            Index(get_request(url), '', '', 1)
        elif name == 'Previous Search Queries':
            search_list = json.loads(open(search_q).read())
            for i in search_list:
                addDir( i,'',12,xbmc.translatePath( os.path.join( home, 'resources', 'icons', 'search.png' ) ),'','','',True)
        else:
            url = 'http://api.justin.tv/api/stream/search/'+name+'.json?limit=100'
            Index(get_request(url), '', '', 1)


def remove_search(name):
        search_list = json.loads(open(search_q).read())
        for index in range(len(search_list)):
            try:
                if search_list[index]==name:
                     del search_list[index]
            except:
                pass
        a = open(search_q, "w")
        a.write(json.dumps(search_list))
        a.close()


def get_search():
        search_file = xbmcvfs.exists(search_q)
        if search_file:
            addDir('New Search','',12,xbmc.translatePath( os.path.join( home, 'resources', 'icons', 'search.png' ) ),'','','')
            addDir('Previous Search Queries','',12,xbmc.translatePath( os.path.join( home, 'resources', 'icons', 'search.png' ) ),'','','')
        else:
            Search('New Search')


def enterChannel():
        searchStr = ''
        keyboard = xbmc.Keyboard(searchStr,'Channel Name')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        newStr = keyboard.getText()
        if len(newStr) == 0:
            return
        try:
            url = 'http://api.justin.tv/api/stream/list.json?channel='+newStr
            Index(get_request(url), None, None, None)
        except:
            xbmc.executebuiltin("XBMC.Notification(Jtv,Nothing found for "+newStr+",5000,"+ICON+")")


def getFavorites():
        for i in json.loads(FAV):
            name = i[0]
            thumb = i[1]
            title = i[2]
            addLiveLink(name,title,'',2,thumb,thumb,'')


def addFavorite(name,thumb,title):
        keyboard = xbmc.Keyboard(title,'Rename?')
        keyboard.doModal()
        if (keyboard.isConfirmed() == False):
            return
        newTitle = keyboard.getText()
        if len(newTitle) == 0:
            return
        else:
            title = newTitle
        if not FAV is None:
            data = json.loads(FAV)
            data.append((name,thumb,title))
            a = open(favorites, "w")
            a.write(json.dumps(data))
            a.close()
        else:
            favorites_file = xbmcvfs.exists(favorites)
            if not favorites_file:
                favorites_file = xbmc.makeLegalFilename(favorites)
            fav_list = []
            fav_list.append((name,thumb,title))
            a = open(favorites, "w")
            a.write(json.dumps(fav_list))
            a.close()


def rmFavorite(name):
        data = json.loads(FAV)
        for index in range(len(data)):
            try:
                if data[index][0]==name:
                    del data[index]
                    a = open(favorites, "w")
                    a.write(json.dumps(data))
                    a.close()
            except:
                pass
        getFavorites()


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


def addDir(name,url,mode,iconimage,catId,subCat,page,showcontext=False):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&page="+str(page)+"&name="+urllib.quote_plus(name)+"&catId="+urllib.quote_plus(catId)+"&subCat="+urllib.quote_plus(subCat)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            if name in SEARCH_LIST:
                    contextMenu = [('Remove','XBMC.Container.Update(%s?url=&mode=13&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
                    liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def addLink(name,url,description,duration,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description, "Duration": duration })
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok


def addLiveLink(name,title,url,mode,iconimage,fanart,description,showcontext=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(title, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": title, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart)
        liz.setProperty('IsPlayable', 'true')
        if showcontext:
            try:
                if name in FAV:
                    contextMenu = [('Remove from Jtv Favorites','XBMC.Container.Update(%s?url=&mode=9&name=%s)' %(sys.argv[0], urllib.quote_plus(name))),
                    ('Get Channel Archives','XBMC.Container.Update(%s?url=&mode=7&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
                else:
                    contextMenu = [('Add to Jtv Favorites','XBMC.Container.Update(%s?url=&mode=8&name=%s&iconimage=%s&title=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(fanart), urllib.quote_plus(title.encode('ascii','ignore')))),
                    ('Get Channel Archives','XBMC.Container.Update(%s?url=&mode=7&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
            except:
                contextMenu = [('Add to Jtv Favorites','XBMC.Container.Update(%s?url=&mode=8&name=%s&iconimage=%s&title=%s)' %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(fanart), urllib.quote_plus(title.encode('ascii','ignore')))),
                ('Get Channel Archives','XBMC.Container.Update(%s?url=&mode=7&name=%s)' %(sys.argv[0], urllib.quote_plus(name)))]
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


params=get_params()

try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass

xbmcplugin.setContent(int(sys.argv[1]), 'movies')

url=None
name=None
mode=None
catId=None
subCat=None
page=None
play=None

try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    title=urllib.unquote_plus(params["title"])
except:
    pass
try:
    catId=urllib.unquote_plus(params["catId"])
except:
    pass
try:
    subCat=urllib.unquote_plus(params["subCat"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    mode=int(params["mode"])
except:
    pass
try:
    page=int(params["page"])
except:
    pass
try:
    play=params["play"]
except:
    pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "catId: "+str(catId)

if mode==None:
    print ""
    Categories()

elif mode==1:
    print ""
    getLiveData(subCat,catId,page)
    if not settings.getSetting('view_mode') == "0":
        try:
        # if (xbmc.getSkinDir() == "skin.confluence"):
            if settings.getSetting('view_mode') == "1": # List
                xbmc.executebuiltin('Container.SetViewMode(502)')
            if settings.getSetting('view_mode') == "2": # Big List
                xbmc.executebuiltin('Container.SetViewMode(51)')
            if settings.getSetting('view_mode') == "3": # Thumbnails
                xbmc.executebuiltin('Container.SetViewMode(500)')
            if settings.getSetting('view_mode') == "4": # Poster Wrap
                xbmc.executebuiltin('Container.SetViewMode(501)')
            if settings.getSetting('view_mode') == "5": # Fanart
                xbmc.executebuiltin('Container.SetViewMode(508)')
            if settings.getSetting('view_mode') == "6":  # Media info
                xbmc.executebuiltin('Container.SetViewMode(504)')
            if settings.getSetting('view_mode') == "7": # Media info 2
                xbmc.executebuiltin('Container.SetViewMode(503)')
        except:
            print "SetViewMode Failed: "+settings.getSetting('view_mode')
            print "Skin: "+xbmc.getSkinDir()

elif mode==2:
    print ""
    if play == 'True':
        playLive(name, True)
    else:
        playLive(name)

elif mode==3:
    print ""
    get_search()

elif mode==4:
    print ""
    enterChannel()

elif mode==5:
    print ""
    getFavorites()

elif mode==6:
    print ""
    getSubcategories(catId, iconimage)

elif mode==7:
    print ""
    getVideos(name)

elif mode==8:
    print ""
    addFavorite(name,iconimage,title)

elif mode==9:
    print ""
    rmFavorite(name)

elif mode==10:
    print ""

elif mode==11:
    print ""
    getUserFavorites(user)

elif mode==12:
    print ""
    Search(name)

elif mode==13:
    print ""
    remove_search(name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))