from django.shortcuts import render
from .models import Post
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm

## this is not the controller
## all the class is that sadinhere is to
## this is used to alter the setting of the generic rendering
## like adding pagination
## inheriting the decorator model
## we use the Postlist.as_view()
## this is the as_view() settings
## you can change three basic thing
## you have to give queryset
                    ## template
                    ## paginate
## because you use the default render function 
## the templatename will be post_list.html
class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'
    paginate_by = 3    


def detail(request,id):
    # we extend the django from in the forms.py
    ## so the registered user can comment
    template_name = 'post_detail.html'
    #return HttpResponse(slug)
    post = get_object_or_404(Post,id=id)

    ## this will be the plural of the comment
    comments = post.comments.filter(active=True)
    new_comment = None
    ## if comment is posted
    if request.method =='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            ## dont immidiatly save the data
            new_comment = comment_form.save(commit=False)
            ## now add the information which post it belongs to
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm() ## empty object

    return render(request,template_name,{
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form ## this will automatically
        #send a form you dont have to everything

    })

