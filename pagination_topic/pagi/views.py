from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def pag_view(request):
  post = Post.objects.all().order_by('id')
  paginator = Paginator(post,per_page=3,orphans=1)
  page_number = request.GET.get("page")
  page_obj = paginator.get_page(page_number)

  return render(request, "page.html", {"page_obj":page_obj})