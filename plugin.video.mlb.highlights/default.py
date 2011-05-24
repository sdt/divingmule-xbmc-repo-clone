import urllib,urllib2,re,os,cookielib,datetime
import xbmcplugin,xbmcgui,xbmcaddon
import simplejson as json
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP


__settings__ = xbmcaddon.Addon(id='plugin.video.mlb.highlights')
addon = xbmcaddon.Addon('plugin.video.mlb.highlights')
profile = xbmc.translatePath(addon.getAddonInfo('profile'))
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )
SCENARIO = __settings__.getSetting('scenario')
SESSIONKEY = os.path.join( profile, 'sessionkey')
COOKIEFILE = os.path.join( profile, 'mlbcookie.lwp')
SOAPCODES = {
    "1"    : "OK",
    "-1000": "Requested Media Not Found",
    "-1500": "Other Undocumented Error",
    "-2000": "Authentication Error",
    "-2500": "Blackout Error",
    "-3000": "Identity Error",
    "-3500": "Sign-on Restriction Error",
    "-4000": "System Error",
    }


print '(((((((((((((((((((  Revision r33    ))))))))))))))))'

def categories():
        addDir("Today's Games",'http://mlb.mlb.com/gdcross/components/game/mlb/'+dateStr.day[0]+'/master_scoreboard.json',6,icon)
        addDir("Yesterday's Games",'http://mlb.mlb.com/gdcross/components/game/mlb/'+dateStr.day[1]+'/master_scoreboard.json',6,icon)
        addDir("Tomorrow's Games",'http://mlb.mlb.com/gdcross/components/game/mlb/'+dateStr.day[2]+'/master_scoreboard.json',6,icon)
        #addDir('Play Latest Videos','http://mlb.mlb.com/video/play.jsp?tcid=mm_mlb_vid',3,icon)
        addDir('MLB.com Realtime Highlights','http://gdx.mlb.com/components/game/mlb/'+dateStr.day[0]+'/media/highlights.xml',8,icon)
        addDir('Videos by Team','',4,icon)
        addDir('Latest Videos','http://mlb.mlb.com/video/play.jsp?tcid=mm_mlb_vid',10,icon)
        addDir('FastCast','http://mlb.mlb.com/ws/search/MediaSearchService?mlbtax_key=fastcast&sort=desc&sort_type=date&hitsPerPage=200&src=vpp',1,icon)
        addDir('Must C','http://mlb.mlb.com/ws/search/MediaSearchService?mlbtax_key=must_c&sort=desc&sort_type=date&hitsPerPage=200&src=vpp',1,icon)
        addDir('Game Recaps','http://mlb.mlb.com/ws/search/MediaSearchService?&sort=desc&sort_type=date&subject=MLBCOM_GAME_RECAP&hitsPerPage=60&src=vpp',1,icon)
        addDir('MLB Network','http://mlb.mlb.com/ws/search/MediaSearchService?mlbtax_key=mlb_network&sort=desc&sort_type=date&hitsPerPage=360&src=vpp',1,icon)
        addDir('Top Plays','http://mlb.mlb.com/ws/search/MediaSearchService?&sort=desc&sort_type=date&subject=MLBCOM_TOP_PLAY&hitsPerPage=60&src=vpp',1,icon)
        addDir("Baseball's Best Moments",'http://mlb.mlb.com/video/play.jsp?topic_id=7759164',10,icon)

def getTeams():
        url='http://mlb.mlb.com/video/index.jsp'
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://mlb.mlb.com'),
                ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulSoup(link)
        teams = soup.find('ul', attrs={'id' : "teamVlpNav"})('li')
        for team in teams:
                name = team('a')[0]['title']
                url = str(team('a')[0]['href'])[-3:].replace('=','')
                addDir(name,url,5,icon)
                

