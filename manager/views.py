# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models.models import Country,State,Town,Source,Profile,User,Articles
from website.forms import ArticleForm

# Create your views here.
#CRUD Country
def create_country(request):
    form = CountryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_countries')

    return render(request,'',{'forms': form})  


def list_countries(request):

    countries = Country.objects.all()

    return render(request,'',{'countries': countries}) 


def update_country(request,id):

    country  = Country.objectss.get(id=id)

    form = CompanyForm(request.POST or None, instance=country)

    if form.is_valid():

        form.save()

        return redirect('list_countries')


    return render(request,'',{'form': form , 'country':country})


def delete_country(request,id):
    
     country  = Country.objectss.get(id=id)
     
     if request.method == 'POST':
        country.delete()
        return redirect('list_countries')
      

     return render(request,'',{'country': country}) 



#CRUD State

def create_state(request):
    form = StateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_states')

    return render(request,'',{'forms': form})  


def list_states(request):

    states = State.objects.all()

    return render(request,'',{'states': states}) 


def update_state(request,id):

    state  = State.objectss.get(id=id)

    form = StateForm(request.POST or None, instance=state)

    if form.is_valid():

        form.save()

        return redirect('list_states')


    return render(request,'',{'form': form , 'state':state})


def delete_state(request,id):
    
     state  = State.objectss.get(id=id)
     
     if request.method == 'POST':
        state.delete()
        return redirect('list_states')
      

     return render(request,'',{'state': state}) 


#CRUD Town

def create_town(request):
    form = TownForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_towns')

    return render(request,'',{'forms': form})  


def list_towns(request):

    towns = Town.objects.all()

    return render(request,'',{'towns': towns}) 


def update_town(request,id):

    town  = Town.objectss.get(id=id)

    form = TownForm(request.POST or None, instance=town)

    if form.is_valid():

        form.save()

        return redirect('list_towns')


    return render(request,'',{'form': form , 'town':town})


def delete_town(request,id):
    
     town  = Town.objectss.get(id=id)
     
     if request.method == 'POST':
        town.delete()
        return redirect('list_towns')
      

     return render(request,'',{'town': town}) 



    
#CRUD Source


def create_source(request):
        form = SourceForm(request.POST or None)

        if form.is_valid():
           form.save()
        return redirect('list_sources')

        return render(request,'',{'forms': form})  


def list_sources(request):

    sources = Source.objects.all()

    return render(request,'',{'sources': sources}) 


def update_source(request,id):

    source  = Source.objectss.get(id=id)

    form = SourceForm(request.POST or None, instance=source)

    if form.is_valid():

        form.save()

        return redirect('list_sources')


    return render(request,'',{'form': form , 'source':source})


def delete_source(request,id):
    
     source  = Source.objectss.get(id=id)
     
     if request.method == 'POST':
        source.delete()
        return redirect('list_sources')
      

     return render(request,'',{'source': source}) 


#CRUD  Articles
def list_articles(request):
    template_name = 'index.html'
    article = Articles.objects.all()

    return render(request,template_name,{'articles': article}) 



def create_article(request):
      if request.method == 'POST':
            title = request.POST.get('title')
            summary = request.POST.get('summary')
            shortdesc = request.POST.get('shortdesc')
            content = request.POST.get('content')
            sid = request.POST.get('sid')
            author = request.POST.get('author')
            status = 1
            obj = Articles.objects.create(
               title = title,
               summary = summary,
               shortdesc = shortdesc,
               content = content,
               sid = sid,
               status = status,
               author = author,
            )
            return redirect('list_articles')
      else:
         return render(request,'forms/article.html')  



def update_article(request,id):

    article  = Articles.objects.get(id=id)
    form = ArticleForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('list_articles')
    return render(request,'forms/article_update.html',{'form':form,'article':article})


def delete_article(request,id):
    
     article  = Articles.objects.get(id=id)
     
     if request.method == 'POST':
        article.delete()
        return redirect('list_articles')
      

     return render(request,'delete.html',{'article': article}) 



#CRUD Profile

def create_profile(request):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
           form.save()
        return redirect('list_profiles')

        return render(request,'',{'forms': form})  


def list_profiles(request):

    profiles = Profile.objects.all()

    return render(request,'',{'profiles': profiles}) 


def update_profile(request,id):

    profile  = Profile.objectss.get(id=id)

    form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid():

        form.save()

        return redirect('list_profiles')


    return render(request,'',{'form': form , 'profile':profile})


def delete_profile(request,id):
    
     profile  = Profile.objectss.get(id=id)
     
     if request.method == 'POST':
        profile.delete()
        return redirect('list_profiles')
      

     return render(request,'',{'profile': profile}) 



#CRUD User

def create_user(request):
        form = UserForm(request.POST or None)

        if form.is_valid():
           form.save()
        return redirect('list_users')

        return render(request,'',{'forms': form})  


def list_users(request):

    users = User.objects.all()

    return render(request,'',{'users': users}) 


def update_user(request,id):

    user  = User.objectss.get(id=id)

    form = UserForm(request.POST or None, instance=profile)

    if form.is_valid():

        form.save()

        return redirect('list_users')


    return render(request,'',{'form': form , 'user':user})


def delete_user(request,id):
    
     user  = User.objectss.get(id=id)
     
     if request.method == 'POST':
        user.delete()
        return redirect('list_users')
      

     return render(request,'',{'user': user}) 
