from .models import Thread, Comment

def sidebar(request):
    threads = Thread.objects.order_by('-created_at')[:5]
    for thread in threads:
        thread.content = thread.content[:140] + (thread.content[140:] and '...')
    comments = Comment.objects.order_by('-created_at')[:5]
    for comment in comments:
        comment.content = comment.content[:140] + (comment.content[140:] and '...')
    return {
        "new_threads": threads,
        "new_comments": comments
    }