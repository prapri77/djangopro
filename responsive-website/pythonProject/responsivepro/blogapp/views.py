from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'main.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def my_view(request):
    # Access the Host header
    host_header = request.headers.get('Host', '')

    # Do something with the host header
    if host_header == 'prasanth.shop':
        return HttpResponse("Host header matches prasanth.shop")
    else:
        return HttpResponse("Host header does not match prasanth.shop")