def getRealtimeVideo(url):
        try:
            req = urllib2.Request(url)
            req.addheaders = [('Referer', 'http://mlb.mlb.com/index.jsp'),
                              ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
            soup = BeautifulStoneSoup(link)
            videos = soup.findAll('media')
            for video in videos:
                name = video.headline.string
                vidId = video['id']
                url = vidId[-3]+'/'+vidId[-2]+'/'+vidId[-1]+'/'+vidId
                duration = video.duration.string
                thumb = video.thumb.string
                addLink(name,'http://mlb.mlb.com/gen/multimedia/detail/'+url+'.xml',duration,2,thumb)
        except:
            pass
        addDir("Yesterday's MLB.com Realtime Highlights",'http://gdx.mlb.com/components/game/mlb/'+dateStr.day[1]+'/media/highlights.xml',8,icon)


def getTeamVideo(url):
        url='http://mlb.mlb.com/gen/'+url+'/components/multimedia/topvideos.xml'
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://mlb.mlb.com'),
                ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulStoneSoup(link, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        videos = soup('item')
        for video in videos:
                name = video('title')[0].string
                thumb = video('picture', attrs={'type' : "dam-raw-thumb"})[0]('url')[0].string
                if video('url', attrs={'speed' : "1200"}):
                        url = video('url', attrs={'speed' : "1200"})[0].string
                elif video('url', attrs={'speed' : "1000"}):
                        url = video('url', attrs={'speed' : "1000"})[0].string
                elif video('url', attrs={'speed' : "800"}):
                        url = video('url', attrs={'speed' : "800"})[0].string
                duration = video('duration')[0].string
                desc = video('big_blurb')[0].string
                addTeamLink(name,url,desc,duration,thumb)
        

def scrapeWebsite(url):
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        req.addheaders = [('Referer', 'http://mlb.mlb.com'),
                ('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3')]
        link=response.read()
        response.close()
        soup = BeautifulSoup(link, convertEntities=BeautifulSoup.HTML_ENTITIES)
        videos = soup.find('div', attrs={'id' : "playlistWrap"})('li')
        for video in videos:
            name = video('p')[0].string
            try:
                thumb = video('img')[0]['data-src']
            except:
                thumb = video('img')[0]['src']
            content = video('a')[0]['rel']
            url = content[-3]+'/'+content[-2]+'/'+content[-1]+'/'+content
            duration = video('div', attrs={'class' : "duration"})[0].string[-5:]
            addLink(name,'http://mlb.mlb.com/gen/multimedia/detail/'+url+'.xml',duration,2,thumb)

        
def playLatest(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://mlb.mlb.com/video/play.jsp?cid=mlb'),
                ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        data = json.loads(link)
        videos = data['mediaContent']
        playlist = xbmc.PlayList(1)
        playlist.clear()
        for video in videos:
                name = video['blurb']
                link = video['url']
                thumb = video['thumbnails'][2]['src']
                url = getVideoURL(link)
                info = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
                playlist.add(url, info)
        play=xbmc.Player().play(playlist)


def getVideos(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://mlb.mlb.com/video/play.jsp?cid=mlb'),
                ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        data = json.loads(link)
        videos = data['mediaContent']
        for video in videos:
                name = video['blurb']
                desc = video['bigBlurb']
                url = video['url']
                thumb = video['thumbnails'][2]['src']
                addLink(name,url,'',2,thumb)


def setVideoURL(url):
        url = getVideoURL(url)
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


        
def getVideoURL(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://mlb.mlb.com/video/play.jsp?cid=mlb'),
                ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        soup = BeautifulStoneSoup(link)
        if soup.find('url', attrs={'playback_scenario' : "FLASH_1200K_640X360"}):
                url = soup.find('url', attrs={'playback_scenario' : "FLASH_1200K_640X360"}).string
        elif soup.find('url', attrs={'playback_scenario' : "FLASH_1000K_640X360"}):
                url = soup.find('url', attrs={'playback_scenario' : "FLASH_1000K_640X360"}).string
        elif soup.find('url', attrs={'playback_scenario' : "FLASH_600K_400X224"}):
                url = soup.find('url', attrs={'playback_scenario' : "FLASH_600K_400X224"}).string
        return url


def getGames(url):
        req = urllib2.Request(url)
        req.addheaders = [('Referer', 'http://mlb.mlb.com/index.jsp'),
                        ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        data = json.loads(link)
        games = data['data']['games']['game']
        for game in games:
                home_team = game['home_team_city']
                away_team = game['away_team_city']
                game_id = game['game_pk']
                status = game['status']['status']
                if status == 'ind' or status == 'Preview':
                        status = str(game['time']) + ' ' + str(game['time_zone'])
                        
                try:
                        thumb = game['video_thumbnail']
                except:
                        thumb = ''
                        
                try:
                        event_id = game['game_media']['media'][0]['calendar_event_id']
                except:
                        try:
                                event_id = game['game_media']['media']['calendar_event_id']
                        except:
                                event_id = ''
                                
                try:
                        content_id = game['game_media']['media'][1]['content_id']
                except:
                        content_id = ''
                        
                try:
                        free_game = game['game_media']['media']['free']
                        if free_game == 'ALL':
                                free = ' Free Game'
                        else:
                                free = ''
                except:
                            free = ''  

                try:
                        media_state = game['game_media']['media']['media_state']
                except:
                        try:
                                media_state = game['game_media']['media'][0]['media_state']
                        except:
                                media_state = ''
                                
                if status == 'In Progress':
                        try:
                                desc = str(game['alerts']['text'])+' '+str(game['status']['inning_state'])+' '+str(game['status']['inning'])
                        except:
                                desc = ''
                        try:
                                inning = str(game['status']['inning_state'])+' '+str(game['status']['inning'])
                                print '------------> there are innings'
                        except:
                                inning = ''
                else:
                        desc = ''
                        inning = ''
                
                
                description = desc        
                name = away_team+' @ '+home_team+' - '+status+' '+free
                u=sys.argv[0]+"?url=&mode=7&name="+urllib.quote_plus(name)+"&event="+urllib.quote_plus(event_id)+"&content="+urllib.quote_plus(content_id)
                if media_state == 'media_on':
                        label1=coloring( name,"green",name )
                        label2=coloring( inning,"blue",inning )
                        liz=xbmcgui.ListItem( label1+' '+label2,iconImage="DefaultVideo.png", thumbnailImage=thumb)
                        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
                else:
                        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumb)
                        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)            
 

def mlbGame(event_id,content_id):

        try:
            os.remove(COOKIEFILE)
        except:
            pass
         
        cj = cookielib.LWPCookieJar()

        if cj != None:
           if os.path.isfile(COOKIEFILE):
              cj.load(COOKIEFILE)
           if cookielib:
              opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
              urllib2.install_opener(opener)

        # Get the cookie first
        theurl = 'https://secure.mlb.com/enterworkflow.do?flowId=registration.wizard&c_id=mlb'
        txheaders = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'}
        data = None
        req = urllib2.Request(theurl,data,txheaders)
        response = urllib2.urlopen(req)
        print 'These are the cookies we have received so far :'
        for index, cookie in enumerate(cj):
            print index, '  :  ', cookie
        try:
            cj.save(COOKIEFILE,ignore_discard=True) 
        except:
            pass

        # now authenticate
        theurl = 'https://secure.mlb.com/authenticate.do'
        txheaders = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13',
                     'Referer' : 'https://secure.mlb.com/enterworkflow.do?flowId=registration.wizard&c_id=mlb'}
        values = {'uri' : '/account/login_register.jsp',
                  'registrationAction' : 'identify',
                  'emailAddress' : __settings__.getSetting('email'),
                  'password' : __settings__.getSetting('password')}

        data = urllib.urlencode(values)
        try:
           req = urllib2.Request(theurl,data,txheaders)
           response = urllib2.urlopen(req)
        except IOError, e:
           print 'We failed to open "%s".' % theurl
           if hasattr(e, 'code'):
               print 'We failed with error code - %s.' % e.code
           elif hasattr(e, 'reason'):
               print "The error object has the following 'reason' attribute :", e.reason
               print "This usually means the server doesn't exist, is down, or we don't have an internet connection."
               return

        else:
            print 'Here are the headers of the page :'
            print response.info()                             # handle.read() returns the page, handle.geturl() returns the true url of the page fetched (in case urlopen has followed any redirects, which it sometimes does)

        if cj == None:
            print "We don't have a cookie library available - sorry."
            print "I can't show you any cookies."
        else:
            print 'These are the cookies we have received so far :'
            for index, cookie in enumerate(cj):
                print index, '  :  ', cookie        
            try:
                cj.save(COOKIEFILE,ignore_discard=True) 
            except:
                pass

        page = response.read()
        pattern = re.compile(r'Welcome to your personal (MLB|mlb).com account.')
        try:
            loggedin = re.search(pattern, page).groups()
            print "Logged in successfully!"
        except:
            pass
            #raise Exception,page

        # Begin MORSEL extraction
        ns_headers = response.headers.getheaders("Set-Cookie")
        attrs_set = cookielib.parse_ns_headers(ns_headers)
        cookie_tuples = cookielib.CookieJar()._normalized_cookie_tuples(attrs_set)
        print repr(cookie_tuples)
        cookies = {}
        for tup in cookie_tuples:
            name, value, standard, rest = tup
            cookies[name] = value
        print repr(cookies)
        #print "ipid = " + str(cookies['ipid']) + " fingerprint = " + str(cookies['fprt'])
        #print "session-key = " + str(cookies['ftmu'])
        #sys.exit()
        # End MORSEL extraction


        # pick up the session key morsel
        theurl = 'http://mlb.mlb.com/enterworkflow.do?flowId=media.media'
        txheaders = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'}
        data = None
        req = urllib2.Request(theurl,data,txheaders)
        response = urllib2.urlopen(req)

        # Begin MORSEL extraction
        ns_headers = response.headers.getheaders("Set-Cookie")
        attrs_set = cookielib.parse_ns_headers(ns_headers)
        cookie_tuples = cookielib.CookieJar()._normalized_cookie_tuples(attrs_set)
        print repr(cookie_tuples)
        #cookies = {}
        for tup in cookie_tuples:
            name, value, standard, rest = tup
            cookies[name] = value
        #print repr(cookies)
        #print "ipid = " + str(cookies['ipid']) + " fingerprint = " + str(cookies['fprt'])
        try:
            print "session-key = " + str(cookies['ftmu'])
            session_key = urllib.unquote(cookies['ftmu'])
            sk = open(SESSIONKEY,"w")
            sk.write(session_key)
            sk.close()

        except:
            session_key = None
            logout_url = 'https://secure.mlb.com/enterworkflow.do?flowId=registration.logout&c_id=mlb'
            txheaders = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13',
                     'Referer' : 'http://mlb.mlb.com/index.jsp'}
            data = None
            req = urllib2.Request(logout_url,data,txheaders)
            response = urllib2.urlopen(req)
            logout_info = response.read()
            response.close()
            print "No session key, so logged out."
            #session = None

        values = {
            'eventId': event_id, 
            'sessionKey': session_key,
            'fingerprint': urllib.unquote(cookies['fprt']),
            'identityPointId': cookies['ipid'],
            'subject':'LIVE_EVENT_COVERAGE'
        }
        theUrl = 'https://secure.mlb.com/pubajaxws/bamrest/MediaService2_0/op-findUserVerifiedEvent/v-2.1?' +\
            urllib.urlencode(values)
        req = urllib2.Request(theUrl, None, txheaders);
        response = urllib2.urlopen(req).read()
        print response

        soup = BeautifulSOAP(response)
        status = soup.find('status-code').string
        if status != "1":
            error_str = SOAPCODES[status]
            xbmc.executebuiltin("XBMC.Notification('MLB','Status : "+error_str+"',10000,"+icon+")")
            return

        items = soup.findAll('user-verified-content', attrs={'type' : 'video'})
        session = soup.find('session-key').string
        event_id = soup.find('event-id').string
        for item in items:
                content_id = item('content-id')[0].string
                blackout_status = item('blackout-status')[0].string
                try:
                    blackout = item('blackout')[0].string.replace('_',' ')
                except:
                    blackout = ''
                call_letters = item('domain-attribute', attrs={'name' : "call_letters"})[0].string
                if item('domain-attribute', attrs={'name' : "home_team_id"})[0].string == item('domain-attribute', attrs={'name' : "coverage_association"})[0].string:
                    coverage = "Home Team Coverage"
                elif item('domain-attribute', attrs={'name' : "away_team_id"})[0].string == item('domain-attribute', attrs={'name' : "coverage_association"})[0].string:
                    coverage = "Away Team Coverage"
                else:
                    coverage = ''
                if blackout_status == '<successstatus></successstatus>':
                    name = coverage+' - '+call_letters
                else:
                    name = coverage+' '+call_letters+' '+blackout
                    
                u=sys.argv[0]+"?url=&mode=9&name="+urllib.quote_plus(name)+"&event="+urllib.quote_plus(event_id)+"&content="+urllib.quote_plus(content_id)+"&session="+urllib.quote_plus(session)+"&cookieIp="+urllib.quote_plus(cookies['ipid'])+"&cookieFp="+urllib.quote_plus(cookies['fprt'])
                if blackout == '<successstatus></successstatus>':
                        label1=coloring( name,"green",name )
                        liz=xbmcgui.ListItem( label1,iconImage="DefaultVideo.png")
                        liz.setInfo( type="Video", infoLabels={ "Title": name } )
                else:
                        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
                        liz.setInfo( type="Video", infoLabels={ "Title": name } )
                liz.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)                      


def getGameURL(name,event,content,session,cookieIp,cookieFp):
        print "Event-id = " + str(event) + " and content-id = " + str(content) + "Name = " + name + "Session = " + session + "cookieIp = " + cookieIp + "cookieFp = " + cookieFp
        txheaders = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'}
        values = {
            'subject':'LIVE_EVENT_COVERAGE',
            'sessionKey': session,
            'identityPointId': cookieIp,
            'contentId': content,
            'playbackScenario': SCENARIO,
            'eventId': event, 
            'fingerprint': cookieFp,
        }
        theUrl = 'https://secure.mlb.com/pubajaxws/bamrest/MediaService2_0/op-findUserVerifiedEvent/v-2.1?' +\
            urllib.urlencode(values)
        req = urllib2.Request(theUrl, None, txheaders);
        response = urllib2.urlopen(req).read()
        print response
        #sys.exit()
        #el = xml.etree.ElementTree.XML(response)
        soup = BeautifulStoneSoup(response, convertEntities=BeautifulStoneSoup.XML_ENTITIES)
        status = soup.find('status-code').string
        # utag = re.search('(\{.*\}).*', el.tag).group(1)
        # status = el.find(utag + 'status-code').text

        if status != "1":
            error_str = SOAPCODES[status]
            xbmc.executebuiltin("XBMC.Notification('MLB','Status : "+error_str+"',10000,"+icon+")")
            return

        if soup.find('state').string == 'MEDIA_OFF':
            print 'Status : Media Off'
            try:
                preview = soup.find('preview-url').contents[0]
                if re.search('innings-index',str(preview)):
                    print '------> research'
                    raise Exception
                    print preview
                else:
                    xbmc.executebuiltin("XBMC.Notification('MLB','Status : "+blackout+" - Playing Preview',10000,"+icon+")")
                    item = xbmcgui.ListItem(path=preview)
                    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
            except:
                xbmc.executebuiltin("XBMC.Notification('MLB','Status : Media Off',5000,"+icon+")")
                return 

            
        elif str(soup.find('blackout-status').next) != '<successstatus></successstatus>':
            try:
                blackout = item('blackout')[0].string.replace('_',' ')
            except:
                blackout = 'Blackout'
            try:
                preview = soup.find('preview-url').contents[0]
                if re.search('innings-index',str(preview)):
                    print '------> research'
                    raise Exception
                    print preview
                else:
                    xbmc.executebuiltin("XBMC.Notification('MLB','Status : "+blackout+" - Playing Preview',10000,"+icon+")")
                    item = xbmcgui.ListItem(path=preview)
                    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
            except:

                xbmc.executebuiltin("XBMC.Notification('MLB','Status : "+blackout+"',5000,"+icon+")")
                return    
        
        elif str(soup.find('auth-status').next) == '<notauthorizedstatus></notauthorizedstatus>':
            print 'Status : Not Authorized'
            try:
                preview = soup.find('preview-url').contents[0]
                if re.search('innings-index',str(preview)):
                    print '------> research'
                    raise Exception
                    print preview
                else:
                    xbmc.executebuiltin("XBMC.Notification('MLB','Status : Not Authorized - Playing Preview',10000,"+icon+")")
                    item = xbmcgui.ListItem(path=preview)
                    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
            except:
                xbmc.executebuiltin("XBMC.Notification('MLB','Status : Not Authorized',5000,"+icon+")")
                return
                
        else:
            try:
                game_url = soup.findAll('user-verified-content')[0]('user-verified-media-item')[0]('url')[0].string
                print '$$$$$----------> game_url: '+game_url
            except:
                print '-----------------> divingmule needs to work on the soup!'

            # try:
                # if play_path is None:
                    # play_path_pat = re.compile(r'ondemand\/(.*)\?')
                    # play_path_pat = re.compile(r'ondemand\/(.*)$')
                    # play_path = re.search(play_path_pat,game_url).groups()[0]
                    # print "play_path = " + repr(play_path)
                    # app_pat = re.compile(r'ondemand\/(.*)\?(.*)$')
                    # app = "ondemand?_fcs_vhost=cp65670.edgefcs.net&akmfv=1.6"
                    # app += re.search(app_pat,game_url).groups()[1]
            # except:
                # play_path = None
            # try:
                # if play_path is None:
                    # live_sub_pat = re.compile(r'live\/mlb_c(.*)\?')
                    # sub_path = re.search(live_sub_pat,game_url).groups()[0]
                    # sub_path = 'mlb_c' + sub_path
                    # live_play_pat = re.compile(r'live\/mlb_c(.*)$')
                    # play_path = re.search(live_play_pat,game_url).groups()[0]
                    # play_path = 'mlb_c' + play_path
                    # app = "live?_fcs_vhost=cp65670.live.edgefcs.net&akmfv=1.6"
                    # bSubscribe = True
                    
            # except:
                # pass

            # print "url = " + str(game_url)
            # print "play_path = " + str(play_path)
            
            
            if re.search('ondemand', game_url):
                play_path_pat = re.compile(r'ondemand\/(.*)$')
                play_path = re.search(play_path_pat,game_url).groups()[0]
                app = ' app=ondemand?_fcs_vhost=cp65670.edgefcs.net&akmfv=1.6'
                app += game_url.split('?')[1]
                swfurl = ' swfUrl="http://mlb.mlb.com/flash/mediaplayer/v4.2/R6/MediaPlayer4.swf?v=15'
                url = str(game_url)+swfurl+' playpath='+str(play_path)+app
                print '-----------ondemand-url = '+url
                item = xbmcgui.ListItem(path=url)
                xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
                
            elif re.search('live/',game_url):
                #live_play_pat = re.compile(r'live\/mlb_c(.*)$')
                #play_path = re.search(live_play_pat,game_url).groups()[0]
                rtmp = game_url.split('mlb_')[0]
                play_path = ' playpath=mlb_'+game_url.split('mlb_')[1]
                #app = ' app=live?_fcs_vhost=cp65670.live.edgefcs.net&akmfv=1.6'
                try:
                    sub_path = str(game_url).split('/')[4].split('?')[0]
                    subscribe = ' subscribe=' + str(sub_path) + ' live=1'
                except:
                    subscribe = ''
            
                pageurl = ' pageUrl="http://mlb.mlb.com/flash/mediaplayer/v4.2/R6/MP4.jsp?calendar_event_id='+soup.find('event-id').string+'&content_id=&media_id=&view_key=&media_type=video&source=MLB&sponsor=MLB&clickOrigin=&affiliateId=&team=mlb&"'
                swfurl = ' swfUrl="http://mlb.mlb.com/flash/mediaplayer/v4.2/R6/MediaPlayer4.swf?v=15'
                url = rtmp[:-1]+swfurl+pageurl+play_path+' live=1'
            print 'mlbGame URL----> '+url
            item = xbmcgui.ListItem(path=url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)


class dateStr:
        today = datetime.date.today()
        ty = 'year_'+str(today).split()[0].split('-')[0]
        tm = '/month_'+str(today).split()[0].split('-')[1]
        tday = '/day_'+str(today).split()[0].split('-')[2]
        t = ty+tm+tday

        one_day = datetime.timedelta(days=1)

        yesterday = today - one_day
        yy = 'year_'+str(yesterday).split()[0].split('-')[0]
        ym = '/month_'+str(yesterday).split()[0].split('-')[1]
        yday = '/day_'+str(yesterday).split()[0].split('-')[2]
        y = yy+ym+yday
        
        tomorrow = today + one_day
        toy = 'year_'+str(tomorrow).split()[0].split('-')[0]
        tom = '/month_'+str(tomorrow).split()[0].split('-')[1]
        tod = '/day_'+str(tomorrow).split()[0].split('-')[2]
        to = toy+tom+tod
        
        day = (t,y,to)

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

        
def coloring( text , color , colorword ):
        if color == "white":
            color="FFFFFFFF"
        if color == "blue":
            color="FF0000FF"
        if color == "cyan":
            color="FF00FFFF"
        if color == "violet":
            color="FFEE82EE"
        if color == "pink":
            color="FFFF1493"
        if color == "red":
            color="FFFF0000"
        if color == "green":
            color="FF00FF00"
        if color == "yellow":
            color="FFFFFF00"
        if color == "orange":
            color="FFFF4500"
        colored_text = text.replace( colorword , "[COLOR=%s]%s[/COLOR]" % ( color , colorword ) )
        return colored_text
        

def addLink(name,url,duration,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "duration": duration } )
        liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        

def addTeamLink(name,url,desc,duration,iconimage):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": desc, "Duration": duration } )
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
try:
        event=urllib.unquote_plus(params["event"])
except:
        pass
try:
        content=urllib.unquote_plus(params["content"])
except:
        pass
try:
        session=urllib.unquote_plus(params["session"])
except:
        pass
try:
        cookieIp=urllib.unquote_plus(params["cookieIp"])
except:
        pass
try:
        cookieFp=urllib.unquote_plus(params["cookieFp"])
except:
        pass

        

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None:
        print ""
        categories()
        
if mode==1:
        print""
        getVideos(url)

if mode==2:
        print""
        setVideoURL(url)
        
if mode==3:
        print""
        playLatest()
        
if mode==4:
        print""
        getTeams()

if mode==5:
        print""		
        getTeamVideo(url)

if mode==6:
        print""		
        getGames(url)

if mode==7:
        print""		
        mlbGame(event,content)
        
if mode==8:
        print""		
        getRealtimeVideo(url)
        
if mode==9:
        print""		
        getGameURL(name,event,content,session,cookieIp,cookieFp)
        
if mode==10:
        print""
        scrapeWebsite(url)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
