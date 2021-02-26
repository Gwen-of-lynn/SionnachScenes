from . import views
from django.urls import include

from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="storystarters"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='postdetail'),
    path("<slug:slug>/", views.postdetail, name="postdetail"),
    path('summernote/', include('django_summernote.urls')),
]
