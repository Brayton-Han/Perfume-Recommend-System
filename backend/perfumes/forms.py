from django import forms 

class queryForm(forms.Form):
    men = forms.BooleanField(label="男香:", required=False)
    mid = forms.BooleanField(label="中性香:", required=False)
    women = forms.BooleanField(label="女香:", required=False)
    weight1 = forms.FloatField(label="用户喜爱度偏好:")
    weight2 = forms.FloatField(label="留香时间偏好:")
    year_prefer = forms.FloatField(label="年代偏好:")
    qing_xin = forms.FloatField(label="清新偏好:")
    gu_dian = forms.FloatField(label="古典偏好:")
    nong_yu = forms.FloatField(label="浓郁偏好:")
    fen_fang = forms.FloatField(label="芬芳偏好:")
