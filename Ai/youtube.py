from turtle import title
from youtube_search import YoutubeSearch
import webbrowser


while True:
    inp = input()
    rs = YoutubeSearch(inp, max_results=10).to_dict()
    for i in range(10):
        print(i+1,'  ', rs[i]['title'].split('|')[0] , "\n    ", rs[i]["duration"])
    if rs:
        l = int(input("moi ban chon bai: "))
        break
url = 'http://www.youtube.com' + rs[l-1]['url_suffix']
webbrowser.open(url)
