
---
title: How to mount remote directory on Windows using SSHFS-Win
date: 2019-12-11 01:12:32.699566
Description: ""
Tags: []
Categories: []
DisableComments: false
---
<https://codeyarns.com/2018/05/03/how-to-mount-remote-directory-on-windows-
using-sshfs-win/>

  

[ **sshfs**](https://codeyarns.com/2014/09/10/how-to-mount-remote-directory-
using-sshfs/) makes it convenient to mount a directory from a remote Linux
computer on a local Linux computer. [ **SSHFS-
Win**](https://github.com/billziss-gh/sshfs-win) makes it easy to mount a
directory from a remote Linux computer on your local Windows computer.

  * Install the latest stable installer of  **WinFSP**  from [here](https://github.com/billziss-gh/winfsp/releases).

  * Install the latest stable installer of SSHFS-Win from [here](https://github.com/billziss-gh/sshfs-win/releases).

  * Open  **File Explorer** , right-click on  **This PC**  and choose  **Map network drive**. Choose a drive to mount at and in the  **Folder**  field enter:

1

|

`\\sshfs\yourRemoteLogin@remoteComputer`  
  
---|---  
  
By default, Windows will use your Windows password or credentials for the
remote computer. If the password or credentials are different on the remote
computer then choose the  **Connect using different credentials**  option.

Windows will ask for your password at the remote computer. After that the home
directory from your remote computer will be mounted at the Windows drive you
chose. I found that I had full read-write access to the files mounted from
remote.

 **Tried with:**  SSHFS-Win 2.7.17334 and WinFSP 1.2.17346  


