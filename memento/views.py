from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import requests
from bs4 import BeautifulSoup


from .models import MementoItem

# Create your views here.

def Hello(request):
    all_memento_items = MementoItem.objects.all()
    return render(request, 'home.html', {'all_items': all_memento_items})

def addMemento(request):
    #newtitle = request.POST['title']
    newnote = request.POST['note']
    newlink = request.POST['link']

    resultDict = scrapePage(newlink)
    print("hello...")
    print(resultDict)
    #resultDict['title']

    new_memento = MementoItem(title=resultDict['title'],blurb=resultDict['description'],note=newnote,link=newlink)
    new_memento.save()
    return HttpResponseRedirect('/home/')

def deleteMemento(request, memento_id):
    memento = MementoItem.objects.get(id=memento_id)
    memento.delete()
    return HttpResponseRedirect('/home/')


def scrapePage(link):
    page = requests.get(link)
    #print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    titleInfo = soup.find("meta", property="og:title")
    descInfo = soup.find("meta", property="og:description")

    resultDict = {"title": None, "description": None, "info1": None, "info2": None}

    if(titleInfo != None):
        title = titleInfo['content']
        resultDict['title'] = title
        print("title: " + title)
    else:
        print("No title meta data found")

    if(descInfo != None):
        desc = descInfo['content']
        resultDict['description'] = desc
        print("desc: " + desc)
    else:
        print("No description meta data found")

    if(titleInfo == None):
        spaninfo = soup.find_all('span',limit=10)
        parainfo = soup.find_all('p',limit=10)
        analyzeTags(spaninfo, parainfo)

    print(resultDict)
    return resultDict


def analyzeTags(spaninfo, parainfo):

    print("analyzetags")
    spans = [s.getText() for s in spaninfo]
    paras = [p.getText() for p in parainfo]
    print(spans)
    print(paras)
