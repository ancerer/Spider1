from urllib import request
from bs4 import BeautifulSoup


class download(object):
    def __init__(self, target):
        self.__target_url = target
        self.__head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
        self.urls = []
        self.text_names = []

    # 获取相应章节的网址
    def get_download_url(self):
        target_req = request.Request(url=self.__target_url, headers=self.__head)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('gbk','ignore')
        soup = BeautifulSoup(target_html, 'lxml')
        download_url_soup = soup.find(class_="listmain")
        lists = download_url_soup.find_all('a')
        for list in lists:
            '''
            print(list)
            print(list.string)
            '''
            self.text_name = list.string
            self.text_names.append(self.text_name)
            self.url = list['href']
            self.urls.append(self.url)
            print(self.url)


    def download_text(self):
        filename = 'ynyh.txt'
        for i in range(len(self.urls)):
            download_url = 'http://www.biqukan.com' + self.urls[i]
            download_req = request.Request(url=download_url, headers=self.__head)
            download_url_response = request.urlopen(download_req)
            download_url_r = download_url_response.read().decode('gbk','ignore')
            url_soup = BeautifulSoup(download_url_r, 'lxml')
            text_name = self.text_names[i]
            text_content = url_soup.find(id='content')
            soup_text = BeautifulSoup(str(text_content), 'lxml').div.text.replace('\xa0','')
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(text_name + '\n')
                f.write(soup_text)







if __name__ == "__main__":
    # 小说地址
    target_url = 'http://www.biqukan.com/1_1094/'
    # 实例化下载类
    down = download(target=target_url)
    down.get_download_url()
    down.download_text()

