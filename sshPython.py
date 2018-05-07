## script to execute bash on a remote vm

from pexpect import pxssh
s = pxssh.pxssh()
if not s.login ('10.244.102.57', 'vmuser', 'vmuser'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    s.sendline ('pyhton hello.py')
    s.prompt()         # match the prompt
    print s.before     # print everything before the prompt.
    s.logout()
