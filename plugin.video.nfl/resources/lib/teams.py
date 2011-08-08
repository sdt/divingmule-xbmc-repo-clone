
# Fanart images are from - Hawk Eyes' - http://www.flickr.com/photos/cpardue/sets/72157627232426473/  http://creativecommons.org/licenses/by-nc/2.0/deed.en
# Icon images are from AStahrr - http://findicons.com/pack/539/nfl For noncommercial use


import urllib,urllib2,re,os,sys
import xbmcplugin,xbmcgui,xbmcaddon


__settings__ = xbmcaddon.Addon(id='plugin.video.nfl')
home = __settings__.getAddonInfo('path')


def addDir(name,url,mode,iconimage,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty( "Fanart_Image", fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def bengals():
        fanart = 'http://farm7.static.flickr.com/6011/6009300352_69756abe8c_o.jpg'
        icon = 'http://farm7.static.flickr.com/6011/6009300352_4f1f19b3bc_m.jpg'
        urlA = 'http://www.bengals.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&sortField=DATE&contentType=AUDIO,VIDEO&showRelatedToContent=Yes&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showViewCount=Yes&showRSS=No&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'All%20Videos,Press%20Conference%20-%20Video,In%20the%20Locker%20Room%20-%20Video,Minicamp-OTAs%20-%20Video,Game%20Highlights%20-%20Video,Bengals%20Weekly%20Marvin%20Lewis%20-%20Video,NFL%20Network%20-%20Video,Game%20Previews%20-%20Video,Rookie%20Minicamp%20-%20Video,NFL%20Draft%20-%20Video,Training%20Camp%20-%20Video,NFL%20Scouting%20Combine%20-%20Video,Miscellaneous%20-%20Video'
        n = names.split(',')
        addDir('All Videos',urlA+n[0].replace('%20-%20Video','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Press Conference',urlA+n[1].replace('%20-%20Video','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('In the Locker Room',urlA+n[2].replace('%20-%20Video','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Minicamp-OTAs',urlA+n[3].replace('%20-%20Video','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[4].replace('%20-%20Video','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Bengals Weekly Marvin Lewis',urlA+n[5].replace('%20-%20Video','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[6].replace('%20-%20Video','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Game Previews',urlA+n[7].replace('%20-%20Video','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Rookie Minicamp',urlA+n[8].replace('%20-%20Video','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('NFL Draft',urlA+n[9].replace('%20-%20Video','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[10].replace('%20-%20Video','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('NFL Scouting Combine',urlA+n[11].replace('%20-%20Video','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('Miscellaneous',urlA+n[12].replace('%20-%20Video','')+urlB+n[12]+urlC,7,icon,fanart)


def browns():
        fanart = 'http://farm7.static.flickr.com/6127/6009299438_d11037aa26_o.jpg'
        icon = 'http://farm7.static.flickr.com/6127/6009299438_1f1dd2bec7_m.jpg'
        urlA = 'http://www.clevelandbrowns.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=CLE&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%20-%20Cleveland%20Browns%20Report,Video%20-%20Draft,Video%20-%20Features,Video%20-%20History,Video%20-%20Interviews,Video%20-%20Off%20the%20Field,Video%20-%20Press%20Conferences'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Cleveland Browns Report',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Draft',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Features',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('History',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Interviews',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Off the Field',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+'Game%20Highlights'+urlB+'Video%20-%20Game%20Highlights'+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+'NFL%20Network'+urlB+'Video%20-%20NFL%20Network'+urlC,7,icon,fanart)


def buccaneers():
        fanart = 'http://farm7.static.flickr.com/6130/6009473824_080faa749e_o.jpg'
        icon = 'http://farm7.static.flickr.com/6130/6009473824_9015669a7c_m.jpg'
        urlA = 'http://www.buccaneers.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=TB&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%3A%20Video%20Archive,Videos%3A%20Cheerleaders,Videos%3A%20Community'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Video Archive',urlA+n[0].replace('Videos%3A%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[1].replace('Videos%3A%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[2].replace('Videos%3A%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+'Training%20Camp'+urlB+'Videos%3A%20Training%20Camp'+urlC,7,icon,fanart)
        addDir('Events',urlA+'Events'+urlB+'Videos%3A%20Events'+urlC,7,icon,fanart)
        addDir('Draft',urlA+'Draft'+urlB+'Videos%3A%20Draft'+urlC,7,icon,fanart)
        addDir('Buccaneers Insider',urlA+'Buccaneers%20Insider'+urlB+'Videos%3A%20Buccaneers%20Insider'+urlC,7,icon,fanart)


def cardinals():
        fanart = 'http://farm7.static.flickr.com/6001/5984449229_3ef7ab5285_o.jpg'
        icon = 'http://farm7.static.flickr.com/6001/5984449229_fbed0e5147_m.jpg'
        urlA = 'http://www.azcardinals.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&sortField=DATE&contentType=VIDEO&relatedClubs=ARI&clubRelatedTerms='
        urlC = '&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%20-%20Press%20Conferences,Videos%20-%20AzCardinals.com%20TV,Videos%20-%20Highlights,Videos%20-%20Maximum%20Cardinals'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('AzCardinals.com TV',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Highlights',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Maximum Cardinals',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)


def chiefs():
        fanart = 'http://farm7.static.flickr.com/6135/5982773393_30dcbb76fe_o.jpg'
        icon = 'http://farm7.static.flickr.com/6135/5982773393_53a393e5e1_m.jpg'
        urlA = 'http://www.kcchiefs.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%20-%20Press%20Conferences,Video%20-%20Inside%20the%20Locker%20Room,Video%20-%20Game%20Highlights,Video%20-%20Cheerleaders,Video%20-%20Arrowhead%20Updates,Video%20-%20Community,Video%20-%20Training%20Camp,Video%20-%202%20Minutes%20with%20Mitch,Video%20-%20Turning%20Point,Video%20-%20Insider%20Game%20Reports,Video%20-%20NFL%20Network,Video%20-%20Chiefs%20Live,Video%20-%20History,Video%20-%20Fans'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Inside the Locker Room',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Arrowhead Updates',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('2 Minutes with Mitch',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Turning Point',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Insider Game Reports',urlA+n[9].replace('Videos%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[10].replace('Videos%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('Chiefs Live',urlA+n[11].replace('Videos%20-%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('History',urlA+n[12].replace('Videos%20-%20','')+urlB+n[12]+urlC,7,icon,fanart)
        addDir('Fans',urlA+n[13].replace('Videos%20-%20','')+urlB+n[13]+urlC,7,icon,fanart)


def chargers():
        fanart = 'http://farm7.static.flickr.com/6022/5983336472_278819939b_o.jpg'
        icon = 'http://farm7.static.flickr.com/6022/5983336472_98c373d130_m.jpg'
        urlA = 'http://www.chargers.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&sortField=DATE&contentType=VIDEO&relatedClubs=SD&clubRelatedTerms='
        urlC = '&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=No&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%3A%20Charger%20Girls,Video%3A%20Features,Video%3A%20Game%20Highlights,Video%3A%20Press%20Conference,Video%3A%20Sights%20and%20Sounds,Video%3A%20USA%20Football'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Charger Girls',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Features',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Press Conference',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Sights and Sounds',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('USA Football',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)


def eagles():
        fanart = 'http://farm7.static.flickr.com/6140/5995277769_52906f9e5d_o.jpg'
        'http://farm7.static.flickr.com/6140/5995277769_fd13323507_m.jpg'
        urlA = 'http://www.philadelphiaeagles.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=PHI&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%20-%20Cheerleaders,Video%20-%20Eaglemania,Video%20-%20Eagles%20Confidential,Video%20-%20Eagles%20TV,Video%20-%20Fandemonium,Video%20-%20Features,Video%20-%20Football%20News,Video%20-%20Gameday%20Coverage,Video%20-%20NFL%20Network,Video%20-%20Off%20The%20Field,Video%20-%20The%20Players%20Show,Video%20-%20Training%20Camp,Video%20-%20Webcast'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Eaglemania',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Eagles Confidential',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Eagles TV',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Fandemonium',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Features',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Football News',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Gameday Coverage',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Off The Field',urlA+n[9].replace('Videos%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('The Players Show',urlA+n[10].replace('Videos%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[11].replace('Videos%20-%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('Webcast',urlA+n[12].replace('Videos%20-%20','')+urlB+n[12]+urlC,7,icon,fanart)


def fortyniners():
        fanart = 'http://farm7.static.flickr.com/6140/5985014424_0df3c84417_o.jpg'
        icon = 'http://farm7.static.flickr.com/6140/5985014424_c9817f5c82_m.jpg'
        urlA = 'http://www.49ers.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&sortField=DATE&contentType=VIDEO&showRelatedToContent=No&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showViewCount=No&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=15&pageno=1'  #&page=1&_=1312500804172
        names = 'Video%20-%20TV49,Video%20-%20Up%20Close,Video%20-%20Spencer%20for%20Hire,Video%20-%20Know%20Your%20Teammates,Video%20-%20Gold%20Rush,Video%20-%20Game%20Highlights,Video%20-%20NFL%20Network,Video%20-%20Youth%20Football,Video%20-%20Fans,Video%20-%20Beat%20the%20Clock,Video%20-%20Super%20Bowl,Video%20-%20Pro%20Bowl,Video%20-%20Scouting%20Combine,Video%20-%2049ers%20%20Total%20Access,Video%20-%20Total%20Access%20for%20Kids,Video%20-%2049ers%20Press%20Pass,Video%20-%20The%20Joe%20Show,Video%20-%20Hall%20of%20Fame,Video%20-%20Community,Video%20-%20Training%20Camp,Video%20-%20Draft,Video%20-%20Senior%20Bowl,Video%20-%20Spikes%20TV'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('TV49',urlA+n[0].replace('Video%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Up Close',urlA+n[1].replace('Video%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Spencer for Hire',urlA+n[2].replace('Video%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Know Your Teammates',urlA+n[3].replace('Video%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Gold Rush',urlA+n[4].replace('Video%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[5].replace('Video%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[6].replace('Video%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Youth Football',urlA+n[7].replace('Video%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Fans',urlA+n[8].replace('Video%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Beat the Clock',urlA+n[9].replace('Video%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Super Bowl',urlA+n[10].replace('Video%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('Pro Bowl',urlA+n[11].replace('Video%20-%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('Scouting Combine',urlA+n[12].replace('Video%20-%20','')+urlB+n[12]+urlC,7,icon,fanart)
        addDir('49ers  Total Access',urlA+n[13].replace('Video%20-%20','')+urlB+n[13]+urlC,7,icon,fanart)
        addDir('Total Access for Kids',urlA+n[14].replace('Video%20-%20','')+urlB+n[14]+urlC,7,icon,fanart)
        addDir('49ers Press Pass',urlA+n[15].replace('Video%20-%20','')+urlB+n[15]+urlC,7,icon,fanart)
        addDir('The Joe Show',urlA+n[16].replace('Video%20-%20','')+urlB+n[16]+urlC,7,icon,fanart)
        addDir('Hall of Fame',urlA+n[17].replace('Video%20-%20','')+urlB+n[17]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[18].replace('Video%20-%20','')+urlB+n[18]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[19].replace('Video%20-%20','')+urlB+n[19]+urlC,7,icon,fanart)
        addDir('Draft',urlA+n[20].replace('Video%20-%20','')+urlB+n[20]+urlC,7,icon,fanart)
        addDir('Senior Bowl',urlA+n[21].replace('Video%20-%20','')+urlB+n[21]+urlC,7,icon,fanart)
        addDir('Spikes TV',urlA+n[22].replace('Video%20-%20','')+urlB+n[22]+urlC,7,icon,fanart)


def giants():
        fanart = 'http://farm7.static.flickr.com/6123/5995276331_2629b77f95_o.jpg'
        icon = 'http://farm7.static.flickr.com/6123/5995276331_5b335c77de_m.jpg'
        urlA = 'http://www.giants.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=NYG&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%20-%20Locker%20Room,Videos%20-%20Game%20Highlights,Videos%20-%20Press%20Conferences,Videos%20-%20Giants%20Rewind,Videos%20-%20Giants%20Insider,Videos%20-%20TV%20Shows,Videos%20-%20History,Videos%20-%20Features,Videos%20-%20Draft'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+urlC,7,icon,fanart)
        addDir('Locker Room',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Giants Rewind',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Giants Insider',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('TV Shows',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('History',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Features',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Draft',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)


def jets():
        fanart = 'http://farm7.static.flickr.com/6127/5999958596_71a39b8f14_o.jpg'
        icon = 'http://farm7.static.flickr.com/6127/5999958596_84ff270f61_m.jpg'
        urlA = 'http://www.newyorkjets.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=NYJ&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'  #&page=1&_=1312466526529'
        names = 'Video%20-%20Features%2FInterviews,Video%20-%20Press%20Conferences,Video%20-%20Gameday%20Highlights,Video%20-%20Historical,Video%20-%20Flight%20Crew,Video%20-%20In%20the%20Community,Video%20-%20New%20Stadium,Video%20-%20Generation%20Jets,Video%20-%20Four%20Quarters,Video%20-%20Draft%2FCombine'
        n = names.split(',')
        addDir('All Videos',urlA+'Most%20Recent%20(All)'+urlB+names+urlC,7,icon,fanart)
        addDir('Features/Interviews',urlA+n[0].replace('Video%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[1].replace('Video%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Gameday Highlights',urlA+n[2].replace('Video%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Historical',urlA+n[3].replace('Video%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Flight Crew',urlA+n[4].replace('Video%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('In the Community',urlA+n[5].replace('Video%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('New Stadium',urlA+n[6].replace('Video%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Generation Jets',urlA+n[7].replace('Video%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Four Quarters',urlA+n[8].replace('Video%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Draft/Combine',urlA+n[9].replace('Video%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)


def lions():
        fanart = 'http://farm7.static.flickr.com/6008/5988506040_18157f0799_o.jpg'
        icon = 'http://farm7.static.flickr.com/6008/5988506040_a546c4983b_m.jpg'
        urlA = 'http://www.detroitlions.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&sortField=DATE&contentType=VIDEO&relatedClubs=DET&clubRelatedTerms='
        urlC = '&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=Yes&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%20-%20Ford%20Lions%20Report,Video%20-%20Game%20Highlights,Video%20-%20Locker%20Room,Video%20-%20Media%20Session,Video%20-%20Postgame,Video%20-%20Press%20Conferences,Video%20-%20Schwartz,Video%20-%20Season%20Review,Video%20-%20Training%20Camp,Video%20-%202011%20Combine,Video%20-%20Video%20Clips'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Ford Lions Report',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Locker Room',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Media Session',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Postgame',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Schwartz',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Season Review',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('2011 Combine',urlA+n[9].replace('Videos%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Video Clips',urlA+n[10].replace('Videos%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)


def packers():
        fanart = 'http://farm7.static.flickr.com/6125/5987940779_13a3491bdc_o.jpg'
        icon = 'http://farm7.static.flickr.com/6125/5987940779_50243f0567_m.jpg'
        urlA = 'http://prod.www.packers.clubs.nfl.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&sortField=DATE&contentType=VIDEO&showRelatedToContent=Yes&relatedClubs=GB&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showViewCount=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%3A%20Ask%20Vic,Videos%3A%20Community,Videos%3A%20Draft,Videos%3A%20Exclusives,Videos%3A%20Fit%20Kids,Videos%3A%20Game%20Highlights,Videos%3A%20Hall%20of%20Fame,Videos%3A%20Inside%20Lambeau,Videos%3A%20Larry%20McCarren%27s%20Locker%20Room,Videos%3A%20Locker%20Room%20Interviews,Videos%3A%20Mike%20McCarthy%20Show,Videos%3A%20NFL%20Network,Videos%3A%20OTAs,Videos%3A%20Press%20Conference,Videos%3A%20Super%20Bowl%20XLV,Videos%3A%20Training%20Camp'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Ask Vic',urlA+n[0].replace('Videos%3A%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[1].replace('Videos%3A%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Draft',urlA+n[2].replace('Videos%3A%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Exclusives',urlA+n[3].replace('Videos%3A%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Fit Kids',urlA+n[4].replace('Videos%3A%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[5].replace('Videos%3A%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Hall of Fame',urlA+n[6].replace('Videos%3A%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Inside Lambeau',urlA+n[7].replace('Videos%3A%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir("Larry McCarren's Locker Room",urlA+n[8].replace('Videos%3A%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Locker Room Interviews',urlA+n[9].replace('Videos%3A%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Mike McCarthy Show',urlA+n[10].replace('Videos%3A%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[10].replace('Videos%3A%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('OTAs',urlA+n[11].replace('Videos%3A%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('Press Conference',urlA+n[12].replace('Videos%3A%20','')+urlB+n[12]+urlC,7,icon,fanart)
        addDir('Super Bowl XLV',urlA+n[12].replace('Videos%3A%20','')+urlB+n[12]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[12].replace('Videos%3A%20','')+urlB+n[12]+urlC,7,icon,fanart)


def panthers():
        fanart = 'http://farm7.static.flickr.com/6012/6009472252_5f4d8509df_o.jpg'
        icon = 'http://farm7.static.flickr.com/6012/6009472252_8492f9d7b2_m.jpg'
        urlA = 'http://www.panthers.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&sortField=DATE&contentType=VIDEO&relatedClubs=CAR&clubRelatedTerms='
        urlC = '&showImage=Yes&showDescription=No&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%20-%20Panthers.com%20TV,Videos%20-%20Panthers%20Gameday,Videos%20-%20Panthers%20Huddle,Videos%20-%20TopCats,Videos%20-%20Sir%20Purr,Videos%20-%20Community,Videos%20-%20NFL%20Network,Videos%20-%20Motorola'
        n = names.split(',')
        addDir('All Videos',urlA+'ALL%20VIDEOS'+urlB+names+urlC,7,icon,fanart)
        addDir('Panthers.com TV',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Panthers Gameday',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Panthers Huddle',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('TopCats',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Sir Purr',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Motorola',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)


def patriots():
        fanart = 'http://farm7.static.flickr.com/6133/5999408997_5dab8ac31f_o.jpg'
        icon = 'http://farm7.static.flickr.com/6133/5999408997_9dd8533670_m.jpg'
        urlA = 'http://www.patriots.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=NE&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=Yes&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=15&pageno=1'    #&page=1&_=1312484799972
        names = 'Video%20-%20General,Video%20-%20All%20Access,Video%20-%20Belichick%20Breakdowns,Video%20-%20Interviews,Video%20-%20From%20the%20NFL,Video%20-%20Patriots%20Today,Video%20-%20Locker%20Room%20Uncut,Video%20-%20PFW%20TV,Video%20-%20Press%20Conference,Video%20-%20Cheerleaders,Video%20-%20Super%20Bowl,Video%20-%20NFL,Video%20-%20Patriots%20Today%3A%20Locker%20Room%20Uncut'
        n = names.split(',')
        addDir('Latest Viedos',urlA+'Latest%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('General',urlA+n[0].replace('Video%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('All Access',urlA+n[1].replace('Video%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Belichick Breakdowns',urlA+n[2].replace('Video%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Interviews',urlA+n[3].replace('Video%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('From the NFL',urlA+n[4].replace('Video%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Patriots Today',urlA+n[5].replace('Video%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Locker Room Uncut',urlA+n[6].replace('Video%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('PFW TV',urlA+n[7].replace('Video%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Press Conference',urlA+n[8].replace('Video%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[9].replace('Video%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Super Bowl',urlA+n[10].replace('Video%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('NFL',urlA+n[11].replace('Video%20-%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('Patriots Today: Locker Room Uncut',urlA+n[12].replace('Video%20-%20','')+urlB+n[12]+urlC,7,icon,fanart)


def raiders():
        fanart = 'http://farm7.static.flickr.com/6145/5982772583_63b5dc49b8_o.jpg'
        icon = 'http://farm7.static.flickr.com/6145/5982772583_6131581422_m.jpg'
        urlA = 'http://www.raiders.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=No&relatedClubs=OAK&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%20-%20Press%20Conferences,Videos%20-%20Behind%20the%20Shield,Videos%20-%20Historical%20Highlights,Videos%20-%20Game%20Highlights,Videos%20-%20NFL%20Network,Videos%20-%20Raiderettes,Videos%20-%20Raiders%20Report,Videos%20-%20Silver%20and%20Black,Videos%20-%20Draft'
        n = names.split(',')
        addDir('All Videos',urlA+'ALL%20VIDEOS'+urlB+names+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Behind the Shield',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Historical Highlights',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Raiderettes',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Raiders Report',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Silver and Black',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Draft',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)


def redskins():
        fanart = 'http://farm7.static.flickr.com/6148/5995833826_79a785014e_o.jpg'
        url = 'http://www.redskins.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&=undefined&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=WAS&clubRelatedTerms=Video%20-%20Comcast%20SportsNet,Video%20-%20Press%20Conferences,Video%20-%20Cheerleaders,Video%20-%20Health%20and%20Wellness,Video%20-%20News%20and%20Highlights,Video%20-%20NFL%20Films,Video%20-%20Player%20and%20Coach%20Profiles,Video%20-%20Post%20Game,Video%20-%20Redskins%20Park%20Action,Video%20-%20Redskins%20Rule,Video%20-%20En%20Espanol&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=No&showPagination=Yes&showPagerStatus=Yes&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        icon = 'http://farm7.static.flickr.com/6148/5995833826_2bb2981de1_m.jpg'
        addDir('All Videos',url,7,icon,fanart)


def rams():
        fanart = 'http://farm7.static.flickr.com/6012/5985015330_83f21bc9e4_o.jpg'
        icon = 'http://farm7.static.flickr.com/6012/5985015330_814587c665_m.jpg'
        urlA = 'http://www.stlouisrams.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=No&relatedClubs=STL&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%20-%20Press%20Conferences,Video%20-%20Interviews,Video%20-%20Highlights,Video%20-%20Community,Video%20-%20Cheerleaders,Video%20-%20NFL%20Networks,Video%20-%20Shows,Video%20-%20NFL%20Draft,Video%20-%20Kids,Video%20-%20Schnucks,Video%20-%20My%20Ride,Video%20-%20Thats%20My%20Dog,Video%20-%20Inside%20Look,Video%20-%20The%20Sports%20Nook,Video%20-%20Wired,Video%20-%20Features,Video%20-%20History,Video%20-%20Live%20Video,Video%20-%20Inside%20the%20Game'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Interviews',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Highlights',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('NFL Networks',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Shows',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('NFL Draft',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Kids',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Schnucks',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('My Ride',urlA+n[9].replace('Videos%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Thats My Dog',urlA+n[10].replace('Videos%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('Inside Look',urlA+n[11].replace('Videos%20-%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('The Sports Nook',urlA+n[12].replace('Videos%20-%20','')+urlB+n[12]+urlC,7,icon,fanart)
        addDir('Wired',urlA+n[13].replace('Videos%20-%20','')+urlB+n[13]+urlC,7,icon,fanart)
        addDir('Features',urlA+n[14].replace('Videos%20-%20','')+urlB+n[14]+urlC,7,icon,fanart)
        addDir('History',urlA+n[15].replace('Videos%20-%20','')+urlB+n[15]+urlC,7,icon,fanart)
        addDir('Live Video',urlA+n[16].replace('Videos%20-%20','')+urlB+n[16]+urlC,7,icon,fanart)
        addDir('Inside the Game',urlA+n[17].replace('Videos%20-%20','')+urlB+n[17]+urlC,7,icon,fanart)


def seahawks():
        fanart = 'http://farm7.static.flickr.com/6002/5984451637_a87e8a2549_o.jpg'
        icon = 'http://farm7.static.flickr.com/6002/5984451637_4f7bb3b46f_m.jpg'
        url = 'http://www.seahawks.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName=All%20Videos%20Archive&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=No&relatedClubs=SEA&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=No&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=Yes&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=7&pageno=1'
        addDir('All Videos',url,7,icon,fanart)


def saints():
        fanart ='http://farm7.static.flickr.com/6125/6008924973_5ecac036b3_o.jpg'
        icon = 'http://farm7.static.flickr.com/6125/6008924973_75bf096d30_m.jpg'
        urlA = 'http://www.neworleanssaints.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=Yes&relatedClubs=NO&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=month&showPagination=Yes&showPagerStatus=Yes&showCount=Yes&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Video%20-%20Gameday,Video%20-%20Draft,Video%20-%20Community,Video%20-%20NFL%20Network,Video%20-%20Path%20to%20the%20Draft,Video%20-%20Youth%20Programs,Video%20-%20Training%20Camp'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Gameday',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Draft',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Path to the Draft',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Youth Programs',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)


def texans():
        fanart = 'http://farm7.static.flickr.com/6010/5994131823_3a1932675c_o.jpg'
        icon = 'http://farm7.static.flickr.com/6010/5994131823_c86dca0c96_m.jpg'
        urlA = 'http://www.houstontexans.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&contentListType=internal&contentType=VIDEO&sortField=DATE&showRelatedToContent=No&relatedClubs=HOU&clubRelatedTerms='
        urlC = '&relatedToId=&showImage=Yes&showDescription=Yes&showByline=Yes&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=15&pageno=1'
        names = 'Videos%20-%20Football,Videos%20-%20Special%20Segments,Videos%20-%20Press%20Conferences,Videos%20-%20Community,Videos%20-%20Gameday,Videos%20-%20Cheerleaders,Videos%20-%20Season%20Highlights,Videos%20-%20Texans%20Huddle,Videos%20-%20Inside%20the%20Locker,Videos%20-%20Teammate%20Trivia,Videos%20-%20NFL%20Films%20Highlights'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Football',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Special Segments',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Gameday',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Season Highlights',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Texans Huddle',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Inside the Locker',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Teammate Trivia',urlA+n[9].replace('Videos%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('NFL Films Highlights',urlA+n[10].replace('Videos%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)


def titans():
        fanart = 'http://farm7.static.flickr.com/6014/5994130863_68a8d53ec4_o.jpg'
        icon = 'http://farm7.static.flickr.com/6014/5994130863_839e1e630b_m.jpg'
        urlA='http://www.titansonline.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB='&sortField=DATE&contentType=VIDEO&relatedClubs=TEN&clubRelatedTerms='
        urlC='&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=No&showFilterType=month&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = '2010%20NFL%20Draft,Videos%3A%20Cheerleader,Videos%3A%20Community,Videos%3A%20Game%20Highlights,Videos%3A%20NFL%20Network%20Features,Videos%3A%20Player%20Interviews,Videos%3A%20Press%20Conference,Videos%3A%20Titans%20All%20Access,Videos%3A%20T-RAC'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('2010 NFL Draft',urlA+n[0].replace('Videos%3A%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('Cheerleader',urlA+n[1].replace('Videos%3A%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('Community',urlA+n[2].replace('Videos%3A%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Game Highlights',urlA+n[3].replace('Videos%3A%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('NFL Network Features',urlA+n[4].replace('Videos%3A%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Player Interviews',urlA+n[5].replace('Videos%3A%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Press Conference',urlA+n[6].replace('Videos%3A%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Titans All Access',urlA+n[7].replace('Videos%3A%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('T-RAC',urlA+n[8].replace('Videos%3A%20','')+urlB+n[8]+urlC,7,icon,fanart)


def vikings():
        fanart = 'http://farm7.static.flickr.com/6016/5988505154_3e5e923ecb_o.jpg'
        icon = 'http://farm7.static.flickr.com/6016/5988505154_0749939588_m.jpg'
        urlA = 'http://www.vikings.com/cda-web/content-list-dynamic-module-paginated.htm?previewMode=false&displayName='
        urlB = '&numberOfResults=100&sortField=DATE&contentType=VIDEO&relatedClubs=MIN&clubRelatedTerms='
        urlC = '&showImage=Yes&showDescription=Yes&showByline=No&showPublicationDate=Yes&showRSS=Yes&showContentType=Yes&showFilterType=No&showPagination=Yes&showPagerStatus=No&showCount=No&showTitleStyle=Yes&view=content-list-variation-2&month=&year=&numberPerPage=10&pageno=1'
        names = 'Videos%20-%20Press%20Conferences,Videos%20-%20NFL%20Network,Videos%20-%20VEN,Videos%20-%20Stadium,Videos%20-%20Vikings%20Weekly,Videos%20-%20Game%20Day,Videos%20-%20Cheerleaders,Videos%20-%20Jared%20Allen%20Street%20Meet,Videos%20-%20Outreach,Videos%20-%20Vikings%20Wired,Videos%20-%20Viktor%20the%20Viking,Videos%20-%20Vikings%20GamePlan,Videos%20-%20Training%20Camp'
        n = names.split(',')
        addDir('All Videos',urlA+'All%20Videos'+urlB+names+urlC,7,icon,fanart)
        addDir('Press Conferences',urlA+n[0].replace('Videos%20-%20','')+urlB+n[0]+urlC,7,icon,fanart)
        addDir('NFL Network',urlA+n[1].replace('Videos%20-%20','')+urlB+n[1]+urlC,7,icon,fanart)
        addDir('VEN',urlA+n[2].replace('Videos%20-%20','')+urlB+n[2]+urlC,7,icon,fanart)
        addDir('Stadium',urlA+n[3].replace('Videos%20-%20','')+urlB+n[3]+urlC,7,icon,fanart)
        addDir('Vikings Weekly',urlA+n[4].replace('Videos%20-%20','')+urlB+n[4]+urlC,7,icon,fanart)
        addDir('Game Day',urlA+n[5].replace('Videos%20-%20','')+urlB+n[5]+urlC,7,icon,fanart)
        addDir('Cheerleaders',urlA+n[6].replace('Videos%20-%20','')+urlB+n[6]+urlC,7,icon,fanart)
        addDir('Jared Allen Street Meet',urlA+n[7].replace('Videos%20-%20','')+urlB+n[7]+urlC,7,icon,fanart)
        addDir('Outreach',urlA+n[8].replace('Videos%20-%20','')+urlB+n[8]+urlC,7,icon,fanart)
        addDir('Vikings Wired',urlA+n[9].replace('Videos%20-%20','')+urlB+n[9]+urlC,7,icon,fanart)
        addDir('Viktor the Viking',urlA+n[10].replace('Videos%20-%20','')+urlB+n[10]+urlC,7,icon,fanart)
        addDir('Vikings GamePlan',urlA+n[11].replace('Videos%20-%20','')+urlB+n[11]+urlC,7,icon,fanart)
        addDir('Training Camp',urlA+n[12].replace('Videos%20-%20','')+urlB+n[12]+urlC,7,icon,fanart)