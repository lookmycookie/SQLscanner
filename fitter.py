#!/usr/bin/env python
# coding :utf8

file = open('bingurls.txt', 'r', encoding='utf-8')
for line in file:
    content = line[0:-1]
    if 'http' in content:
        result_file = open("temp.txt", "a+", encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        result_file.close()
        print(content)
    else:
        content = 'http://' + content
        result_file = open("temp.txt", "a+", encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        result_file.close()
        print(content)
file.close()

file = open('temp.txt', 'r')
# 拼接不合适的url
# 不关闭两次有时候会出现玄学读写错误


a = 0
writeDir = "temp1.txt"
lines_seen = set()
outfile = open(writeDir, "w")
f = open('temp.txt', "r")
for line in f:
    if line not in lines_seen:
        a += 1
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
f.close()
print("success")

# url去重


file = open('temp1.txt', 'r', encoding='utf-8')
for line in file:
    content = line[0:-1]
    if content.endswith('html'):
        continue
    if content.endswith('htm'):
        continue
    if "https://wappass.baidu.com/static/" in content:
        print("检测到百度拦截，已跳过")
        continue
    if ".php?" in content:
        result_file = open('phppoint.txt', 'a+', encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        print(content)
    if ".asp?" in content:
        result_file = open('asppoint.txt', 'a+', encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        print(content)
    if "gov" in content:
        result_file = open('highvalue/gov.txt', 'a+', encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()
        print(content)
    if "edu" in content:
        result_file = open('highvalue/edu.txt', 'a+', encoding='utf-8')
        result_file.write(content + "\r")
        result_file.close()


