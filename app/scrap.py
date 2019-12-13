import requests, re, json, urllib.request
from bs4 import BeautifulSoup
from re import match

def imagesearch(query):
    url = "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query
    mozhdr = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}    
    req = requests.get(url, headers = mozhdr)
    data = BeautifulSoup(req.content, "lxml")
    dataGoogle = []
    for listAllJsons in data.findAll("div",{"class":"rg_meta"}):
        getAllJson = json.loads(listAllJsons.text)
        dataGoogle.append({"title":getAllJson["pt"],"source":getAllJson["ru"],"image":getAllJson["ou"]})
    result = {
       "Status":"OK",
       "Creator":"Hayden",
       "Result":dataGoogle
       }
    return(result)
	
def instaprofile(user):
    profile = requests.get("https://www.instagram.com/" + user)
    soup = BeautifulSoup(profile.text, 'lxml')
    window=soup.findAll("script")[4].text.replace(";","").split("window._sharedData = ")[1]
    dw=json.loads(window)
    data=[]
    full_name="{}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["full_name"])
    username="\nUsername {}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["username"])
    followers="\nfollowers {}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_followed_by"]["count"])
    followed="\nfollowed {}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_follow"]["count"])
    post="\nPost {}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["count"])
    biography="\nBiography {}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["biography"])
    private="\nPrivate {}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["is_private"])
    image="\n{}".format(dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["profile_pic_url_hd"])
    data.append({"full_name":full_name,"username":username,"followers":followers,"followed":followed,"post":post,"biography":biography,"image":image})
    result = {
        "Status":"OK",
        "Creator":"Hayden",
        "Result":data
        }
    return(result)

