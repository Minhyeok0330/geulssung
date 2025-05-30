# Generated by Django 5.2.1 on 2025-05-28 02:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prompts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('T', '논리적 글쓰기'), ('F', '감정적 글쓰기')], max_length=1)),
                ('genre', models.CharField(choices=[('column', '칼럼'), ('analysis', '분석글'), ('essay', '에세이'), ('poem', '시')], max_length=20)),
                ('step1', models.TextField(blank=True)),
                ('step2', models.TextField(blank=True)),
                ('step3', models.TextField(blank=True)),
                ('final_content', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('prompt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referenced_posts', to='prompts.generatedprompt')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
