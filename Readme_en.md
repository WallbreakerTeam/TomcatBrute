<h1>破壁者·Tomcat爆破</h1><br/>

必备材料：

Burpsuite

TomcatBrute.py

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

插件的一些不足：<br/>

①只能爆破7.0以下版本的汤姆猫。<br/>

②在运行时会卡住主进程。<br/>

③字典不能过大，否则会失灵。<br/>
