

from django.contrib import admin
from django.urls import path,include
from Blog import views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings
import core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list, name="post_list"),
    path('signup/', core.views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/(?P<id>\d+)/(?P<slug>[\w-]+)/',views.post_detail,name="post_detail"),
    path('blog/post_create/',views.post_create,name="post_create"),
    path('blog/(?P<id>\d+)/post_edit/', views.post_edit, name="post_edit"),
    path('blog/(?P<id>\d+)/post_delete/', views.post_delete, name="post_delete"),
    path('ckeditor/',include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
