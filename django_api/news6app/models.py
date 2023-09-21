from django.db import models

# Create your models here.
class Category(models.Model):
    cat2_id = models.SmallIntegerField(primary_key=True)
    cat1_name = models.CharField(max_length=16)
    cat2_name = models.CharField(max_length=16)
    platform_name = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'CATEGORY'


class Comment(models.Model):
    news = models.ForeignKey('News', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    comment = models.TextField()
    date_upload = models.DateTimeField()
    date_fix = models.DateTimeField(blank=True, null=True)
    good_cnt = models.SmallIntegerField(blank=True, null=True)
    bad_cnt = models.SmallIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.pk) + str(self.comment)

    class Meta:
        managed = False
        db_table = 'COMMENT'


class News(models.Model):
    cat2 = models.ForeignKey(Category, models.DO_NOTHING)
    title = models.CharField(max_length=256)
    press = models.CharField(max_length=16, blank=True, null=True)
    writer = models.CharField(max_length=32, blank=True, null=True)
    date_upload = models.DateTimeField()
    date_fix = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sticker = models.JSONField()
    url = models.CharField(unique=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'NEWS'


class User(models.Model):
    user_id = models.CharField(unique=True, max_length=8, db_collation='utf8mb3_bin')
    user_name = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USER'