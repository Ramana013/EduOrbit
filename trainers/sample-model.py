from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from shared.constants import COUNTRY_CODES
from .forms import IT_EXPERIENCE_CHOICES
from courseapp.models import Course
from trainers.models import Qualification, Awards
from django.conf import settings


# Validate Gmail address function
def validate_gmail(email):
    if not email.endswith('@gmail.com'):
        raise ValidationError("Email must be a Gmail address.")

# Trainer Model (Updated Version)
class Trainer(models.Model):
    COURSES_TO_TRAIN_CHOICES = [
        ('', ''),
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('Django', 'Django'),
        ('Flask', 'Flask'),
        ('Machine Learning', 'Machine Learning'),
        ('Data Science', 'Data Science'),
        ('Web Development', 'Web Development'),
        ('Other', 'Any Other Course'),
    ]
    QUALIFICATION_CHOICES = [
        ('', ''),
        ('BCA', 'BCA'),
        ('B.E', 'B.E'),
        ('B.Sc', 'B.Sc'),
        ('B.Tech', 'B.Tech'),
        ('MBA', 'MBA'),
        ('MCA', 'MCA'),
        ('M.E', 'M.E'),
        ('M.Sc', 'M.Sc'),
        ('M.Tech', 'M.Tech'),
        ('Ph.D', 'Ph.D'),
        ('Other', 'Any Other Qualification'),
    ]

    IT_EXPERIENCE_CHOICES= [
        ('', ''),
        ('0-2 years', '0-2 years'),
        ('2-5 years', '2-5 years'),
        ('5-10 years', '5-10 years'),
        ('10+ years', '10+ years'),
    ]
    AWARDS_CHOICES = [
        ('', ''),
        ('Best Trainer', 'Best Trainer'),
        ('Outstanding Performance', 'Outstanding Performance'),
        ('Excellence in Teaching', 'Excellence in Teaching'),
        ('Innovative Teaching Methodology', 'Innovative Teaching Methodology'),
        ('Other', 'Any Other Award'),
    ]
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]


    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    dob = models.DateField(verbose_name="Date of Birth")
    experience = models.PositiveIntegerField(verbose_name="Training Experience (Years)", choices = IT_EXPERIENCE_CHOICES, default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    profile_pic = models.ImageField(upload_to='trainers/', blank=True, null=True)

    # New fields based on your UI
    prior_batches = models.PositiveIntegerField(verbose_name="No. of Prior Batches", default=0)
    prior_aspirants = models.PositiveIntegerField(verbose_name="No. of Prior Aspirants", default=0)
    prior_weekly_tests = models.PositiveIntegerField(verbose_name="No. of Weekly Tests Conducted", default=0)

    # Relationships
    courses_to_train = models.ManyToManyField(
        'courseapp.Course',
        related_name='trainers_to_teach',
        verbose_name="Courses to Train",
        blank=True,
        help_text="Select one or more courses the trainer is capable of teaching.",
        choices=COURSES_TO_TRAIN_CHOICES
    )
    other_courses_to_train = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Other Courses (if applicable)"
    )

    qualifications = models.ManyToManyField(
        'trainers.Qualification',
        related_name='qualified_trainers',
        verbose_name="Trainer Qualifications",
        blank=True,
        choices=QUALIFICATION_CHOICES,
    )
    other_qualifications = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Other Qualifications (if applicable)"
    )

    awards = models.ForeignKey(
        'trainers.Awards',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Award",
        choices=AWARDS_CHOICES,

    )
    other_awards = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Other Awards (if applicable)"
    )

    # Replacing ForeignKey with direct field in ITExperience
    it_experience = models.CharField(
    max_length=100,
    choices=IT_EXPERIENCE_CHOICES,
    verbose_name="IT Experience",
    blank=True,
    null=True
)

    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=10, default='+91')
    phone = models.CharField(max_length=15)

    status = models.BooleanField(default=True, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trainer_detail', kwargs={'pk': self.pk})
    
#deepseek trainer model


# class Qualification(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

# class Organization(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# class Trainer(models.Model):
#     STATUS_CHOICES = [
#         ('active', 'Active'),
#         ('inactive', 'Inactive'),
#         ('on_leave', 'On Leave'),
#     ]

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100, blank=True)
#     bio = models.TextField()
#     dob = models.DateField()
#     training_experience = models.PositiveIntegerField(default=0)
#     rating = models.FloatField(
#         validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
#         default=5.0,
#         blank=True,
#         null=True
#     )
#     prior_batches = models.PositiveIntegerField(default=0)
#     prior_aspirants = models.PositiveIntegerField(default=0)
#     prior_weekly_tests = models.PositiveIntegerField(default=0)
#     picture = models.ImageField(upload_to='trainers/profile_pics/', blank=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
#     qualifications = models.ManyToManyField(Qualification, through='TrainerQualification')
#     courses = models.ManyToManyField(Course)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.user.get_full_name()} ({self.title})"

