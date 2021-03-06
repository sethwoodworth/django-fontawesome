from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def fontawesome_icon(icon, size=False, fixed=False, spin=False, li=False,
    rotate=False, border=False, color=False):
    size = 

    return '<i class="{prefix} {prefix}-{icon}{size}{fixed}{spin}{li}{rotate}{border}"{color}></i>'.format(
        prefix=getattr(settings, 'FONTAWESOME_PREFIX', 'fa'),
        icon=icon,
        size=' fa-lg' if size == 'large' else 'fa-{size}'.format(size),
        fixed=' fa-fw' if fixed else '',
        spin=' fa-spin' if spin else '',
        li=' fa-li' if li else '',
        rotate=' fa-rotate-%s' % str(rotate) if rotate else '',
        border=' fa-border' if border else '',
        color='style="color:%s;"' % color if color else ''
    )

@register.simple_tag
def fontawesome_stylesheet():
    href = getattr(settings, 'FONTAWESOME_CSS_URL', static('fontawesome/css/font-awesome.min.css'))
    link = format_html('<link href="{0}" rel="stylesheet" media="all">', href)
    return link
