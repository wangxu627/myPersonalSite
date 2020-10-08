
---
title:  C语言实现Base64编码/解码
date: 2019-11-21 13:42:44.831096
Description: ""
Tags: []
Categories: []
DisableComments: false
---
Bse64是一种以64个可打印字符对二进制数据进行编码的编码算法。base64在对数据进行编码时以三个8位字符型数据为一组，取这三个字符型数据的ASCII码，然后以6位为一组组成4个新的数据，这4个新的数据有6位，所以它的最大值为2^6=64。我们以4个6位数据的十进制数从base64表中得到最终编码后的字符。

Base64 编码表

Value| Char | Value| Char | Value| Char | Value| Char  
---|---|---|---|---|---|---|---  
0| A| 16| Q| 32| g| 48| w  
1| B| 17| R| 33| h| 49| x  
2| C| 18| S| 34| i| 50| y  
3| D| 19| T| 35| j| 51| z  
4| E| 20| U| 36| k| 52| 0  
5| F| 21| V| 37| l| 53| 1  
6| G| 22| W| 38| m| 54| 2  
7| H| 23| X| 39| n| 55| 3  
8| I| 24| Y| 40| o| 56| 4  
9| J| 25| Z| 41| p| 57| 5  
10| K| 26| a| 42| q| 58| 6  
11| L| 27| b| 43| r| 59| 7  
12| M| 28| c| 44| s| 60| 8  
13| N| 29| d| 45| t| 61| 9  
14| O| 30| e| 46| u| 62| +  
15| P| 31| f| 47| v| 63| /  
  


       由于base64编码是将编码前的3*8位数据，分解成4个6位的数据，所以经过base64编码后的字符串长度是4的倍数。但往往我们进行编码的数据长度并不是3的倍数，这就造成了“编码”后的位数不为4的倍数，比如Brisk共5×8=40位，以6位为一组可以分为7组，这样“编码”后就有7个字符，但base64编码后的字符长度应该是4的倍数，显然这里就出问题了，那么怎么办呢？前面的不可以抛弃掉，所以就只有“追加”了，所以Brisk经过base64编码后的长度应该是8个字符，而第8个编码后的字符是'='，再比如对单个字符a进行base64编码，由于它的长度不是3的倍数，以3个字节为一组它只能分一组，再以6位为一位它只能分两组，所以经过“编码”后它的长度是2，但base64编码后的个数应该是4的倍数，所以它的长度应该是4，所以在后面补上两个‘=’,由于一个数求余3后有三个不同的结果，0、1、2，所以在对一个数据进行base64进行编码后它的长度为：



