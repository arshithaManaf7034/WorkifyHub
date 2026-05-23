from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # HOME
    path('', views.home),

    # ADMIN
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', views.login_view),
    path('register/', views.register_view),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # DASHBOARD
    path('dashboard/', views.dashboard),

    # WORKERS
    path('workers/', views.workers),

    # DYNAMIC WORKER PROFILE
    path(
        'worker/<int:worker_id>/',
        views.worker_profile
    ),

    # JOBS
    path(
        'post-job/', views.post_job),

    # RATINGS
    path(
        'rate/<int:worker_id>/',
        views.rate_worker
    ),
    path('book/<int:worker_id>/',
        views.book_appointment
    
    ),
    path('seller-appointments/',
        views.seller_appointments
    ),
    path('admin-dashboard/',
        views.admin_dashboard
    ),
    path('edit-profile/',
        views.edit_profile
    ),
    path(
    'chat/<int:user_id>/',
    views.chat_view,
    name='chat'
    
    ),
    path(
    'accept-appointment/<int:appointment_id>/',
    views.accept_appointment
    ),

    path(
    'reject-appointment/<int:appointment_id>/',
    views.reject_appointment
    ),
    path(
    'buyer-appointments/',
    views.buyer_appointments
    ),
    path(
    'buyer-appointments/',
    views.buyer_appointments
    ),

    path(
    'check-notifications/',
    views.check_notifications
),
]


# MEDIA FILES
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

