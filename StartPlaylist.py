import urllib2
import yaml

host = "http://192.168.1.101:4040/rest/"
view = "getPlaylist.view"
logginParameters = "?u=USERNAME&t=MD5PASSWORD&s=SALT&v=1.15.0&c=iSub&f=json" #if the password is sesame and the random salt is c19b2d, then token = md5("sesamec19b2d") = 26719a1196d2a940705a59634eb18eab. 
playlistID = 39
actionParameters = "&id=" +  playlistID

webUrl = urllib2.urlopen(host + view + logginParameters + actionParameters)
if(webUrl.getcode() == 200):
	data = webUrl.read()
	#theJSON = json.loads(data)
	theJSON = yaml.load(data)
	length = len(theJSON["subsonic-response"]["playlist"]["entry"])
	songID = [0] * length
	for i in range(0, length):
		songID[i] = theJSON["subsonic-response"]["playlist"]["entry"][i]["id"]
view = "jukeboxControl.view"
actionParameters = "&action=set"
setUrl = host + view + logginParameters + actionParameters
for songs in songID:
	setUrl = setUrl + "&id=" + songs

urllib2.urlopen(setUrl)
actionParameters = "&action=shuffle"
urllib2.urlopen(host + view + logginParameters + actionParameters)
actionParameters = "&action=skip&index=0"
urllib2.urlopen(host + view + logginParameters + actionParameters)
