from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):

        return self.name
class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20
    )

    skills = models.ManyToManyField(
    Skill,
    blank=True
)

    qualification = models.CharField(
        max_length=200,
        blank=True
    )

    education = models.CharField(
        max_length=300,
        blank=True
    )

    certification = models.CharField(
        max_length=300,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    about = models.TextField(
        blank=True
    )

    experience = models.IntegerField(
        default=0
    )

    pricing = models.IntegerField(
        default=500
    )

    price = models.IntegerField(
        default=0
    )

    rating = models.FloatField(
        default=4.5
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    portfolio = models.FileField(
        upload_to='portfolio/',
        blank=True,
        null=True
    )

    work_image = models.ImageField(
        upload_to='work_images/',
        blank=True,
        null=True
    )

    work_video = models.FileField(
        upload_to='work_videos/',
        blank=True,
        null=True
    )

    def __str__(self):

        return self.user.username


class Job(models.Model):

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    category = models.ForeignKey(
    Skill,
    on_delete=models.SET_NULL,
    null=True
)

    description = models.TextField()

    budget = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title


class Rating(models.Model):

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='worker_ratings'
    )

    stars = models.IntegerField()

    review = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.buyer.username} rated {self.seller.user.username}"


class Appointment(models.Model):

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyer_appointments'
    )

    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='seller_appointments'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.buyer.username} booked {self.seller.user.username}"


class Message(models.Model):

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    def __str__(self):

        return f"{self.sender} -> {self.receiver}"


class Review(models.Model):

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.buyer.username} reviewed {self.seller.user.username}"
    
class JobInterest(models.Model):

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.seller.user.username} -> {self.job.title}"
class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message = models.CharField(
        max_length=300
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.message
    
