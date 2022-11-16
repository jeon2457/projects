import markdown  # 마크다운 필터
from django.utils.safestring import mark_safe  # 마크다운 필터
from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


# 마크다운 필터 등록
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
