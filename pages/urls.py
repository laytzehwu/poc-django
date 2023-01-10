from django.urls import path, re_path, include
from .views import homePageView, abcPageView, abcPageWithInputView, userDetectorView

urlpatterns = [
    path("", homePageView, name = "home"),
    path("abc", abcPageView, name = "abc"),
    path("abc/<int:intInput>", abcPageWithInputView, name = "abc-int"),
    path("abc/<slug:title>", abcPageWithInputView, name = "abc-title"),
    path("abc/<int:intInput>/<slug:title>", abcPageWithInputView, name = "abc-int-title"),
    re_path(r'^bio/P(?P<username>\w+)/$', userDetectorView, name = "user-detector"), # (?P<username>\w+), prefix 'P' is required to identify parameter
    re_path(r'^api/', include('pages.api.urls')),
]