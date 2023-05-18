from django.urls import path
from .views import *
from properties.views import *

urlpatterns = [
    path('home', homepageView, name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('scope', ScopeView.as_view(), name='scope'),
    path('hiw', HowItWorks.as_view(), name='hiw'),
    path('residentialMenu', residentialMenuView, name = 'residentialMenu'),
    path('commercialMenu', commercialMenuView, name = 'commercialMenu'),
    path('ongoingMenu', onGoingMenuView, name = 'ongoingMenu'),
    path('property/<int:id>',detailView,name = 'property'),
]



