__author__ = 'I322233'
import sys,urllib
url = "http://aliyuntianchiresult.cn-hangzhou.oss.aliyun-inc.com/file/race/documents/231506/test_items.txt?Expires=1442912629&OSSAccessKeyId=2zep9f8tkzg6ennfl26ciifi&Signature=GJDcpYjj%2BXFs38cgnIeFEMCFeg4%3D"
wp = urllib.urlopen(url)
content = wp.read()
f = open("test_items.txt",'w')
f.write(content)
f.close()
print (content)
