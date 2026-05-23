from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Job, Rating
from .models import UserProfile, Job, Rating, Appointment
from .models import UserProfile
from .models import Message





def home(request):

    return render(request, 'home.html')


def register_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        skills = request.POST.get('skills', '')

        if User.objects.filter(username=username).exists():

            return render(
                request,
                'register.html',
                {
                    'error': 'Username already exists'
                }
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            role=role,
            skills=skills
        )

        login(request, user)

        return redirect('/dashboard/')

    return render(request, 'register.html')


def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # ADMIN LOGIN
            if user.is_superuser:

                return redirect('/admin-dashboard/')

                # NORMAL USER LOGIN
            return redirect('/dashboard/')

        return render(
            request,
            'login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(request, 'login.html')


@login_required
def logout_view(request):

    logout(request)

    return redirect('/')


@login_required
def dashboard(request):

    profile = get_object_or_404(
        UserProfile,
        user=request.user
    )

    # RECENT MESSAGES

    recent_messages = Message.objects.filter(
        receiver=request.user
    ).order_by('-created_at')[:5]
    unread_messages = Message.objects.filter(
    receiver=request.user,
    is_read=False
    ).count()

    # NOTIFICATIONS

    notifications = Appointment.objects.filter(
        buyer=request.user
    ).exclude(
        status="Pending"
    ).order_by('-created_at')[:5]

    # DASHBOARD CONTEXT

    context = {

        'profile': profile,

        'recent_messages': recent_messages,

        'notifications': notifications,
        'unread_messages': unread_messages

    }

    return render(
        request,
        'dashboard.html',
        context
    )


def workers(request):

    query = request.GET.get(
        'q',
        ''
    ).strip()

    workers_list = UserProfile.objects.filter(
        role='seller'
    )

    if query:

        workers_list = workers_list.filter(
            skills__icontains=query
        )

    workers_list = workers_list.order_by(
        '-rating'
    )

    context = {

        'workers': workers_list,

        'query': query

    }

    return render(
        request,
        'workers.html',
        context
    )
def worker_profile(request, worker_id):

    worker = get_object_or_404(
        UserProfile,
        id=worker_id
    )

    ratings = Rating.objects.filter(
        seller=worker
    ).order_by('-created_at')

    context = {
        'worker': worker,
        'ratings': ratings
    }

    return render(
        request,
        'worker_profile.html',
        context
    )


@login_required
def post_job(request):

    if request.method == "POST":

        Job.objects.create(
            buyer=request.user,
            title=request.POST.get('title'),
            category=request.POST.get('category'),
            description=request.POST.get('description'),
            budget=request.POST.get('budget')
        )

        return redirect('/dashboard/')

    return render(request, 'post_job.html')


@login_required
def rate_worker(request, worker_id):

    seller = get_object_or_404(
        UserProfile,
        id=worker_id
    )

    if request.method == "POST":

        stars = int(request.POST.get('stars'))
        review = request.POST.get('review')

        Rating.objects.create(
            buyer=request.user,
            seller=seller,
            stars=stars,
            review=review
        )

        ratings = Rating.objects.filter(
            seller=seller
        )

        total_stars = sum(
            rating.stars for rating in ratings
        )

        average_rating = total_stars / ratings.count()

        seller.rating = round(
            average_rating,
            1
        )

        seller.save()

        return redirect(
            f'/worker/{worker_id}/'
        )

    context = {
        'seller': seller
    }

    return render(
        request,
        'rate_worker.html',
        context
    )
@login_required
def book_appointment(request, worker_id):

    seller = get_object_or_404(
        UserProfile,
        id=worker_id
    )

    if request.method == "POST":

        Appointment.objects.create(

            buyer=request.user,

            seller=seller,

            appointment_date=request.POST.get(
                'appointment_date'
            ),

            appointment_time=request.POST.get(
                'appointment_time'
            ),

            message=request.POST.get(
                'message'
            )

        )

        return redirect(
            f'/worker/{worker_id}/'
        )

    context = {
        'seller': seller
    }

    return render(
        request,
        'book_appointment.html',
        context
    )
@login_required
def seller_appointments(request):

    profile = get_object_or_404(
        UserProfile,
        user=request.user
    )

    appointments = Appointment.objects.filter(
        seller=profile
    ).order_by('-created_at')

    context = {
        'appointments': appointments
    }

    return render(
        request,
        'seller_appointments.html',
        context
    )



@login_required
def admin_dashboard(request):

    total_users = User.objects.count()

    total_sellers = UserProfile.objects.filter(
        role='seller'
    ).count()

    total_buyers = UserProfile.objects.filter(
        role='buyer'
    ).count()

    total_jobs = Job.objects.count()

    total_appointments = Appointment.objects.count()

    total_reviews = Rating.objects.count()

    recent_appointments = Appointment.objects.order_by(
        '-created_at'
    )[:5]

    context = {

        'total_users': total_users,
        'total_sellers': total_sellers,
        'total_buyers': total_buyers,
        'total_jobs': total_jobs,
        'total_appointments': total_appointments,
        'total_reviews': total_reviews,
        'recent_appointments': recent_appointments

    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )
@login_required
def edit_profile(request):

    profile = UserProfile.objects.get(
        user=request.user
    )

    if request.method == "POST":

        profile.skills = request.POST.get(
            'skills'
        )

        profile.education = request.POST.get(
            'education'
        )

        profile.certification = request.POST.get(
            'certification'
        )

        profile.bio = request.POST.get(
            'bio'
        )

        profile.experience = request.POST.get(
            'experience'
        )

        profile.price = request.POST.get(
            'price'
        )

        if request.FILES.get('profile_image'):

            profile.profile_image = request.FILES.get(
                'profile_image'
            )

        if request.FILES.get('work_image'):

            profile.work_image = request.FILES.get(
                'work_image'
            )

        if request.FILES.get('intro_video'):

            profile.intro_video = request.FILES.get(
                'intro_video'
            )

        profile.save()

        return redirect('/dashboard/')

    return render(
        request,
        'edit_profile.html',
        {
            'profile': profile
        }
    )



@login_required
def chat_view(request, user_id):

    other_user = User.objects.get(
        id=user_id
    )

    messages = Message.objects.filter(

        sender__in=[request.user, other_user],

        receiver__in=[request.user, other_user]

    ).order_by('created_at')
    Message.objects.filter(

    sender=other_user,

    receiver=request.user,

    is_read=False

).update(

    is_read=True

)

    if request.method == "POST":

        text = request.POST.get('message')

        if text:

            Message.objects.create(

                sender=request.user,

                receiver=other_user,

                message=text

            )

        return redirect(
            'chat',
            user_id=other_user.id
        )

    return render(
        request,
        'chat.html',
        {
            'other_user': other_user,
            'messages': messages
        }
    )

@login_required
def accept_appointment(request, appointment_id):

    appointment = Appointment.objects.get(
        id=appointment_id
    )

    appointment.status = "Accepted"

    appointment.save()

    return redirect('/seller-appointments/')


@login_required
def reject_appointment(request, appointment_id):

    appointment = Appointment.objects.get(
        id=appointment_id
    )

    appointment.status = "Rejected"

    appointment.save()

    return redirect('/seller-appointments/')

@login_required
def buyer_appointments(request):

    appointments = Appointment.objects.filter(
        buyer=request.user
    ).order_by('-created_at')

    context = {
        'appointments': appointments
    }

    return render(
        request,
        'buyer_appointments.html',
        context
    )




@login_required
def check_notifications(request):

    accepted = Appointment.objects.filter(

        buyer=request.user,

        status="Accepted"

    ).count()

    rejected = Appointment.objects.filter(

        buyer=request.user,

        status="Rejected"

    ).count()

    return JsonResponse({

        'accepted': accepted,

        'rejected': rejected

    })