import os

passwd = 'yc123'
cmd = 'ls -al'
cmd = 'pwd'

os.system(cmd)

#1. pull github and merge new change
cmd = 'git pull origin master'
os.system(cmd)

#2. auto build to create new static html
cmd = ('mkdocs build')
os.system(cmd)

#3. copy /site to /tomcat/webapp
cmd = ('sudo cp -fr site/ /opt/tomcat/apache-tomcat-9.0.21/webapps/')
os.system('echo %s|sudo -S %s' % (passwd, cmd))
