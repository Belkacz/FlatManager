"""FaltManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from flat_manager import views
from accounts import views as accounts_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.IndexView.as_view(), name='index'),
    path('home/search', views.SearchView.as_view(), name='search'),

    path('home/leaseagreement-list', views.LeaseAgreementList.as_view(), name='lease_agreement_list'),
    path('home/leaseagreement-create', views.LeaseAgreementCreate.as_view(), name='lease_agreement_create'),
    path('home/leaseagreement-delete/<int:pk>', views.LeaseAgreementDelete.as_view(), name='lease_agreement_delete'),
    path('home/leaseagreement-update/<int:pk>', views.LeaseAgreementUpdate.as_view(), name='lease_agreement_update'),
    path('home/leaseagreement-details/<int:pk>', views.LeaseAgreementDetails.as_view(), name='lease_agreement_details'),

    path('home/flat-list', views.FlatList.as_view(), name='flat_list'),
    path('home/flat-create', views.FlatCreate.as_view(), name='flat_create'),
    path('home/flat-delete/<int:pk>', views.FlatDelete.as_view(), name='flat_delete'),
    path('home/flat-update/<int:pk>', views.FlatUpdate.as_view(), name='flat_update'),

    # path('home/flat-list', views.FlatList.as_view(), name='flat_list'),
    path('home/room-create', views.RoomCreate.as_view(), name='room_create'),
    # path('home/flat-delete/<int:pk>', views.FlatDelete.as_view(), name='flat_delete'),
    # path('home/flat-update/<int:pk>', views.FlatUpdate.as_view(), name='flat_update'),

    path('home/rentier-list', views.RentierList.as_view(), name='rentier_list'),
    path('home/rentier-create', views.RentierCreate.as_view(), name='rentier_create'),
    path('home/rentier-delete/<int:pk>', views.RentierDelete.as_view(), name='rentier_delete'),
    path('home/rentier-update/<int:pk>', views.RentierUpdate.as_view(), name='rentier_update'),

    path('home/owner-list', views.OwnerList.as_view(), name='owner_list'),
    path('home/owner-create', views.OwnerCreate.as_view(), name='owner_create'),
    path('home/owner-delete/<int:pk>', views.OwnerDelete.as_view(), name='owner_delete'),
    path('home/owner-update/<int:pk>', views.OwnerUpdate.as_view(), name='owner_update'),

    path('home/agent-list', views.AgnetList.as_view(), name='agent_list'),
    path('home/agent-create', views.AgnetCreate.as_view(), name='agent_create'),
    path('home/agent-delete/<int:pk>', views.AgentDelete.as_view(), name='agent_delete'),
    path('home/agent-update/<int:pk>', views.AgentUpdate.as_view(), name='agent_update'),

    ###############
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("register/", accounts_view.RegisterUser.as_view(), name='register'),
]
