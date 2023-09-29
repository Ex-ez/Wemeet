from django.urls import path
from rest_framework.routers import SimpleRouter,DefaultRouter
from . import views
#router = DefaultRouter()
# router.register(r'', views.PlanViewSet, basename='plan'),
#
# urlpatterns =[
#     *router.urls,
# ]

urlpatterns = [
  # path('<uuid:pk>/',views.PlanViewSet.as_view({'get':'retrieve'}), name='plan_detail'),
    path('', views.PlanList.as_view(), name='plan'),
    path('<uuid:pk>/', views.PlanDetail.as_view(), name='plan_detail'),
]