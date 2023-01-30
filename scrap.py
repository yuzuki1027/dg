import urllib.request
from bs4 import BeautifulSoup

url = "https://www.amazon.co.jp/s?k=%E6%97%A5%E6%9C%AC%E6%98%A0%E7%94%BB&i=instant-video&bbn=4217521051&rh=n%3A4217521051%2Cp_n_feature_six_browse-bin%3A5871472051&dc&ds=v1%3AYy78u2RtvELVwYqpiJJ2oYBw%2Bv2N5Q3tn9ToEi0ZkFc&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&qid=1675083564&rnid=5871471051&ref=sr_nr_p_n_feature_six_browse-bin_1"  # 取得したいURLを入力
chrome = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 GoogleChrome/89.0"} # ブラウザを設定

request = urllib.request.Request(url=url, headers=chrome) # 指定したブラウザとURLを設定
url_file = urllib.request.urlopen(request) # 指定したブラウザでURLを開く
encording = url_file.info().get_content_charset() 

text = url_file.read().decode(encording) # デコードしたオブジェクトをtextに代入

soup = BeautifulSoup(text, 'html.parser')

for a in soup.find_all(class_ = 'a-size-base-plus a-color-base a-text-normal'):
    if a.text != '':
        a_text = a.text
        print(a_text)