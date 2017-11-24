from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Sum
from .models import CartInfo
from ttsx_user.user_decorators import islogin
# Create your views here.

@islogin
def add(request):
    ok=2
    msg=''
    #从登录状态中获取用户编号
    uid=request.session.get('uid')
    #接收请求的数据
    dict=request.POST
    gid=int(dict.get('gid'))
    nums=int(dict.get('nums'))

    # 查询用户uid是否购买过商品gid
    carts=CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if carts:
        #如果购买过 则增加数量

        print(carts[0])
        cart=carts[0]

        cart.nums+=nums
        if cart.nums>=5:
            cart.nums=5
            msg='单个账号限购5件'
    else:
        # 没用购买过

    # 构造购物车对象
        cart=CartInfo()
        cart.goods_id=gid
        cart.user_id=uid
        cart.nums=nums


    try:
        cart.save()
        ok=1
    except:
        ok=2
    # 查询当前用户购物车总数量
    cart_sum=CartInfo.objects.filter(user_id=uid).aggregate(Sum('nums'))
    # 聚合函数返回一个字典
    count=cart_sum.get('nums__sum')
    # return redirect('/cart/')
    return JsonResponse({'ok':ok,'msg':msg,'count':count})

@islogin
def index(request):
    uid=request.session.get('uid')
    #查询当前用户的购物车信息
    carts=CartInfo.objects.filter(user_id=uid)

    context={'title':'购物车','carts':carts}
    return render(request,'tt_cart/index.html',context)

@islogin
def delete(request):
    cid=request.POST.get('cid')
    cart=CartInfo.objects.get(id=cid)
    cart.delete()
    return JsonResponse({'ok':1})

@islogin
def set(request):
    # 接收购物车编号 数量
    dict=request.POST
    cid=int(dict.get('cid'))
    num=int(dict.get('num'))
    # 查询购物车对象 ,并修改数量
    cart=CartInfo.objects.get(id=cid)
    cart.nums=num
    cart.save()

    return JsonResponse({'ok':1})