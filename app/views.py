from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Subject, Course, Teacher, Module, Content

# Home & Static pages
class HomeView(ListView):
    model = Course
    template_name = 'home/index.html'
    context_object_name = 'courses'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactView(TemplateView):
    template_name = 'home/contact.html'


class FeatureView(TemplateView):
    template_name = 'home/feature.html'


class TeamView(TemplateView):
    template_name = 'home/team.html'


class TestimonialView(TemplateView):
    template_name = 'home/testimonial.html'


# Courses
class CourseListView(ListView):
    model = Course
    template_name = 'home/courses.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'home/detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.object.modules.all()
        return context


# Subjects
class SubjectListView(ListView):
    model = Subject
    template_name = 'home/subject_list.html'
    context_object_name = 'subjects'


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'home/subject_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.object.courses.all()
        return context


# Teachers
class TeacherListView(ListView):
    model = Teacher
    template_name = 'home/teacher_list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.filter(is_active=True)


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'home/teacher_detail.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.object.courses.all()
        return context


# Modules
class ModuleDetailView(DetailView):
    model = Module
    template_name = 'home/module_detail.html'
    pk_url_kwarg = 'module_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contents'] = self.object.contents.all()
        return context


# Content
class ContentDetailView(View):
    template_map = {
        'text': 'home/text.html',
        'image': 'home/image.html',
        'video': 'home/video.html',
        'file': 'home/file.html',
    }

    def get(self, request, content_id):
        content = get_object_or_404(Content, id=content_id)
        item = content.item
        model_name = content.content_type.model
        template = self.template_map.get(model_name)
        return TemplateView.as_view(template_name=template)(request, item=item)


# Extra example
class SomeView(ListView):
    model = Subject
    template_name = 'home/template.html'
    context_object_name = 'subjects'
