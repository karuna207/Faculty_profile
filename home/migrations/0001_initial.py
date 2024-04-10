# Generated by Django 4.2.7 on 2024-03-16 04:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Archive",
            fields=[
                (
                    "model_name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("archived_data", models.JSONField()),
                ("deleted_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "course_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("course_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Faculty_Login",
            fields=[
                (
                    "username",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="profile_pics"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.faculty_login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professionalexp",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("designation", models.CharField(max_length=100)),
                ("institution_code", models.CharField(max_length=50)),
                ("from_date", models.DateField()),
                ("to_date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.faculty_login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProfessionalDetail",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("designation", models.CharField(max_length=100)),
                (
                    "highest_qualification",
                    models.CharField(
                        choices=[
                            ("Bachelor", "Bachelor"),
                            ("Master", "Master"),
                            ("PhD", "PhD"),
                        ],
                        max_length=20,
                    ),
                ),
                ("joining_date", models.DateField(default=django.utils.timezone.now)),
                ("leaving_date", models.DateField(blank=True, null=True)),
                (
                    "languages_known",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "programming_languages",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.faculty_login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PersonalDetail",
            fields=[
                (
                    "digital_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "contact_no",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinLengthValidator(10),
                            django.core.validators.MaxLengthValidator(10),
                        ]
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("email_id", models.EmailField(max_length=100)),
                ("aicte_id", models.CharField(max_length=50)),
                (
                    "blood_grp",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("B+", "B+"),
                            ("AB+", "AB+"),
                            ("O+", "O+"),
                            ("A-", "A-"),
                            ("B-", "B-"),
                            ("AB-", "AB-"),
                            ("O-", "O-"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "faculty_login",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.faculty_login",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoursesTaught",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.course"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Award",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("awardname", models.CharField(max_length=255)),
                ("year_of_rec", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AcademicPerformance",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("degree", models.CharField(max_length=100)),
                ("institution_code", models.CharField(max_length=50)),
                ("year_of_completion", models.DateField()),
                ("remark", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]