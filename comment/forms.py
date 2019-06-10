from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'content_type', 'object_id']
        widgets = {
            'content_type':forms.HiddenInput(),
            'object_id':forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = ""
        self.fields['text'].widget.attrs = {'class': "form-control", 'placeholder': "댓글을 남겨주세요."}