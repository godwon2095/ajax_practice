from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from .models import Item, Like, Review
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.http import HttpResponse
import json


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'items/item_list.html', context)


def item_show(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'items/item_show.html', context)


@login_required
@require_POST
def like_toggle(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_like, item_like_created = Like.objects.get_or_create(user=request.user, item=item)

    if not item_like_created:
        item_like.delete()
        result = 'heart-empty'
    else:
        result = 'heart'

    context = {
        'result': result
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
@require_POST
def create_review(request, item_id):
    user = request.user
    item = get_object_or_404(Item, pk=item_id)
    body = request.POST.get('body')
    review = Review.objects.create(user=user, item=item, body=body)    

    return redirect('items:show', item.id)
    # return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
# @require_POST
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('items:show', review.item.id)