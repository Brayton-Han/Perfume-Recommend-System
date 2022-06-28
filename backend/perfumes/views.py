from email import message
from django.shortcuts import render, redirect
from perfumes.forms import queryForm
from perfumes.models import Perfume, Rate_Perfume
import matlab.engine
eng = matlab.engine.start_matlab()
dic = {'柑橘调': 0.95, '柑橘美食调': 0.6, '柑橘馥奇香调': 0.7, '绿叶调': 0.95, '绿叶馥奇香调': 0.75, 
       '绿叶花香调': 0.7, '水生调': 0.95, '水生馥奇香调': 0.8, '水生花香调': 0.65, '水生木质调': 0.55, 
       '馥奇香调': 0.95, '果香馥奇香调': 0.55, '辛辣馥奇香调': 0.5, '木质馥奇香调': 0.7, '东方馥奇香调': 0.65, 
       '皮革调': 1, '西普调': 0.95, '花香西普调': 0.55, '果香西普调': 0.5, '木质西普调': 0.8, '木质调': 0.95, 
       '木质花香调': 0.7, '辛辣木质调': 0.5, '木质东方调': 0.9, '东方调': 0.95, '东方花香调': 0.75, '辛辣东方调': 0.5, 
       '东方美食调': 0.9, '美食调': 0.95, '花果香美食调': 0.775, '花香调': 0.95, '醛香花香调': 0.5, '花香果香调': 0.9,
       '果香调': 0.95}

# Create your views here.
def getForm(request):
    query_form = queryForm()
    if request.method == "POST":
        eng.cd('C:/Users/dell/Desktop/Expert_System/backend/perfumes')
        rate_list = Rate_Perfume.objects.all()
        query_form = queryForm(request.POST)
        if query_form.is_valid():  # 获取数据
            if query_form.cleaned_data['men']:
                rate_list = rate_list.exclude(attr="男香")
            if query_form.cleaned_data['mid']:
                rate_list = rate_list.exclude(attr="中性香")
            if query_form.cleaned_data['women']:
                rate_list = rate_list.exclude(attr="女香")
            weight1 = query_form.cleaned_data['weight1']
            weight2 = query_form.cleaned_data['weight2']
            year_prefer = query_form.cleaned_data['year_prefer']
            qingxin = query_form.cleaned_data['qing_xin']
            gudian = query_form.cleaned_data['gu_dian']
            nongyu = query_form.cleaned_data['nong_yu']
            fenfang = query_form.cleaned_data['fen_fang']

            xiangdiao_scores = eng.style(qingxin, gudian, nongyu, fenfang)[0]
            ganju_score = xiangdiao_scores[0]
            lvye_score = xiangdiao_scores[1]
            shuisheng_score = xiangdiao_scores[2]
            fuqixiang_score = xiangdiao_scores[3]
            pige_score = xiangdiao_scores[4]
            xipu_score = xiangdiao_scores[5]
            muzhi_score = xiangdiao_scores[6]
            dongfang_score = xiangdiao_scores[7]
            meishi_score = xiangdiao_scores[8]
            huaxiang_score = xiangdiao_scores[9]
            guoxiang_score = xiangdiao_scores[10]

            #print('test!!!')
            for r in rate_list:
                s1 = weight1 * r.user_love_score
                s2 = weight2 * r.time_score

                r.year_score = eng.year_score(r.year, year_prefer)
                r.save()

                style_score = 0
                if r.style.find('柑') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * ganju_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * ganju_score
                if r.style.find('绿') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * lvye_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * lvye_score
                if r.style.find('水') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * shuisheng_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * shuisheng_score
                if r.style.find('馥') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * fuqixiang_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * fuqixiang_score
                if r.style.find('皮') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * pige_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * pige_score
                if r.style.find('西') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * xipu_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * xipu_score
                if r.style.find('木') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * muzhi_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * muzhi_score
                if r.style.find('东') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * dongfang_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * dongfang_score
                if r.style.find('美') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * meishi_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * meishi_score
                if r.style.find('花') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * huaxiang_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * huaxiang_score
                if r.style.find('果') != -1:
                    if style_score == 0:
                        style_score = dic[r.style] * guoxiang_score
                    else:
                        style_score = style_score * 0.5 + 0.5 * dic[r.style] * guoxiang_score
                r.style_score = style_score
                r.save()

                r.score = 0.1 * s1 + 0.2 * s2 + 0.1 * r.year_score + 0.6 * r.style_score
                r.save()
                Perfume.objects.filter(rank=r.rank).update(score=r.score)

            #print('Alright!!!')
            return redirect('recommand')

        else:
            message = "请检查填写的表单是否有误"

    return render(request, "queryPerfume.html", locals())

def recommand(request):
    rate_list = Rate_Perfume.objects.all().order_by('-score')
    top_list = rate_list[0:7]
    recommand_list = []
    for t in top_list:
        recommand_list.append(Perfume.objects.get(rank=t.rank))
    for r in rate_list:
        r.score = 0
        r.save()
    return render(request, "recommand.html", locals())