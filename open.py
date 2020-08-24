#file1 = open('/Users/qi/Desktop/test/abc.txt','r',encoding='utf-8')
#filecontent = file1.read()   
#print(filecontent)
#file1.close()  
file1 = open('/Users/qi/Desktop/test/abc.txt', 'a',encoding='utf-8') 
#以追加的方式打开文件abc.txt
file1.write('张无忌\n')     
#把字符串'张无忌'写入文件file1
file1.write('宋青书\n')     
#把字符串'宋青书'写入文件file1
file1.close()