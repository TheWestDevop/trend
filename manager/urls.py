from django.urls import path
from manager.views import dashboard,login,auth,logout,startCrawler

urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('login/',login,name="login"),
    path('auth',auth,name="auth"),
    path('logout/',logout,name="logout"),
    path('crawler/',startCrawler,name="startCrawler"),
    path('endcrawler/',startCrawler,name="stopCrawler"),
]