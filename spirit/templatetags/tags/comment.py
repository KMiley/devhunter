# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext as _

from . import register
from spirit.forms.comment import CommentForm
from spirit.models.comment import Comment, MOVED, CLOSED, UNCLOSED, PINNED, UNPINNED


@register.assignment_tag()
def get_comment_list(topic):
    return Comment.objects.for_topic(topic).order_by('date')


@register.inclusion_tag('spirit/comment/_form.html')
def render_comments_form(topic, next=None):
    form = CommentForm()
    return {'form': form, 'topic_id': topic.pk, 'next': next, 'STATIC_URL': settings.STATIC_URL}


@register.simple_tag()
def get_comment_action_text(action):
    if action == MOVED:
        return _("This topic has been moved")
    elif action == CLOSED:
        return _("This topic has been closed")
    elif action == UNCLOSED:
        return _("This topic has been unclosed")
    elif action == PINNED:
        return _("This topic has been pinned")
    elif action == UNPINNED:
        return _("This topic has been unpinned")
    else:
        return _("Unknown topic moderation action")
