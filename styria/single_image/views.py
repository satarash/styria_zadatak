from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from models import Image
from forms import UploadImageForm


class SingleImageDetailView(DetailView):
    model = Image
    template_name = 'single_image/single.html'
    context_object_name = 'image'


class AllImagesListView(ListView):
    model = Image
    template_name = 'single_image/list.html'
    context_object_name = 'images'
    paginate_by = settings.PAGINATION_PAGE_SIZE


class UploadImageCreate(CreateView):
    model = Image
    template_name = 'single_image/upload.html'
    context_object_name = 'image'
    form_class = UploadImageForm
    success_url = reverse_lazy('single_image')
