---
title: "ssh tutorial"
date: 2021-04-07T01:17:24
Description: ""
Tags: []
Categories: []
DisableComments: false
---
### [ssh.com](https://www.ssh.com/ssh/copy-id)
### [ssh-copy-id](https://www.ssh.com/ssh/copy-id)

###  Generate an SSH Key
```bash
# ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ylo/.ssh/id_rsa): mykey
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in mykey.
Your public key has been saved in mykey.pub.
The key fingerprint is:
SHA256:GKW7yzA1J1qkr1Cr9MhUwAbHbF2NrIPEgZXeOUOz3Us ylo@klar
The key's randomart image is:
+---[RSA 2048]----+
|.*++ o.o.        |
|.+B + oo.        |
| +++ *+.         |
| .o.Oo.+E        |
|    ++B.S.       |
|   o * =.        |
|  + = o          |
| + = = .         |
|  + o o          |
+----[SHA256]-----+
#
```
Creating a key pair (public key and private key) only takes a minute. The key files are usually stored in the `~/.ssh` directory.
### Copy the key to a server
```bash
ssh-copy-id -i ~/.ssh/mykey user@host
```
This logs into the server host, and copies keys to the server, and configures them to grant access by adding them to the [authorized_keys](https://www.ssh.com/ssh/authorized_keys) file. The copying may ask for a password or other authentication for the server.
 
### Test the new key
```
ssh -i ~/.ssh/mykey user@host
```
The login should now complete without asking for a password. Note, however, that the command might ask for the passphrase you specified for the key.
### Troubleshooting

There are a number of reasons why the test might fail:

-   The server might not be configured to accept public key authentication. Make sure  [/etc/ssh/sshd_config](https://www.ssh.com/ssh/sshd_config)  on the server contains  `PubkeyAuthentication yes`. Remember to restart the  [sshd](https://www.ssh.com/ssh/sshd/)  process on the server.
    
-   If trying to login as  [root](https://www.ssh.com/iam/user/root), the server might not be configured to allow root logins. Make sure  `/etc/sshd_config`  includes  `PermitRootLogin yes`,  `PermitRootLogin prohibit-password`, or  `without-password`. If it is set to  `forced-commands-only`, the key must be manually configured to use a forced command (see  `command=`  option in  `~/.ssh/authorized_keys`.
    
-   Make sure the client allows public key authentication. Check that  [/etc/ssh/config](https://www.ssh.com/ssh/config)  includes  `PubkeyAuthentication yes`.
    
-   Try adding  `-v`  option to the  `ssh`  command used for the test. Read the output to see what it says about whether the key is tried and what authentication methods the server is willing to accept.
    
-   OpenSSH only allows a maximum of five keys to be tried authomatically. If you have more keys, you must specify which key to use using the  `-i`  option to  `ssh`.
## How ssh-copy-id works
`ssh-copy-id`  uses the  [SSH protocol](https://www.ssh.com/ssh/protocol/)  to connect to the target host and upload the SSH user key. The command edits the  `authorized_keys`  file on the server. It creates the  `.ssh`  directory if it doesn't exist. It creates the authorized keys file if it doesn't exist. Effectively, ssh key copied to server.

It also checks if the key already exists on the server. Unless the  `-f`  option is given, each key is only added to the authorized keys file once.

It further ensures that the key files have appropriate permissions. Generally, the user's home directory or any file or directory containing keys files should not be writable by anyone else. Otherwise someone else could add new authorized keys for the user and gain access. Private key files should not be readable by anyone else.
## Some best practices for SSH keys

SSH keys are very useful, but can lead to problems if they are not properly managed. They are access credentials just like user names and passwords. If they are not properly removed when people leave or systems are decommissioned, no-one may any longer know who really has access to which systems and data. Many large organizations have ended up having millions of SSH keys.
### Use a passphrase when possible

It is recommended that keys used for single sign-on have a passphrase to prevent use of the key if it is stolen or inadvertatly leaked. The  [ssh-agent](https://www.ssh.com/ssh/agent)  and  [ssh-add](https://www.ssh.com/ssh/add)  programs can be used to avoid having to enter the passphrase every time the key is used.

Generally all keys used for interactive access should have a passphrase. Keys without a passphrase are useful for fully automated processes. They allow shell scripts, programs, and management tools to log into servers unattended. This is often used for backups and data transfers between information systems.

### Add a command restriction when possible

The  `copy-id`  tool does not automatically add command restrictions to keys. Using command restrictions is highly recommended when the key is used for automating operations, such as running a report for fetching some files. A command restriction is basically a  `command="<permitted command>"`  option added to the beginning of the line in the server's  [authorized_keys](https://www.ssh.com/ssh/authorized_keys/)  file.

### Managing SSH keys

Anyone having more than a few dozen servers is strongly recommended to  [manage SSH keys](https://www.ssh.com/iam/ssh-key-management). Not managing the keys exposes the organization to substantial risks, including loss of confidentiality, insertion of fraudulent transactions, and outright destruction of systems.

The  `copy-id`  tool can be dangerous. It can easily accidentally install multiple keys or unintended keys as authorized. The logic for choosing which key to install is convoluted. Extra authorized keys grant permanent access. They can later be used to spread attacks host-to-host, and the more keys there are, the higher the risk. It also violates all  [regulatory compliance requirements](https://www.ssh.com/compliance/).

The  [Universal SSH Key Manager](https://www.ssh.com/products/universal-ssh-key-manager)  is a widely used product for managing SSH keys.

