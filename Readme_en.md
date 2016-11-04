<h1>WallbreakerTeam·TomcatBrute</h1><br/>

必备材料：

Burpsuite

TomcatBrute.py

jython-standalone-2.7-b1.jar

https://repo1.maven.org/maven2/org/python/jython-standalone/2.7-b1/jython-standalone-2.7-b1.jar

Step:<br/>
①Open burpsuite,Click the 'Extender' tab，Click the Sub Tab 'Options',Add jython-standalone-2.7-b1.jar to Python Environment.<br/>
<img  src="http://www.whitecell-club.org/wp-content/uploads/2016/09/1.jpg" alt="1" width="842" height="563"><br/>
②Open Sub Tab 'Extensions',Click the 'Add' button to add the plugin.<br/>
<img  src="http://www.whitecell-club.org/wp-content/uploads/2016/09/2.jpg" alt="2" width="700" height="258"><br/>
③Open TomcatBrute Tab,Enter destination URL,Add dist,Click the 'start' button.<br/>
<img src="http://www.whitecell-club.org/wp-content/uploads/2016/09/3.jpg" alt="3" width="763" height="341"><br/>
④Open Extender Tab,Open Sub Tab 'Extensions',view 'output' Tab.<br/>
<img src="http://www.whitecell-club.org/wp-content/uploads/2016/09/4.jpg" alt="4" width="683" height="690"><br/>

Plug in deficiency:<br/>

①Tomcat version order 7.0 .<br/>

②Stuck in the main process at run time.<br/>

③Dictionary cannot be too big,otherwise it will fail.<br/>
