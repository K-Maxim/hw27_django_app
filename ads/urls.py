from django.urls import path
from ads import views

urlpatterns = [
    path('cat/', views.CatView.as_view()),
    path('cat/<int:pk>', views.CatDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CarDeleteView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdUploadImageView.as_view()),
    ]