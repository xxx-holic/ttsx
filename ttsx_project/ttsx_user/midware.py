# 记录当前地址,登录成功后转回这个地址
class LoginUrlMiddleware:
    def process_view(self,request,view_fun,view_args,view_kwargs):
        urls=['/user/register/',
              '/user/register_handle/',
              '/user/register_uname/',
              '/user/active/',
              '/user/login/',
              '/user/login_handle/',
              '/user/logout/',
              '/user/sheng/',
              '/cart/add/',
              '/user/pwd_handle/',
              '/user/pwd/'

              ]
        if request.path not in urls:
            request.session['url']=request.get_full_path()
'''
    url('^register/$', views.register),
    url('^register_handle/$', views.register_handle),
    url('^register_uname/$', views.regiester_uname),
    url(r'^active/$', views.active),
    url('^login/$', views.login),
    url('^login_handle/$', views.login_handle),
    url('^info/$', views.info),
    url('^site/$', views.site),
    url('^site_add/$', views.site_add),
    url('^sheng/$', views.sheng),
    url('^logout/$', views.logout),
'''