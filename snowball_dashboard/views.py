from django_nextjs.render import render_nextjs_page

def index(request):
    return render_nextjs_page(request)