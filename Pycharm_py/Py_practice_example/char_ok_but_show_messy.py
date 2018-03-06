#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
[Function]
【整理】Python中实际上已经得到了正确的Unicode或某种编码的字符，但是看起来或打印出来却是乱码
http://www.crifan.com/python_already_got_correct_encoding_string_but_seems_print_messy_code

[Date]
2013-07-19 

[Author]
Crifan Li

[Contact]
http://www.crifan.com/about/me/
-------------------------------------------------------------------------------
"""
 
#---------------------------------import---------------------------------------

#------------------------------------------------------------------------------
def char_ok_but_show_messy():
    """
        Demo Python already got normal chinese char, with some encoding, but print to windows cmd show messy code
    """
    #此处，当前Python文件是UTF-8编码的，所以如下的字符串，是UTf-8编码的
    cnUtf8Char = "我是UTF-8的中文字符串";
    #所以，将UTF-8编码的字符串，打印输出到GBK编码的命令行（Windows的cmd）中，就会显示出乱码
    print  "cnUtf8Char=",cnUtf8Char; #cnUtf8Char= 鎴戞槸UTF-8鐨勪腑鏂囧瓧绗︿覆
    #如果想要正确显示出中文字符，不显示乱码的话，则有两种选择：
    #1. 把字符串转换为Unicode编码，则输出到GBK的命令行时，Python会自动将Unicode的字符串，编码为GBK，然后正确显示字符
    decodedUnicodeChar = cnUtf8Char.decode("UTF-8");
    print "decodedUnicodeChar=",decodedUnicodeChar; #decodedUnicodeChar= 我是UTF-8的中文字符串
    #2. 让字符串的编码和输入目标（windows的cmd）的编码一致：把当前的字符串(由上述解码后得到的Unicode再次去编码)也变成GBK，然后输出到GBK的命令行时，就可以正确显示了
    reEncodedToGbkChar = decodedUnicodeChar.encode("GBK");
    print "reEncodedToGbkChar=",reEncodedToGbkChar; #reEncodedToGbkChar= 我是UTF-8的中文字符串
   

###############################################################################
if __name__=="__main__":
    char_ok_but_show_messy();