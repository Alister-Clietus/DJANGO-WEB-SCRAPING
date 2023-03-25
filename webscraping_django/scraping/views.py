from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
from scraping.models import links,linkk
from scraping.models import heading

# Create your views here.
def home(request):
    if request.method=='POST':
      websitename=request.POST.get('website',None)
      websitelink=request.POST.get('link',None)
      webscraping(websitelink)
      headingg(websitelink)
      temp=links.objects.create(Website_Name=websitename,Website_Link=websitelink)
      temp.save()
      return render(request,'t.html') 
    else:
      return render(request,'first.html') 


def trial(request):
    return render(request,'t.html') 


def webscraping(name):
   url=name
   response=requests.get(url)
   soup = BeautifulSoup(response.content, 'html.parser')
   for anchor in soup.find_all('a'):
        href = anchor.get('href')
        if href:
            text = anchor.string.strip() if anchor.string else href
            linkk.objects.create(url=href, text=text)


def headingg(name):
   url=name
   response=requests.get(url)
   soup = BeautifulSoup(response.content, 'html.parser')
   headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
   for headingss in headings:
        tag = headingss.name
        text = headingss.get_text().strip()
        heading.objects.create(TAG=tag, TEXT=text)
        print(tag)
        print(headings)
