from django.db import models
import datetime as dt
from django.utils import timezone


class Account(models.Model):
    """
        Public population of SASTRA will be given an account each
        Register Number is the primary key.
        Since a club member has to be a student of SASTRA, class Member inherits Account.
    """
    name = models.CharField(max_length=50)
    register_no = models.PositiveIntegerField(unique=True)
    sastra_email = models.EmailField()
    branch = models.CharField(max_length=100)
    batch = models.PositiveIntegerField()
    posts = models.TextField(default="[0]")
    password = models.CharField(max_length=128)
    # posts stores list of post_id as a json string. will dump and load whenever necessary.


class Member(models.Model):
    """
        Class for Permanent Members of SALVO.
        Roles = {Member, Advisor, Coordinator, Lead}
        TO-DO: Find Formula for Contribution Score
        Privileges: Can Verify Posts, apart from posting.
    """
    name = models.CharField(max_length=50)
    register_no = models.PositiveIntegerField(unique=True)
    sastra_email = models.EmailField()
    branch = models.CharField(max_length=100)
    batch = models.PositiveIntegerField()
    posts = models.TextField(default="[0]")
    password = models.CharField(max_length=128)
    club_role = models.CharField(max_length=40)
    join_date = models.DateField(default=timezone.now)
    contribution_score = models.FloatField(default=0.0)
    attendance_percentage = models.FloatField(default=0.0)

    @property
    def is_coordinator_or_above(self):
        return self.club_role in ['Lead', 'Co-ordinator', 'Advisor']


class Post(models.Model):
    """
        Class for Storage of Posted Contents.
        Verification done by members only.
        Verified_by attribute points to regno of Member who verified.
        likes is an attribute to track like count.
        author_reg_no points to regno of Account that posts the post.
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author_reg_no = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    verified_by = models.PositiveIntegerField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    tags = models.JSONField(default=list)


class JoinRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    applicant_name = models.CharField(max_length=50, blank=True, null=True)
    applicant_reg_no = models.PositiveIntegerField(blank=True, null=True)
    reason_to_join = models.TextField()
    why_recruit = models.TextField()
    other_clubs = models.TextField()
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    upvotes = models.ManyToManyField(Member, blank=True)

    def save(self, *args, **kwargs):
        if self.account:
            self.applicant_name = self.account.name
            self.applicant_reg_no = self.account.register_no
        super().save(*args, **kwargs)

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    register_no = models.PositiveIntegerField()  # from Account or Member

    class Meta:
        unique_together = ('post', 'register_no')
