from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,Page
from django.http import HttpResponse
# Create your views here.
def index(request):
    '''
    模板中需要的数据,就从视图中传递过去
     需要的数据:分类, 3个最热商品, 4个最新商品{type: , hot: , new: }
     共六个分类[{},{},{}...]
    '''
    goods=[]
    tlist=TypeInfo.objects.all()
    for t in tlist:
        dict={'type':t}
        # 查询当前分类最热门的3个商品
        dict['hot']=t.goodsinfo_set.all().order_by('-gclick')[0:3]
        # 查询当前分类最新的4个商品
        dict['new']=GoodsInfo.objects.filter(gtype=t).order_by('-id')[0:4]
        # 将数据构造列表 ,用于传递到模板中
        goods.append(dict)

    context={'isCart':1,'goods':goods}
    return render(request,'tt_goods/index.html',context)

def list(request,tid,pindex,order):
    '''
    模板需要的数据: 分类名称,最新的2个.当前页的数据
    排序:1默认 2价格升序 3价格降序 4最火
    '''
    #指定排序规则
    order_str='-id'
    if order=='2':
        order_str='gprice'
    elif order=='3':
        order_str='-gprice'
    elif order=='4':
        order_str='gclick'
    # 获取分类对象 ,最新的2个
    t=TypeInfo.objects.get(id=tid)
    new=t.goodsinfo_set.all().order_by('-id')[0:2]
    # 当前分类的所有商品
    glist=GoodsInfo.objects.filter(gtype_id=tid).order_by(order_str)


    # 分页
    paginator=Paginator(glist,10)
    # 验证当前页码的合法性
    pindex = int(pindex)
    if pindex <= 1:
        pindex = 1
    if pindex>=paginator.num_pages:
        pindex=paginator.num_pages
    #获取当前页的数据
    page = paginator.page(int(pindex))


    # print(page)
    # print(paginator)
    # print(glist)
    # print(new)
    #构造页码列表
    if paginator.num_pages<=5:
        #如果不够5页,则返回数据页码数字
        plist=paginator.page_range
    else:
        #如果大于5, 则进行公式运算
        if pindex<=2:
            #特例1 12345
            plist=range(1,6)
        elif pindex>=paginator.num_pages-1:
            #特例2 固定最后5页 n-4,n-3,n-2,n-1,n
            plist=range(paginator.num_pages-4,paginator.num_pages+1)
        else:
            plist=range(pindex-2,pindex+3)

    context = {'title':'商品列表','isCart':1,'t':t,'new':new,'page':page,'order':order,'plist':plist}
    return render(request,'tt_goods/list.html',context)

'''
当前是第8页,则显示为 6 7 8 9 10
当前是第5页,则显示为 3 4 5 6 7
plist=range(page.number-2,page.number+3)
range(2,5)===> 2, 3, 4

特例1: 如果是第1,2 末1,末2 有问题
特例2: 如果不够5页则全显示


'''

def detail(request,gid):
    #根据编号查询商品
    goods=GoodsInfo.objects.filter(id=gid)
    #判断编号是否合法
    if goods:
        goods1=goods[0]
        #更新点击量
        goods1.gclick+=1
        goods1.save()

        # 当前商品对应分类
        gtype=goods1.gtype
        #获取这个分类的最新的两个商品
        new=gtype.goodsinfo_set.all().order_by('-id')[0:2]

        context={'title':'商品详情','isCart':1,'goods':goods1,'new':new}
        response=render(request,'tt_goods/detail.html',context)
        # 记录最近浏览
        '''
        先读取原来写好的商品编号,在这个基础上添加上最新的
        最多存储5个最近浏览,所以结构为列表
        注意:cookie中只能存字符串,所以需要将列表与字符串相互转换
        '''
        #读取浏览器中已经浏览过的商品编号
        zjll_str=request.COOKIES.get('zjll','')
        print('=================%s' %zjll_str)
        #cookie中只能存字符串,先转换成列表在进行添加
        zjll_list=zjll_str.split(',')
        print(zjll_list)
        #如果当前编号已经存在则删除
        if gid in zjll_list:
            zjll_list.remove(gid)
        zjll_list.insert(0,gid)
        #如果当前个数超过5个则删除最后一个
        if len(zjll_list)>5:
            zjll_list.pop()
        zjll_str=','.join(zjll_list)
        print(type(zjll_str))


        response.set_cookie('zjll',zjll_str)
        # response.set_cookie('zjll',gid)

        return response
    else:
        return render(request,'404.html')

from haystack.generic_views import SearchView

class MySearchView(SearchView):
    """My custom search view."""


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['isLeft']=2
        context['isCart']=1
        return context