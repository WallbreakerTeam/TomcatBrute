必备材料：
Burpsuite<br />
TomcatBrute.py<br />
jython-standalone-2.7-b1.jar<br />
https://repo1.maven.org/maven2/org/python/jython-standalone/2.7-b1/jython-standalone-2.7-b1.jar<br />
步骤：<br />
①	打开burpsuite，进入Extender选项卡，点击子选项卡Options，添加jython-standalone-2.7-b1.jar到Python Environment。<br />
 
②	打开子选项卡Extensions，点击Add添加一个插件。<br />
 
③打开TomcatBrute选项卡，输入目标网址，添加字典，点击开始。<br />
 
④进入Extender选项卡，打开子选项卡Extensions，查看Output。<br />
 
不足：<br />
①	只能暴力破解7.0以下版本。<br />
②	在运行时不能进行其他操作。<br />
改善：<br />
①解决开始爆破线程会卡住的问题。<br />
②可以输入用户名和密码。<br />
③解决在当前选项页面的输出。<br />