（1）当进行编码的数据长度是3的倍数时，len=strlen(str_in)/3*4;  
（2）当进行编码的数据长度不是3的倍数时，len=(strlen(str_in)/3+1)*4;

       我们以Brisk这个例子来说明一下base64编码的过程。首先我们以3个字符为一组将Brisk进行分组，Brisk被氛围两组：Bri 和 sk；然后我们取出这两个分组中每个字节的ASCII码，B:66 r:114 i:105 s:115 k:107。它们对应的二进制数为  B:01000010 r:01110010 i:01101001 s:01110011 k:01101011；

       第一组，我们以6位为一组对每一个3字节分组进行再分组就变成了010000 100111 001001 101001。所对应的十进制数是16 39 9 41，对应base64表中的结果是 Q n J p；

       第二组，011100 110110 101100(不够补0)，所以对应的十进制数是 28 54 44，对应base64表中的结果是 c 2 s，最终结果为QnJpc2s=（因为第二组“编码”后只有三个字节）。

      解码的过程是一个逆过程，我们将经过编码后的字符按4个字符为一组，然后对照base64表得到相应的十进制数，再将其通过拆分和组合，组成3个8位数据，这个数据就是解码后的数据，下面给一个c语言实现编码和解码的代码。



    
          1. /*base64.h*/  
    
      2. #ifndef _BASE64_H  
    
      3. #define _BASE64_H  
    
      4.   
    
      5. #include <stdlib.h>  
    
      6. #include <string.h>  
    
      7.   
    
      8. unsigned char *base64_encode(unsigned char *str);  
    
      9.   
    
      10. unsigned char *bae64_decode(unsigned char *code);  
    
      11.   
    
      12. #endif  
    
    
    







    
          1. /*base64.c*/  
    
      2. #include "base64.h"  
    
      3.   
    
      4. unsigned char *base64_encode(unsigned char *str)  
    
      5. {  
    
      6.     long len;  
    
      7.     long str_len;  
    
      8.     unsigned char *res;  
    
      9.     int i,j;  
    
      10. //定义base64编码表  
    
      11.     unsigned char *base64_table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";  
    
      12.   
    
      13. //计算经过base64编码后的字符串长度  
    
      14.     str_len=strlen(str);  
    
      15.     if(str_len % 3 == 0)  
    
      16.         len=str_len/3*4;  
    
      17.     else  
    
      18.         len=(str_len/3+1)*4;  
    
      19.   
    
      20.     res=malloc(sizeof(unsigned char)*len+1);  
    
      21.     res[len]='\0';  
    
      22.   
    
      23. //以3个8位字符为一组进行编码  
    
      24.     for(i=0,j=0;i<len-2;j+=3,i+=4)  
    
      25.     {  
    
      26.         res[i]=base64_table[str[j]>>2]; //取出第一个字符的前6位并找出对应的结果字符  
    
      27.         res[i+1]=base64_table[(str[j]&0x3)<<4 | (str[j+1]>>4)]; //将第一个字符的后位与第二个字符的前4位进行组合并找到对应的结果字符  
    
      28.         res[i+2]=base64_table[(str[j+1]&0xf)<<2 | (str[j+2]>>6)]; //将第二个字符的后4位与第三个字符的前2位组合并找出对应的结果字符  
    
      29.         res[i+3]=base64_table[str[j+2]&0x3f]; //取出第三个字符的后6位并找出结果字符  
    
      30.     }  
    
      31.   
    
      32.     switch(str_len % 3)  
    
      33.     {  
    
      34.         case 1:  
    
      35.             res[i-2]='=';  
    
      36.             res[i-1]='=';  
    
      37.             break;  
    
      38.         case 2:  
    
      39.             res[i-1]='=';  
    
      40.             break;  
    
      41.     }  
    
      42.   
    
      43.     return res;  
    
      44. }  
    
      45.   
    
      46. unsigned char *base64_decode(unsigned char *code)  
    
      47. {  
    
      48. //根据base64表，以字符找到对应的十进制数据  
    
      49.     int table[]={0,0,0,0,0,0,0,0,0,0,0,0,
    
      50.     		 0,0,0,0,0,0,0,0,0,0,0,0,
    
      51.     		 0,0,0,0,0,0,0,0,0,0,0,0,
    
      52.     		 0,0,0,0,0,0,0,62,0,0,0,
    
      53.     		 63,52,53,54,55,56,57,58,
    
      54.     		 59,60,61,0,0,0,0,0,0,0,0,
    
      55.     		 1,2,3,4,5,6,7,8,9,10,11,12,
    
      56.     		 13,14,15,16,17,18,19,20,21,
    
      57.     		 22,23,24,25,0,0,0,0,0,0,26,
    
      58.     		 27,28,29,30,31,32,33,34,35,
    
      59.     		 36,37,38,39,40,41,42,43,44,
    
      60.     		 45,46,47,48,49,50,51
    
      61.     	       };  
    
      62.     long len;  
    
      63.     long str_len;  
    
      64.     unsigned char *res;  
    
      65.     int i,j;  
    
      66.   
    
      67. //计算解码后的字符串长度  
    
      68.     len=strlen(code);  
    
      69. //判断编码后的字符串后是否有=  
    
      70.     if(strstr(code,"=="))  
    
      71.         str_len=len/4*3-2;  
    
      72.     else if(strstr(code,"="))  
    
      73.         str_len=len/4*3-1;  
    
      74.     else  
    
      75.         str_len=len/4*3;  
    
      76.   
    
      77.     res=malloc(sizeof(unsigned char)*str_len+1);  
    
      78.     res[str_len]='\0';  
    
      79.   
    
      80. //以4个字符为一位进行解码  
    
      81.     for(i=0,j=0;i < len-2;j+=3,i+=4)  
    
      82.     {  
    
      83.         res[j]=((unsigned char)table[code[i]])<<2 | (((unsigned char)table[code[i+1]])>>4); //取出第一个字符对应base64表的十进制数的前6位与第二个字符对应base64表的十进制数的后2位进行组合  
    
      84.         res[j+1]=(((unsigned char)table[code[i+1]])<<4) | (((unsigned char)table[code[i+2]])>>2); //取出第二个字符对应base64表的十进制数的后4位与第三个字符对应bas464表的十进制数的后4位进行组合  
    
      85.         res[j+2]=(((unsigned char)table[code[i+2]])<<6) | ((unsigned char)table[code[i+3]]); //取出第三个字符对应base64表的十进制数的后2位与第4个字符进行组合  
    
      86.     }  
    
      87.   
    
      88.     return res;  
    
      89.   
    
      90. }  
    
    
    



    
          1. /*一个测试程序*/  
    
      2. #include "base64.h"  
    
      3. #include <stdio.h> 
    
      4. #include <string.h>   
    
      5.   
    
      6. int main(int argc,char **argv)  
    
      7. {  
    
      8.     unsigned char *buf =NULL;
    
      9.     if(strcmp(argv[1],"-d") == 0) 
    
      10.     { 
    
      11. 	buf = base64_decode(argv[2]);
    
      12.         printf("%s\n",buf);  
    
      13.     }
    
      14.     else  
    
      15.     {
    
      16. 	buf = base64_encode(argv[1]);
    
      17.         printf("%s\n",buf);   
    
      18.     }
    
      19.  
    
      20.     free(buf);
    
      21.   
    
      22.     return 0;  
    
      23. } 
    
    
    



编译  
gcc -o test test.c base64.c

./test a123456  
YTEyMzQ1Ng==

  
./test -d YTEyMzQ1Ng==  
a123456


