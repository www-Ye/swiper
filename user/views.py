from django.shortcuts import render

# Create your views here.
def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')

def login(request):
    '''短信验证登录'''
    pass

def get_profile(request):
    '''获取个人资料'''
    pass

def modify_profile(request):
    '''修改个人资料'''
    pass

def upload_avatar(request):
    '''头像上传'''
    pass