def instapost(user):
    profile = requests.get("https://www.instagram.com/" + user)
    soup = BeautifulSoup(profile.text, 'lxml')
    window=soup.findAll("script")[4].text.replace(";","").split("window._sharedData = ")[1]
    dw=json.loads(window)
    linkpost=["https://www.instagram.com/p/"+c2["node"]["shortcode"] for c2 in dw["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]]
    hasildata=[]
    for isi in linkpost:
        req=requests.get(isi).text
        b=BeautifulSoup(req,"lxml")
        s=b.findAll("script")[3].text.replace(";","").split("window._sharedData = ")[1]
        data=json.loads(s)
        if "video_url" in data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]:
            hasil="{}".format(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["video_url"])
        else:   
            hasil="{}".format(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"])
        hasildata.append({"link":hasil})
    result={
        "Creator":"Hayden",
        "Status":"OK",
        "Result":hasildata
        }
    return(result)

def instastory(user):
    profile = requests.get("https://storiesig.com/stories/" + user)
    soup = BeautifulSoup(profile.text, "lxml")
    a = soup.findAll("a",{"target":"_blank"})
    story = []
    for hasil in a:
        if "https://instasave.io/" not in hasil.get("href"):
            if "https://twitter.com/jlobitu" not in hasil.get("href"):
                if "https://instagram.com/jlobitu" not in hasil.get("href"):
                    data=hasil.get("href")
                    story.append({"link":data})
    result = {
        "Creator":"Hayden",
        "Status":"OK",
        "Result":story
    }
    return(result)
def downloadsmule(cari):
    query=cari
    if "smule.com/c/" in query or "smule.com/p/" in query:
        data=[]
        url=query.split("/")[4]
        r = requests.get('https://www.smuledownloader.download/p/{}'.format(url))
        s = BeautifulSoup(r.text,'lxml')
        image = s.select('meta')[9].get('content')
        det = s.select('meta')[8].get('content')
        title=det.replace('Get Smule Performace : ','')
        if s.select('p.lead > a'):
              audio = s.select('p.lead > a')[1].get('href').replace('\n','')
        else:
              audio = s.select('p > a')[1].get('href').replace('\n','')
        data.append({"image":image,"title":title,"link":audio})
    else:
        data=[]
        lihat=urllib.request.urlopen(query)
        baca=lihat.read()
        b=BeautifulSoup(baca,"html.parser")
        c=b.findAll("script")[1].text.replace("\n","")
        d=json.loads(c)
        key=d["url"].split("/")[5]
        r = requests.get('https://www.smuledownloader.download/p/{}'.format(key))
        s = BeautifulSoup(r.text,'lxml')
        image = s.select('meta')[9].get('content')
        det = s.select('meta')[8].get('content')
        title = det.replace('Get Smule Performace : ','')
        if s.select('p.lead > a'):
              audio = s.select('p.lead > a')[1].get('href').replace('\n','')
        else:
              audio = s.select('p > a')[1].get('href').replace('\n','')
        data.append({"image":image,"title":title,"link":audio})
    result = {
        "Creato":"hayden",
        "Status":"OK",
        "Result":data
    }
    return(result)

def idsmule(query):
    ret=[]
    url = 'https://www.smule.com/'+query
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    r = soup.findAll('script')[0].text
    d = re.search(r'Profile:\s(.*?),\n',str(r)).group(1)
    data = json.loads(d)
    i = data['user']
    i1 = 'Idsmuel : '+str(i['handle'])
    i1 += '\nLinksmule : '+'https://www.smule.com'+str(i['url'])
    i1 += '\nPengikut : '+str(i['followers'])
    i1 += '\nMengikuti : '+str(i['followees'])
    i1 += '\nKanal : '+str(i['num_performances'])
    #i1 += '\nNama depan : '+str(i['first_name'])
    #i1 += '\nNama belakang : '+str(i['last_name'])
    i1 += '\nFavorit : '+str(i['sfam_count'])
    i1 += '\nId akun : '+str(i['account_id'])
    i1 += '\nVIP : '+str(i['is_vip'])
    i1 += '\nverifikasi : '+str(i['is_verified'])
    i1 += '\nTipe verifikasi : '+str(i['verified_type'])
    i1 += '\nPenyebutan : '+str(i['blurb'])
    hasil= str(i1)
    image = str(i['pic_url'])
    ret.append({"hasil":hasil,"image":image})
    result={
      "Status":"OK",
      "Creator":"Hayden",
      "Result":ret
    }
    return(result)

def performsmule(query):
    r = requests.get("https://www.smule.com/{}/performances/json".format(query))
    data = json.loads(r.text)
    ret=[]
    for li in data["list"]:
        c = " Judul Oc: "+str(li["title"])
        c += "\n Pembuat: "+str(li["owner"]["handle"])
        c += "\n Total like: "+str(li["stats"]["total_loves"])+" like"
        c += "\n Total comment: "+str(li["stats"]["total_comments"])+" comment"
        c += "\n Status VIP: "+str(li["owner"]["is_vip"])
        c += "\n Status Oc: "+str(li["message"])
        c += "\n Created Oc: {}".format(li["created_at"][:10])
        c += "\n Didengarkan: {}".format(li["stats"]["total_listens"])+" orang"
        hasil = str(c)
        image = str(li["cover_url"])
        id_record = str(li["key"])
        ret.append({"hasil":hasil,"id_record":id_record,"image":image})
    result={
      "Status":"OK",
      "Creator":"Hayden",
      "Result":ret
    }
    return(result)

def idrecordsmule(query):
    r = requests.get('https://www.smuledownloader.download/p/{}'.format(query))
    s = BeautifulSoup(r.text,'lxml')
    if s.select('p.lead > a'):
        x = s.select('p.lead > a')[1].get('href').replace('\n','')
    else:    
        x = s.select('p > a')[1].get('href').replace('\n','')
    result={
        "Status":"OK",
        "Creator":"Hayden",
        "Result":x
    }
    return(result)  

def songbooksmule(query):
    url="https://www.smule.com/{}/songs/json?offset=0&size=0&limit=24".format(query)
    r=requests.get(url).text
    data=json.loads(r)
    ret=[]
    for b in data["list"]:
        c = " Judul Songbook: "+str(b["title"])
        c += "\n Artis: "+str(b["artist"])
        c += "\n Pembuat: "+str(b["owner"]["handle"])
        c += "\n Sampul: "+str(b["owner"]["pic_url"])+" comment"
        c += "\n Id smule: https://www.smule.com"+str(b["owner"]["url"])
        c += "\n Sampul songbook: "+str(b["cover_url"])
        c += "\n Dibuat: {}".format(b["created_at"])
        c += "\n Songbook: https://www.smule.com{}".format(b["web_url"])
        hasil = str(c)
        image = str(b["cover_url"])
        ret.append({"hasil":hasil,"image":image})
    result={
      "Status":"OK",
      "Creator":"Hayden",
      "Result":ret
    }
    return(result)
