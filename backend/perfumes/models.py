from django.db import models

# Create your models here.
class Perfume(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=128)
    img = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    style = models.CharField(max_length=128)
    top = models.CharField(max_length=128, null=True)
    middle = models.CharField(max_length=128, null=True)
    base = models.CharField(max_length=128, null=True)
    smells = models.CharField(max_length=128, null=True)
    attr = models.CharField(max_length=128)
    creater = models.CharField(max_length=128)
    labels = models.CharField(max_length=128)
    rate = models.FloatField()
    time = models.IntegerField()
    main_smells = models.CharField(max_length=10)
    score = models.FloatField(null=True)

class Rate_Perfume(models.Model):
    attr = models.CharField(max_length=128, null=True)

    rank = models.IntegerField()
    rate = models.FloatField()
    user_love_score = models.FloatField(null=True)
    #weight1 = models.FloatField(null=True)

    time = models.IntegerField()
    time_score = models.FloatField(null=True)
    #weight2 = models.FloatField(null=True)

    year = models.IntegerField()
    #year_prefer = models.FloatField(null=True)
    year_score = models.FloatField(null=True)

    #qing_xin = models.FloatField(null=True)
    #gu_dian = models.FloatField(null=True)
    #nong_yu = models.FloatField(null=True)
    #fen_fang = models.FloatField(null=True)
    #ganju_score = models.FloatField(null=True)
    #lvye_score = models.FloatField(null=True)
    #shuisheng_score = models.FloatField(null=True)
    #fuqixiang_score = models.FloatField(null=True)
    #pige_score = models.FloatField(null=True)
    #xipu_score = models.FloatField(null=True)
    #muzhi_score = models.FloatField(null=True)
    #dongfang_score = models.FloatField(null=True)
    #meishi_score = models.FloatField(null=True)
    #huaxiang_score = models.FloatField(null=True)
    #guoxiang_score = models.FloatField(null=True)
    style = models.CharField(max_length=128)
    style_score = models.FloatField(null=True)

    score = models.FloatField(null=True)
