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
        #index_link {
            text-align:center;
            margin-left: auto;
            margin-right: auto;
        }
        #baidu {
            width: 800px;
            position: absolute;
            top: 305px;
            left: 50%;
            margin-left: -160px;
            height: 158px;
            padding: 25px;

        }
        
    </style>

    <div id="ICP">
        <p>Copyright © 2018 Powered by 陈严肃 All Rights Reserved.</p>
        <a href="http://www.miitbeian.gov.cn/" rel="nofollow" target="_blank">吉ICP备18001719号</a>
    </div>
    <div id="index_link">
        <a href="blog">BLOG</a>
	<a href="http://www.chenyansu.xyz:8848/nextcloud"> NEXTCLOUD </a>
        <a href="admin"> 后台 </a>
    </div>
    <div id="baidu">
     <form action="http://www.baidu.com/baidu" target="_blank">
        <table bgcolor="#FFFFFF"><tr><td>
            <input name=tn type=hidden value=baidu>
            <a href="http://www.baidu.com/"></a>
            <input type=text name=word size=30>
            <input type="submit" value="百度搜索">
            </td></tr>
        </table>
    </form> 
    
    </div>
    

    """)
