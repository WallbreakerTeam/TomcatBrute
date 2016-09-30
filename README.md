破壁者·Tomcat爆破<br/>
小O是个菜鸟，他，不懂什么是注入原理，不懂漏洞挖掘。他是刚接触“黑客”技术的纯种菜鸟，他是一个只会使用工具的“脚本小子”。

他每天不亦乐乎的看着别人黑站，看着“前辈”们炫耀着今天黑了这个站，黑了那个站，感觉很是佩服，很好奇他们是如何做到的。于是也模仿前辈去黑站，不懂的时候就去问“前辈”，虽然有的前辈不搭理他，但他还是乐此不疲，向每一个他认为是高手的“前辈”请教。慢慢的他学会了通过关键字查找注入的方法，也了解了一些SQL注入的工具，如很古老的啊D、pangolin、havij，到sqlmap注入神器。为什么说sqlmap是注入神器呢？只因大部分的注入漏洞sqlmap能检测出来，其他注入工具却不能检测出来。

小O最近遇到一个问题，他碰见了一个网站不知如何下手，只知道是Tomcat网站，但他喜欢叫做“汤姆猫”，他用sqlmap跑了一下没找到注入，只能留在汤姆猫网站主页那里，有一些说明文档，但他不知道如何入手。于是，他找到最近认识的一个对他态度还不错的“前辈”L。

小O：“L前辈，我最近遇到一个汤姆猫的网站，不知该如何下手，能请教下你吗？”

L：“小O你可以通过汤姆猫的管理页面部署war包webshell。”

小O：“那我怎么进入汤姆猫的管理页面呢？”

L：“你可以点击页面Manager App按钮或访问链接加/manager/html进入管理页面。”

小O：“L前辈，它需要密码怎么办？”

L：“你可以尝试通过一些常用的帐号进行猜解，看看能不能进入。”

小O：“有没有什么工具可以批量进行猜解？”

L：“破壁者那个burpsuite插件不错，我拷给你吧”

小O接过前辈递过来的U盘，疑惑的问道：“破壁者？”

这个时候，小O捕捉到前辈若有所思中坚定的眼神。

“那年秋天”，L前辈缓缓道来，好像将要对他诉说一个内心深处的秘密：“我参加了一场叫做《破壁计划》的沙龙，这场沙龙深深的改变了我的人生”。

——“喵！”

突然不知从哪里窜出一只猫，打翻了我们旁边的果盘，L前辈脸色突然变得阴沉，欲言又止。我们两人尴尬的沉默了几秒，他话题一转：

L：“好了，拿去用吧”，抬起眼看了看小O，“不过tomcat管理密码猜解只能是6.0及以下的，7.0及更高做了相关防爆破所以爆破不了！”

小O：“好的，谢谢前辈。”

小O拿到L给的工具，并根据L的指点，很快就安装好这个插件。小O有个习惯，就是喜欢做笔记，于是记录下了他安装插件的过程：

必备材料：

Burpsuite

TomcatBrute.py（L给的插件）

jython-standalone-2.7-b1.jar（插件使用python写的，要在burpsuite使用需要jython环境）

https://repo1.maven.org/maven2/org/python/jython-standalone/2.7-b1/jython-standalone-2.7-b1.jar

步骤：<br/>
①打开burpsuite，进入Extender选项卡，点击子选项卡Options，添加jython-standalone-2.7-b1.jar到Python Environment。<br/>
<img  src="http://www.whitecell-club.org/wp-content/uploads/2016/09/1.jpg" alt="1" width="842" height="563"><br/>
②打开子选项卡Extensions，点击Add添加一个插件。<br/>
<img  src="http://www.whitecell-club.org/wp-content/uploads/2016/09/2.jpg" alt="2" width="700" height="258"><br/>
③打开TomcatBrute选项卡，输入目标网址，添加字典，点击开始。<br/>
<img src="http://www.whitecell-club.org/wp-content/uploads/2016/09/3.jpg" alt="3" width="763" height="341"><br/>
④进入Extender选项卡，打开子选项卡Extensions，查看Output。<br/>
<img src="http://www.whitecell-club.org/wp-content/uploads/2016/09/4.jpg" alt="4" width="683" height="690"><br/>
小O使用这个插件成功的爆破了tomcat登陆验证，但也在使用中发现了这个插件的一些不足：<br/>

①只能爆破7.0以下版本的汤姆猫。<br/>

②在运行时会卡住主进程。<br/>

③字典不能过大，否则会失灵。<br/>

 

小O打电话给L前辈，把自己成功的喜悦和发现的问题都告诉了前辈，并且想要趁热打铁，拿到快速成长的秘诀。电话那头的L前辈告诉他，凡事要循序渐进、稳扎稳打，切不可急躁，并向他推荐了《WhiteCellClub团队技能树》，这时小O突然听到电话那头传来一阵嘈杂。

——前辈？前辈？

——…….
