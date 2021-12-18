from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import get_user_model
from .models import Message
from django.urls import reverse
from django.contrib import messages
from review.models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from django.template import RequestContext


def handler404(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


class HomePageView(TemplateView):
    template_name = 'home.html'


def MessageView(request, username):
    User = get_user_model()
    message_user = get_object_or_404(User, username=username)
    all_messages = message_user.messages.all()
    if request.method == 'POST':
        message = request.POST['message']
        user_new_message = Message.objects.create(
            customuser=message_user, text=message)
        user_new_message.save()
        messages.success(
            request, 'Compliments dropped successfully, Create your own Account below to receive and give Anonymous compliments')
        return redirect('account_signup')

    return render(request, 'message.html', {'all_messages': all_messages,
                                            'message_user': message_user,
                                            })


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'


CustomUser = get_user_model()


@login_required(login_url='account_login')

def EditProfile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # user_profile = user.get_absolute_url()
            user_profile = reverse('user_profile')
            return HttpResponseRedirect(user_profile)

    form = EditProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='account_login')
def delete_message(request, m_id):
    message_instance = get_object_or_404(Message, id=m_id)
    message_instance_user = message_instance.customuser
    if message_instance_user == request.user:
        message_instance.delete()
        return redirect(message_instance_user.get_absolute_url())
    else:
        return redirect('home')


@login_required(login_url='account_login')
def spam_message(request, m_id):
    # get the Message filtering by the id provided in the url as *args
    message_instance = get_object_or_404(Message, id=m_id)
    # the person who created the message
    message_instance_user = message_instance.customuser
    if message_instance_user == request.user:
        message_instance.text = 'The owner has marked this message as a spam.'
        message_instance.save()
        return redirect(message_instance_user.get_absolute_url())

    else:
        if request.user.is_authenticated:
            url = 'home'
        else:
            url = 'account_login'
        return redirect(url)


class AbouUs(TemplateView):
    template_name = 'about.html'


class ContactUs(TemplateView):
    template_name = 'contact.html'


def ReviewView(request):
    reviews = Review.objects.all()
    template_name = "review.html"
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(page_number)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, template_name, {'page_obj': page_obj})


@login_required(login_url='account_login')
def SettingsView(request):

    return render(request, 'settings.html', {})


def AddReview(request):
    if request.method == 'POST':
        name = request.POST['name']
        review = request.POST['review']
        occupation = request.POST['occupation']

        new_review = Review.objects.create(
            name=name, review=review, occupation=occupation)
        new_review.save()
        messages.success(request, 'Review submitted successfully')
        return redirect('review')
    return render(request, 'add_review.html', {})
