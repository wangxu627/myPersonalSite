---
title: "How to ignore invalid and self signed ssl connection errors with curl"
date: 2020-10-20T11:05:02+08:00
Description: ""
Tags: []
Categories: []
DisableComments: false
---

> Wanted to curl command to ignore SSL certification warning. (Does curl command have a --no-check-certificate option like wget command)[https://www.cyberciti.biz/faq/wget-example-download-from-https-web-sites/] on Linux or Unix-like system?  
[![](https://www.cyberciti.biz/media/new/category/old/terminal.png)](http://google.com.au/)


You need to pass the `-k` or `--insecure` option to the curl command. This option explicitly allows curl to perform “insecure” SSL connections and transfers. All SSL connections are attempted to be made secure by using the CA certificate bundle installed by default.

---
# Does curl have a –no-check-certificate option like wget command on Linux?

The syntax is as follows that allows curl command to work with “insecure” or “invalid” SSL certificates without https certicates:

```
curl -k url
curl --insecure url
curl --insecure [options] url
curl --insecure -I url
```
## cURL ignore SSL certificate warnings command

In this example disable certificate verification for curl command:
```
curl --insecure -I https://202.54.1.2/
```
OR
```
curl -k -O https://202.54.1.2/file.tar.gz
```
Without the `-k` or `--insecure` option, you will get an error message that read as follows:
```
curl: (60) SSL certificate problem: Invalid certificate chain
More details here: https://curl.haxx.se/docs/sslcerts.html

curl performs SSL certificate verification by default, using a "bundle"
 of Certificate Authority (CA) public keys (CA certs). If the default
 bundle file isn't adequate, you can specify an alternate file
 using the --cacert option.
If this HTTPS server uses a certificate signed by a CA represented in
 the bundle, the certificate verification probably failed due to a
 problem with the certificate (it might be expired, or the name might
 not match the domain name in the URL).
If you'd like to turn off curl's verification of the certificate, use
 the -k (or --insecure) option.
```

Here is one useful example where you want to grab a file or see header info from remote host without using SSL enabled SNI domain name:
```
curl -O --insecure --header 'Host: www.example.com' -I https://207.5.1.10/file.html
### OR ###
curl -k --header 'Host: www.example.com' -I https://207.5.1.10/file.html
```

Sample outputs:
![](https://www.cyberciti.biz/media/new/faq/2017/01/curl-ignore-ssl-certificate-warning.jpg)