import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(url, img_name):
    res = urllib.request.urlopen(url)
    img_content = res.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    urls = [
        "https://rpic.douyucdn.cn/live-cover/appCovers/2017/10/13/2270388_20171013013734_small.jpg",
        "https://rpic.douyucdn.cn/live-cover/appCovers/2018/11/04/4446780_20181104221734_small.jpg",
        "https://rpic.douyucdn.cn/live-cover/appCovers/2018/10/08/5725848_20181008153156_small.jpg"
    ]
    gevent.joinall([
        gevent.spawn(downloader, urls[0], "1.jpg"),
        gevent.spawn(downloader, urls[1], "2.jpg"),
        gevent.spawn(downloader, urls[2], "3.jpg")
    ])


if __name__ == '__main__':
    main()
