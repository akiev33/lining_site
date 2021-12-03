from django.forms import ModelForm

from board_body.models import Post, Stock


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'