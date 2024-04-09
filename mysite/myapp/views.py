from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Link is the model name, because we have defined a class named Link
from .models import Link
from django.http import HttpResponseRedirect


# Create your views here.

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        page = requests.get(site)
        # using page.text instead of page.content for extracting the tags...
        # otherwise, page.content is encoded, if you want to download it, then use page.content
        soup = BeautifulSoup(page.text, "html.parser")

        # link_address = []

        for link in soup.find_all("a"):
            # link_address.append(link.get("href"))
            # now we are going to save the link and name to our model
            # we need import our model first
            link_address = link.get("href")
            # link.string 是 BeautifulSoup 中用于获取 HTML 标签内的文本内容的属性。
            link_text = link.string
            # Pass the above data as parameters to create an object of Link
            # it will get saved in the database
            Link.objects.create(name=link_text, address=link_address)

        return HttpResponseRedirect('/')

    # Just a normal GET request from user
    else:
        # return render(request, "myapp/result.html", {"link_address": link_address})
        # Get all the objects from Link table
        data = Link.objects.all()

        # Then pass the data to front end
        return render(request, "myapp/result.html", {"data": data})



# write a view for delete method
def clear(request):
    Link.objects.all().delete()
    return render(request, "myapp/result.html")