from django.urls import path
from .views import (
    HomeView,
    AboutView,
    ContactView,
    CourseListView,
    CourseDetailView,
    SubjectListView,
    SubjectDetailView,
    TeacherListView,
    TeacherDetailView,
    ModuleDetailView,
    ContentDetailView,
    FeatureView,
    TeamView,
    TestimonialView,
)

app_name = 'app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    path('courses/', CourseListView.as_view(), name='courses'),
    path('courses/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),

    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/<slug:slug>/', SubjectDetailView.as_view(), name='subject_detail'),

    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    path('module/<int:module_id>/', ModuleDetailView.as_view(), name='module_detail'),
    path('content/<int:content_id>/', ContentDetailView.as_view(), name='content_detail'),

    path('feature/', FeatureView.as_view(), name='feature'),
    path('team/', TeamView.as_view(), name='team'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
]

