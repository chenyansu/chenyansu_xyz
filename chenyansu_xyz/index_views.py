#coding:utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
    # return render(request, 'index.html')
    return HttpResponse("""
    <style type="text/css">
        #ICP {
            width:100%; 
            height:60px; 
            line-height:10px; 
            background:#ccc; 
            position:fixed; 
            bottom:0px; 
            left:0px; 
            font-size:14px; 
            color:#000; 
            text-align:center;
            }
    </style>

    <div id="ICP">
        <p>Copyright © 2018 Powered by 陈严肃 All Rights Reserved.</p>
        <a href="http://www.miitbeian.gov.cn/" rel="nofollow" target="_blank">吉ICP备18001719号</a>
    </div>
    """)