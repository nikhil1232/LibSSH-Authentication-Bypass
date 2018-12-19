# LibSSH-Authentication-Bypass
LibSSH Authentication Bypass CVE-2018-10933

### Usage:                                                                                                                                     

To use this script type in: python3 LibAuth.py –help to see all the options and parameters we need to use.

So we need to specify the victim’s IP address, port no and finally the command that we want to execute in the victim machine.

The Final command would be 
### python3 LibAuth.py –host 192.168.0.100 -p 22 -c “uname -a”

![alt text](https://theblocksec.com/wp/wp-content/uploads/2018/12/Screenshot-216.png)

## References:
https://pentesterlab.com/exercises/cve-2018-10933/course

https://github.com/kn6869610/CVE-2018-10933

https://www.youtube.com/watch?v=ZSWQjmfcn4g

http://docs.paramiko.org
