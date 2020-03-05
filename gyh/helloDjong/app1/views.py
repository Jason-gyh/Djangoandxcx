from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Article
# Create your views here.
def show_aa(request):
    first_a = Article.objects.all()[0]
    title = first_a.title
    brief_content = first_a.brief_content
    content = first_a.content
    publish_date = first_a.publish_date
    return_str = '文章标题: %s' \
                 ' 文章摘要: %s ' \
                 '文章内容: %s ' \
                 '发布时间: %s' % \
                 (title,brief_content,content,publish_date)
    return HttpResponse(return_str)
def show_a(request):
    first_a = Article.objects.all()
    return render(request,'show.html',{'articles':first_a})
def get_d(request,article_id):
    all_ar = Article.objects.all()
    curr_a = None
    previous_index = 0
    next_index = 0
    pre_ar = None
    ne_ar = None
    for index, article in enumerate(all_ar):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_ar) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_a = article
            pre_ar = all_ar[previous_index]
            ne_ar = all_ar[next_index]
            break
    section_l = curr_a.content.split('\n')
    return render(request,'detail.html',{
        'curr_a': curr_a,
        'section_l': section_l,
        'pre_ar': pre_ar,
        'ne_ar': ne_ar
    })
