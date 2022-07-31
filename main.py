# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Hello Git world!")
import requests
headers={
'authority': 'vz-0823c98a-4c8.b-cdn.net',
'path': '/eac3e490-af1e-44d3-84bd-42f26350ab75/640x360/video.m3u8',
'origin': 'https://iframe.mediadelivery.net',
'referer': 'https://iframe.mediadelivery.net/',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
i=requests.get('https://vz-0823c98a-4c8.b-cdn.net/eac3e490-af1e-44d3-84bd-42f26350ab75/640x360/video.m3u8',headers=headers)
print(i.text)