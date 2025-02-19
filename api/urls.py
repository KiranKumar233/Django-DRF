from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter # It will take of default urls


router = DefaultRouter()
router.register('employees', views.EmployeeViewset,  basename='employee')



urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

  # path('employees/', views.Employees.as_view()), # When ever we use class based view as view we can use as_vies
  # path('employees/<int:pk>/', views.EmployeeDetails.as_view()),
  path('', include(router.urls)),

# These 2 statemts are the None Primary key based url Pattern
  path('blogs/', views.BlogsView.as_view()),
  path('comments/', views.CommentsView.as_view()),

  path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),

]