# Description

This is a pure-Python implementation of PDQ.

you can use this repo to quickly build a usable service.

# Dependencies

This uses the Python Image Library.

```
sudo pip3 install -r requirements.txt
```

# Running the server

```shell
python3 main.py
```

# Computing photo hashes

use the following command to compute the hash of a URL:

using the remote image

```shell
curl --location 'http://127.0.0.1:9000/uri/hashing' \
--header 'Content-Type: application/json' \
--data '{
    "url": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"
}'
```

or exists in the file `img/1675811437498658816.jpg`

```shell
curl --location 'http://127.0.0.1:9000/file/hashing' --form 'the_file=@"./img/1675811437498658816.jpg"'
```

# Running the Docker

```shell
docker build -t pdq .
docker run -p 9000:9000 pdq
```

# Reference

the original GitHub repo is [here](https://github.com/facebook/ThreatExchange)

[pdqhashing](./pdqhashing) is copied from the original [repo](https://github.com/facebook/ThreatExchange/tree/0a306c98fc67c0f9dfe57d0f7896af4540b8c692/pdq/python).
