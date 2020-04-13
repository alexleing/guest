from jpype import *
import os.path
import jpype
import time
import unittest
import requests


# startJVM("C:/Program Files/Java/jre1.8.0_171/bin/server/jvm.dll", "-ea")
# java.lang.System.out.println("helloWorld")

# 集享卡的私钥，用来签名加密
privateKey = 'PS9wVMAF4bCcODZd7Cs1eS/kKDUNp/q0INF0k6KygfO+F7CmyRr3mm/K2TQMLpoC05oUfWTRFPl//H7yECQQCWV' \
             '1uS4+tPcYl013hD5gRjJKihRNj+AGoM3q4NH4qOoTA0ssw5+gGuLhHFnxFZxmu4ss6n8Lkg6vwjJNCvd2rjAkBJv' \
             'Ksum26U4P2BKzMe2F5uXIFzQGWB1Wm1DJNK8L0Ut7KbAh+DrJXzo2DUIOL7kaSAkrTFqaF5T0GVmaeBzoZhAkAJfq' \
             'zm4wQaeVYwDeeniiBezpLj1IBL0mTgOTQO2h4bEe0EdwJU6wguIvS2YWxsGg71lD1e9+IJRS31Xj7bxhP3AkBe' \
             'Q/3u2NAnA2Hp7DKbhiSumIwSqFUUr5rhEulHvY62vrFWH8HzvZccY/ymLh+7+xHqhy6msWEplnJFauDc2dEq'
# 集享卡的公钥，用来业务数据data加密
jxcPublicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfDvfIr5IRRCVIudeiKs53O+3cl3s' \
               '2GCBqME2ywF31OhBIW8zC8PMmJkCuZk1Gt+y7IlYk2mPO3QCf7HZz1nd6P2WD869Bh/L6p' \
               '8bN1zVplXleQ+Yqa8s4Bh4/jdLzs2+LBayowvUNju94QoPxo2ylljTez5g1D5wYVTVWZkClWQIDAQAB'

# 调用多个jar包，注意调用几个jar包在jpype.startJVM那里就需要几个%s;
jarpath1 =os.path.join(os.path.abspath('.'), 'D:/apache-jmeter-3.2/lib/ext/commons-codec-1.6.jar')
jarpath2 =os.path.join(os.path.abspath('.'), 'D:/apache-jmeter-3.2/lib/ext/fastjson-1.1.37.jar')
jarpath3 =os.path.join(os.path.abspath('.'), 'D:/apache-jmeter-3.2/lib/ext/Ne_test.jar')
jpype.startJVM("C:/Program Files/Java/jre1.8.0_171/bin/server/jvm.dll", "-ea",
               "-Djava.class.path=%s;%s;%s" % (jarpath3,jarpath1,jarpath2))  # jarpath1, jarpath2,

# data结构中的nonce结构
appId = 'FDA1276694626DA0'
appSecret = 'B8FFCF23FDA1276694626DA0E228C6FA'
timestamp = '20190417120505'
nonce = "appId=" + appId + "&appSecret=" + appSecret + "&timestamp=" + timestamp
print(nonce)

# 调用jar包里面的类
JClass1 = jpype.JClass('org.apache.commons.codec.binary.Base64')
JClass2 = jpype.JClass('com.maxxipoint.test.MaxxipointSecurity')
JClass3 = jpype.JClass('com.maxxipoint.test.MD5')
instance2 = JClass2.encryptMD5(nonce)
instance1 = JClass1.encodeBase64String(instance2)

print(instance1)







shutdownJVM()