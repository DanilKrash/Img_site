from django.shortcuts import render, get_object_or_404

from images.forms import CommentForm

from images.models import Img


def images_views(request):
    context = {'imgs': Img.objects.all() }
    return render(request, 'images/page_1.html', context)


def images_detail_view(request, img_id):
    detail = get_object_or_404(Img, id=img_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = CommentForm
    
    comment = detail.comments.all()
    context = {'img_detail': detail, 'comment': comment}
    return render(request, "images/details.html", context)
