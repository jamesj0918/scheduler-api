# Generated by Django 2.1.3 on 2018-11-19 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, '없음'), (1, '상경계'), (2, '인문학'), (3, '사회과학'), (4, '국방/군사/경찰'), (5, '과학/공학'), (6, '예술'), (7, '언어'), (8, '진로'), (9, '취미/생활')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16, verbose_name='lecture id')),
                ('division', models.CharField(default=1, max_length=8, verbose_name='division')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('type', models.IntegerField(blank=True, choices=[(0, '중핵필수'), (4, '중핵필수선택'), (2, '자유선택교양'), (3, '전공필수'), (4, '전공선택'), (5, '전공기초교양')], default=0, null=True, verbose_name='lecture type')),
                ('grade', models.IntegerField(blank=True, default=1, null=True, verbose_name='grade')),
                ('point', models.FloatField(blank=True, default=1.0, null=True, verbose_name='point')),
                ('language', models.IntegerField(blank=True, choices=[(0, '한국어'), (1, '영어'), (2, '영어/한국어')], default=0, null=True, verbose_name='language')),
                ('classroom', models.CharField(blank=True, max_length=16, null=True, verbose_name='classroom')),
                ('professor', models.CharField(blank=True, max_length=32, null=True, verbose_name='professor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='lecture.Category', verbose_name='category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='lecture.Department', verbose_name='department')),
                ('origin_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_lectures', to='lecture.Department', verbose_name='origin department')),
            ],
        ),
        migrations.CreateModel(
            name='LectureTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, '월'), (1, '화'), (2, '수'), (3, '목'), (4, '금')], default=0)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='lecture.Lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.IntegerField(choices=[(0, '없음'), (1, '경제'), (2, '경영'), (3, '마케팅'), (4, '철학'), (5, '문학'), (6, '역사/문화'), (7, '행정'), (8, '심리'), (9, '교육학'), (10, '법'), (11, '사회학'), (12, '언론/신문/방송'), (13, '기계/전기/전자'), (14, '도시/토목/건설'), (15, '물리학'), (16, '생물학'), (17, '수학'), (18, '천문/지구과학'), (19, '화학'), (20, '컴퓨터'), (21, '무용'), (22, '미술'), (23, '음악'), (24, '연극/영화'), (25, '대중문화'), (26, '국어'), (27, '영어'), (28, '일본어'), (29, '중국어'), (30, '창업/취업'), (31, '진로'), (32, '논술/면접대비'), (33, '공무원/자격증'), (34, '고시'), (35, '자기능력계발'), (36, '리빙'), (37, '레저/스포츠'), (38, '여성/패션')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='lecture.Subcategory', verbose_name='subcategory'),
        ),
    ]