#     @property
#     def age(self):
#         from datetime import date
#         return date.today().year - self.dob.year if self.dob else None

# class TrainerQualification(models.Model):
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
#     qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
#     year_obtained = models.PositiveIntegerField()

#     class Meta:
#         unique_together = ('trainer', 'qualification')

# class ITExperience(models.Model):
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     position = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)
#     currently_working = models.BooleanField(default=False)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.position} at {self.organization}"

# class Award(models.Model):
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     awarding_body = models.CharField(max_length=200)
#     year_received = models.PositiveIntegerField()
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.name} ({self.year_received})"
    
# #end of deepseek trainer model



# Commented out older Trainer Model (To be deleted or kept for reference)
# class Trainer(models.Model):
#     name = models.CharField(max_length=25)
#     qualification = models.CharField(max_length=10)
#     college = models.CharField(max_length=30, verbose_name="College/University")
#     experience = models.PositiveIntegerField(verbose_name="IT Experience in Years", validators=[MinValueValidator(3), MaxValueValidator(50)])
#     training_exp = models.PositiveIntegerField(verbose_name="Training Experience in Years", validators=[MinValueValidator(3), MaxValueValidator(50)])
#     email = models.EmailField(
#         max_length=60, 
#         validators=[validate_gmail],
#         help_text="This will be used to communicate with trainers officially by administrator")
#     country_code = models.CharField(max_length=3, choices=COUNTRY_CODES, default='+91')
#     phone_number = models.CharField(
#         max_length=10,
#         validators=[RegexValidator(r'^\d{10}$', 'Mobile number must be exactly 10 digits.')],
#         help_text='Mobile number will be used to communicate with Trainer by Administrator over WhatsApp',
#     )
#     rating = models.DecimalField(
#         verbose_name="Rating (1-5)", 
#         max_digits=3, 
#         decimal_places=1, 
#         validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
#     )
#     status = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Shri. {self.name}, {self.qualification}, {self.experience} yrs Experience"

#     def save(self, *args, **kwargs):
#         super(Trainer, self).save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('trainer_one', kwargs={'pk': self.pk})

# Colleges Model (No change required, just for clarity)
class Colleges(models.Model):
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.full_name

# Degree Model
class Degree(models.Model):
    title = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    certificate = models.FileField(upload_to='certificates/')

    def __str__(self):
        return self.title

# Organization Model
class Organization(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    short_name = models.CharField(max_length=50, verbose_name="Short Name")
    from_year = models.PositiveIntegerField(
        verbose_name="From Year",
        help_text="The year when the trainer started working in the organization"
    )
    to_year = models.PositiveIntegerField(
        verbose_name="To Year",
        default=0,
        help_text="The ending year of the experience (0 means currently working)"
    )
    
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )

    def __str__(self):
        return self.full_name

# Qualification Model
class Qualification(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    
    degree = models.ForeignKey(
        Degree,
        on_delete=models.CASCADE,
        related_name='qualifications'
    )
    college = models.ForeignKey(
        Colleges,  
        on_delete=models.CASCADE,
        related_name='qualifications'
    )
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )

    def __str__(self):
        return f"{self.degree.title} from {self.college.full_name}"

# Awards Model
class Awards(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive'),
    ]
    name = models.CharField(max_length=100, blank=True, null=True, default="Unknown Award")  # Add default value here
    full_title = models.CharField(max_length=255, verbose_name="Full Title")
    short_title = models.CharField(max_length=100, verbose_name="Short Title")
    certificate = models.ImageField(
        upload_to='award_certificates/',
        null=True,
        blank=True,
        verbose_name="Certificate"
    )
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
        verbose_name="Status"
    )

    def __str__(self):
        return self.short_title