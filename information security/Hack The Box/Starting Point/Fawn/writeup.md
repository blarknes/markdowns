# Fawn

## Information

**Difficulty**: Very Easy  
**Tags**: FTP; Network; Protocols; Reconnaissance; Anonymous/Guest Access.

## Flags

1. What does the 3-letter acronym FTP stand for?
   - File Transfer Protocol
2. Which port does the FTP service listen on usually?
   - 21
3. What acronym is used for the secure version of FTP?
   - SFTP
4. What is the command we can use to send an ICMP echo request to test our connection to the target?
   - ping
5. From your scans, what version is FTP running on the target?
   - vsftpd 3.0.3
6. From your scans, what OS type is running on the target?
   - Unix
7. What is the command we need to run in order to display the 'ftp' client help menu?
   - ftp -h
8. What is username that is used over FTP when you want to log in without having an account?
   - anonymous
9. What is the response code we get for the FTP message 'Login successful'?
   - 230
10. There are a couple of commands we can use to list the files and directories available on the FTP server. One is dir. What is the other that is a common way to list files on a Linux system.
    - ls
11. What is the command used to download the file we found on the FTP server?
    - get

## Solution

"_The key is a strong foundation_"

This machine is made of mainly teorical questions, but when applied in practice, we get to the flag.

Starting with a nmap to see which ports are open on the machine we find out that there's a ftp open on port 21.

```sh
$ nmap $ip

Starting Nmap 7.93 ( https://nmap.org ) at $date
Nmap scan report for $ip
Host is up (0.40s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp
```

With that in mind, let's connect to the ftp.

```sh
$ ftp $ip
Connected to $ip.
220 (vsFTPd 3.0.3)
Name ($ip:kali):
```

The service requires an user to connect, the default user to ftp is **anonymous** and it doesn't have a password, so just press **Enter** when the password is required.

```sh
Name ($ip:kali): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

After we're in, lets recognize the environment.

```sh
ftp> ls
229 Entering Extended Passive Mode (|||41716|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
```

We can't see the contents of the file inside the ftp, so let's download it and see what is the flag.

```sh
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||14944|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
100% |***************************************************************|    32        0.13 KiB/s    00:00 ETA
226 Transfer complete.
32 bytes received in 00:00 (0.04 KiB/s)
```

Let's exit the ftp to be polite.

```sh
ftp> exit
221 Goodbye.
```

Goodbye ftp!

Now with the file downloaded in our machine, the last step is to cat the flag.

```sh
$ ls
Desktop  Documents  Downloads  flag.txt  Music  Pictures  Public  Templates  Videos

$ cat flag.txt
035db21c881520061c53e0536e44f815
```

## Flag

035db21c881520061c53e0536e44f815
