from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("https://blog.csdn.net/c406495762/article/details/58716886")
    html = response.read()
    charset = chardet.detect(html)
    decode = charset['encoding']
    hm = html.decode(decode)
    print(decode)
    print(charset)
    print(hm)