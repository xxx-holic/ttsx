from django.shortcuts import redirect
from django.http import JsonResponse

# 判断是否登录
def islogin(view_fun):
    def fun(request,*args,**kwargs):# fun的参数由view_fun的参数决定
        # 判断是否登录,如果未登录转到登录页面
        if 'uid' not in request.session:
            # 判断是否为ajax请求
            if request.is_ajax():
                return JsonResponse({'islogin':1})

            return redirect('/user/login')
        else:
            return view_fun(request,*args,**kwargs)
    return fun

