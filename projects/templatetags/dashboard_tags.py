from django import template
from projects.models import Project
from blogs.models import Blog
from contacts.models import Contact

register = template.Library()

@register.simple_tag
def get_dashboard_stats():
    return {
        'projects': Project.objects.count(),
        'blogs': Blog.objects.count(),
        'unread_messages': Contact.objects.filter(is_read=False).count(),
    }
