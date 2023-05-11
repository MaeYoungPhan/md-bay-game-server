"""baygame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from baygameapi.views import register_user, login_user, RiverAndStreamView, OccasionView, BayItemView, RecordOfTripView, BaySiteView, AvatarView, ReactionView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'riverandstreams', RiverAndStreamView, 'riverandstreams') #set up url, tell server which view to use when it sees that url, and assign a base name in case of error
router.register(r'occasions', OccasionView, 'occasions')
router.register(r'bayitems', BayItemView, 'bayitems')
router.register(r'recordoftrips', RecordOfTripView, 'recordoftrips')
router.register(r'baysites', BaySiteView, 'baysites')
router.register(r'avatars', AvatarView, 'avatars')
router.register(r'reactions', ReactionView, 'reactions')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
