from django import forms
from models import UserModel, PostModel, LikeModel, CommentModel,ContactModel

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'name', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image','caption']

class LikeForm(forms.ModelForm):
    class Meta:
        model = LikeModel
        fields=['post']

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text','post']

class MailForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields=['name','subject','feedback','email','number','city']