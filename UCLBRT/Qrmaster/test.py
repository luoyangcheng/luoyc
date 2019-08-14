from bs4 import BeautifulSoup
import urllib.request
import re


#如果是网址，可以用这个办法来读取网页
#html_doc = "http://tieba.baidu.com/p/2460150866"
#req = urllib.request.Request(html_doc)
#webpage = urllib.request.urlopen(req)
#html = webpage.read()



html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="xiaodeng"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<a href="http://example.com/lacie" class="sister" id="xiaodeng">Lacie</a>
and they lived at the bottom of a well.</p>
<div class="ntopbar_loading"><img src="http://simg.sinajs.cn/blog7style/images/common/loading.gif">加载中…</div>

<div class="SG_connHead">
            <span class="title" comp_title="个人资料">个人资料</span>
            <span class="edit">
                        </span>
<div class="info_list">     
                                   <ul class="info_list1">
                    <li><span class="SG_txtc">博客等级：</span><span id="comp_901_grade"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src="http://simg.sinajs.cn/blog7style/images/common/number/9.gif"  /></span></li>
                    <li><span class="SG_txtc">博客积分：</span><span id="comp_901_score"><strong>0</strong></span></li>
                    </ul>
                    <ul class="info_list2">
                    <li><span class="SG_txtc">博客访问：</span><span id="comp_901_pv"><strong>3,971</strong></span></li>
                    <li><span class="SG_txtc">关注人气：</span><span id="comp_901_attention"><strong>0</strong></span></li>
                    <li><span class="SG_txtc">获赠金笔：</span><strong id="comp_901_d_goldpen">0支</strong></li>
                    <li><span class="SG_txtc">赠出金笔：</span><strong id="comp_901_r_goldpen">0支</strong></li>
                    <li class="lisp" id="comp_901_badge"><span class="SG_txtc">荣誉徽章：</span></li>
                    </ul>
                  </div>
<div class="atcTit_more"><span class="SG_more"><a href="http://blog.sina.com.cn/" target="_blank">更多&gt;&gt;</a></span></div>                 
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'html.parser')   #文档对象



# 类名为xxx而且文本内容为hahaha的div
for k in soup.find_all('div',class_='atcTit_more'):#,string='更多'
    print(k)
    #<div class="atcTit_more"><span class="SG_more"><a href="http://blog.sina.com.cn/" target="_blank">更多&gt;&gt;</a></span></div>