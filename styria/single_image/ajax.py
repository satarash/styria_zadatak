from django.template.loader import render_to_string
from django.db.models import Avg

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from models import Comment, Image, Rating


@dajaxice_register
def insert_comment(request, text, image):
    dajax = Dajax()
    if text == '':
        return dajax.json()
    else:
        dajax = Dajax()
        Comment.objects.create(text=text, image=Image.objects.get(pk=image))
        dajax.assign('#id_text', 'value', '')
        comments = Comment.objects.filter(image=image)
        render_comments = render_to_string('single_image/comments.html', {'comments': comments, })
        dajax.assign('#comments', 'innerHTML', render_comments)
        return dajax.json()


@dajaxice_register
def load_single(request, image):
    dajax = Dajax()
    comments = Comment.objects.filter(image=image)
    ratings = Rating.objects.filter(image=image)[:5]
    render_comments = render_to_string('single_image/comments.html', {'comments': comments, })
    dajax.assign('#comments', 'innerHTML', render_comments)
    render_ratings = render_to_string('single_image/ratings.html', {'ratings': ratings, })
    dajax.assign('#ratings', 'innerHTML', render_ratings)
    average_rating = Rating.objects.filter(image=image).aggregate(Avg('rating'))
    dajax.assign('#average_rating', 'innerHTML', round(average_rating['rating__avg'], 2))
    return dajax.json()


@dajaxice_register
def insert_rating(request, rating, image):
    dajax = Dajax()
    Rating.objects.create(rating=rating, image=Image.objects.get(pk=image))
    average_rating = Rating.objects.filter(image=image).aggregate(Avg('rating'))
    dajax.assign('#average_rating', 'value', average_rating)
    ratings = Rating.objects.filter(image=image)[:5]
    render_ratings = render_to_string('single_image/ratings.html', {'ratings': ratings, })
    dajax.assign('#ratings', 'innerHTML', render_ratings)
    dajax.assign('#average_rating', 'innerHTML', round(average_rating['rating__avg'], 2))
    return dajax.json()
