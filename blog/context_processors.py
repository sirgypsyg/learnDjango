from .models import Post

def latest_post(request):
    try:
        return {'latest_post': Post.objects.latest('date_posted')}
    except Post.DoesNotExist:
        return {'latest_post': None}