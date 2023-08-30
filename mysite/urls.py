from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from articles import views as articles_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("articles/", include("articles.urls")),
    path("about/", views.about, name="about"),
    path("", articles_views.article_list, name="home"),
    path("docs/", include_docs_urls(title='MySite API')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
