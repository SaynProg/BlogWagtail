from home.models import FooterModel

from django import template

register = template.Library()

@ register.inclusion_tag('home/tags/footer.html', takes_context=True)
def footer_tag(context):
	return {
		'request':context['request'],
		'footer':FooterModel.objects.first()
	}