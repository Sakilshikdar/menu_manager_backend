from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('menus', views.MenuListandViewSet)
router.register('rating', views.MenuReviewListandViewSet)

urlpatterns = [
    path('all_menu/', views.MenuViewSet.as_view(), name='menu_list'),    
    path('admincustomer_menu/<int:pk>', views.MenuListViewSet.as_view(), name='menu_list_view'),    
    path('menu-detail/<int:pk>/', views.MenuDetailsViewSet.as_view(), name='bbok_details'),    
    path('menu-reviews/', views.ReviewViewSet.as_view(), name='review_list'),
    path('review_detail/<int:pk>/', views.ReviewDetailsViewSet.as_view(), name='review_list'),
    path('review_menu/<int:pk>/', views.ReviewDetailViewSet.as_view(), name='review_details'),
    path('admincustomer_login/', views.admincustomer_login, name='login'),
    path('admincustomer_register/', views.admincustomer_register, name='register'),
    path('admincustomer/<int:pk>/', views.AdminCustomerDetail.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('admincustomer-change-password/<int:pk>/', views.AdminCustomerChangePassword),
    
]

urlpatterns += router.urls
