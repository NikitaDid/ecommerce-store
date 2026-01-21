from django.forms import ModelForm

from apps.catalog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'