#coding=utf-8
#python version:2.7
import urllib2  
import urllib  

class Loginer():  
    def __init__(self, username, password):  
        self.loginUrl = 'http://202.118.1.87/srun_portal_pc.php?ac_id=1&'  
        self.username = username  
        self.password = password  
        self.openner = urllib2.build_opener()  

    def login(self):  
        postdata = {  
            'username': self.username,  
            'password': self.password,  
            'action': 'login',  
            'ac_id': '1',
            'user_ip':'',
            'nas_ip':'',
            'user_mac':'',
            'url':''  
        }  
        postdata = urllib.urlencode(postdata)  
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)  

        result = self.openner.open(myRequest).read()
        resStr=str(result)
        with open('t.ttt','w') as t:
            t.write(resStr)
        # resStr.encode('gbk')
        resStr = unicode(resStr,'utf-8')
        print resStr
        ind=resStr.find(u'网络已连接') 
        if(ind!=-1):
            print 'connected successfully' 
        else:
            print 'connected faild!! Maybe your username or password is wrong!'

def main():  
    username=raw_input('Enter your username:')
    password=raw_input('Enter your password:')
    file=open('d:/temp_username.dat','w')
    file.write(username)
    file.close()
    l = Loginer(username,password)
    l.login()  


if __name__ == '__main__':  
    main()  
    print 'done'
