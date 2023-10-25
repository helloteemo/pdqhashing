import io
import logging

import requests
from flask import Flask
from flask import request

from pdqhashing.hasher.pdq_hasher import PDQHasher

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route("/maintenance")
def maintenance():
    return "<p>Hello, World!</p>"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/file/hashing', methods=['GET', 'POST'])
# 使用 form-data 传递参数，其中file key 为 the_file. value为文件
def upload_file():
    if request.method == 'POST':
        f = request.files.get('the_file')
        if f is None:
            return {
                "code": -2,
                "msg": "file is None"
            }

        pdqHasher = PDQHasher()
        hashAndQuality = pdqHasher.fromBufferedImage(f)
        logging.info("[file/hashing] filename: {} pdq hashing: {}".format(f.filename, hashAndQuality.getHash()))
        return {
            "code": 1,
            "hash": str(hashAndQuality.getHash()),
            "quality": int(hashAndQuality.getQuality())
        }
    else:
        return {
            "code": -1,
            "msg": "please using POST"
        }


@app.route('/uri/hashing', methods=['GET', 'POST'])
# 使用 application/json 传递参数, 格式如下：
# {
#     "url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"
# }
def upload_url():
    if request.method == 'POST':
        body = request.json
        url = body["url"]
        imageBytes = download_img(url)
        pdqHasher = PDQHasher()
        hashAndQuality = pdqHasher.fromBufferedImage(io.BytesIO(imageBytes))
        logging.info("[uri/hashing] url:{} pdq hashing: {}".format(url, hashAndQuality.getHash()))
        return {
            "code": 1,
            "hash": str(hashAndQuality.getHash()),
            "quality": int(hashAndQuality.getQuality())
        }
    else:
        return {
            "code": -1,
            "msg": "please using POST"
        }


def download_img(img_url):
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        var = r.content
        r.close()
        return var
    del r


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
