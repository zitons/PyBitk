# -*- coding: utf-8 -*-
# @Time : ${DATE} ${TIME}
# @Author : zitons
# @Email : zitons@outlook.com
# @File : ${NAME}.py
# @Project : ${PROJECT_NAME}
#待优化
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello Git world!")
import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor

headers = {
    'authority': 'vz-0823c98a-4c8.b-cdn.net',
    'path': '/eac3e490-af1e-44d3-84bd-42f26350ab75/640x360/video.m3u8',
    'origin': 'https://iframe.mediadelivery.net',
    'referer': 'https://iframe.mediadelivery.net/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
i = requests.get('https://vz-0823c98a-4c8.b-cdn.net/eac3e490-af1e-44d3-84bd-42f26350ab75/640x360/video.m3u8',
                 headers=headers)
print(i.text)
ts = i.text
with open('play.tx', 'w+') as file:
    file.write(ts)

start = time.time()
# 准备下载路径
m3u8 = []
with open('play.tx', 'r') as file:
    lst = file.readlines()

    for i in lst:
        print(i)
        i = i.strip()
        if i.startswith('#'):
            continue
        else:
            m3u8.append(i)
print(f'目标文件数共{len(m3u8)}个')


# 下载一个ts文件的函数
def download_ts(i):
    for _ in range(10):
        try:
            with open(f'{i}.ts', 'wb') as file:
                resp = requests.get(
                    'https://vz-0823c98a-4c8.b-cdn.net/eac3e490-af1e-44d3-84bd-42f26350ab75/640x360/' + m3u8[i],
                    headers=headers).content
                file.write(resp)
            print(f'第{i}个ts片段已下载完成!')
            break
        except:
            print(f'第{i}个ts文件下载失败，重新下载！')
            continue


with ThreadPoolExecutor(100) as t:
    for i in range(len(m3u8)):
        t.submit(download_ts, i)
    t.shutdown()
# 补录程序
with ThreadPoolExecutor(50) as f:
    for i in range(len(m3u8)):
        with open(f'{i}.ts', 'rb+') as file:
            if file.read():
                continue
            else:
                f.submit(download_ts, i)
    f.shutdown()
print('ts文件下载完毕')
# ts文件的合并
print('ts文件开始合并....')
with open('test.mp4', 'wb') as file:
    for i in range(len(m3u8)):
        with open(f'{i}.ts', 'rb') as f:
            f_view = f.read()
            file.write(f_view)
print('ts文件合并完毕!')
# ts文件的删除操作
# print('开始删除ts文件....')
# for i in range(len(m3u8)):
#     try:
#      os.remove(rf'E:\PyProject\{i}.ts')
#     except FileNotFoundError:
#         continue
# print('ts文件删除完毕！')
print('电影完美下载！')
end = time.time()
print('本次下载共耗时长：', end - start, 's')
