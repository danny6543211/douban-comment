import requests
from bs4 import BeautifulSoup
import time
import os

# 请求头
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
    , 
    'cookie': 
    'bid=Z5YqxtsS-PY; viewed="35196328"; ct=y; ll="108306"; _pk_id.100001.4cf6=b7610704fc18dcbf.1690814391.; _vwo_uuid_v2=D97F2FF07E681ADB476F8897208CB57F7|65bf3f60727fc1f687f499a02d512a1b; __utmz=30149280.1691044679.9.4.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1691045117.8.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1691050863%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utma=30149280.128983496.1689642155.1691044679.1691050863.10; __utmc=30149280; __utma=223695111.2028630251.1690814392.1691045117.1691050863.9; __utmc=223695111; __utmt=1; __utmb=30149280.1.10.1691050863; dbcl2="272854055:Ath8e5hVWr4"; ck=sBFT; __utmb=223695111.2.10.1691050863; push_noty_num=0; push_doumail_num=0'
}

# url字典
url_dict = {
    '武林外传': 'https://movie.douban.com/subject/3882715/comments?status=P',
    '甄缳传': 'https://movie.douban.com/subject/4922787/comments?status=P',
    '红楼梦': 'https://movie.douban.com/subject/1864810/comments?status=P',
    '大明王朝1566': 'https://movie.douban.com/subject/2210001/comments?status=P',
    '仙剑奇侠传(一)': 'https://movie.douban.com/subject/2210031/comments?status=P',
    '仙剑奇侠传(三)': 'https://movie.douban.com/subject/3227335/comments?status=P',
    '大宋提刑官': 'https://movie.douban.com/subject/2239292/comments?status=P',
    '大明宫词': 'https://movie.douban.com/subject/2154859/comments?status=P',
    '少年包青天': 'https://movie.douban.com/subject/2157131/comments?status=P',
    '上错花桥嫁对郎': 'https://movie.douban.com/subject/2229576/comments?status=P',
    '大秦帝国之裂变': 'https://movie.douban.com/subject/3114220/comments?status=P',
    '琅琊榜': 'https://movie.douban.com/subject/25754848/comments?status=P',
    '山河令': 'https://movie.douban.com/subject/34923491/comments?status=P',
    '长安十二时辰': 'https://movie.douban.com/subject/26849758/comments?status=P',
    '庆余年': 'https://movie.douban.com/subject/25853071/comments?status=P',
    '宸汐缘': 'https://movie.douban.com/subject/30230682/comments?status=P',
    '琅琊榜之风起长林': 'https://movie.douban.com/subject/26665065/comments?status=P',
    '陈情令': 'https://movie.douban.com/subject/27195020/comments?status=P',
    '御赐小仵作': 'https://movie.douban.com/subject/32581207/comments?status=P',
    '天盛长歌': 'https://movie.douban.com/subject/26761328/comments?status=P',
    '知否知否应是绿肥红瘦': 'https://movie.douban.com/subject/26928226/comments?status=P'
}

# 翻页后url
def other_url(url, start):
    return url+'&start='+str(start)+'&limit=20&sort=new_score'

# 抓取评论
def get_comment(movie_name, url):
    # 目前豆瓣短评只放出六百多个评论
    max_comment = 700
    # 抓取页面
    file = open(movie_name+'.txt', 'w', encoding='utf-8')
    for start in range(0, max_comment, 20):
        html = requests.get(other_url(url, start), headers=header).text
        soup = BeautifulSoup(html, 'lxml')
        find = soup.find_all(class_='short')
        for comment in find:
            file.write(comment.text+'\n')
        # ui界面
        time.sleep(2)
        os.system('cls')
        print(movie_name)
        print('{0:.2f}%'.format(start/(max_comment/100)))
    file.close()

# 主函数
if __name__ == '__main__':
    for key, value in url_dict.items():
        get_comment(key, value)