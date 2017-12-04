import configparser
import os
from os.path import dirname, join
from TwitterAPI import TwitterAPI


package_dir = dirname(__file__)
images_dir = join(package_dir, 'images')
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# auth
config = configparser.ConfigParser()
config.read(join(package_dir, 'auth.ini'))
auth = config['AUTH']
consumer_key = auth['consumer key']
consumer_secret = auth['consumer secret']
token = auth['token']
token_secret = auth['token secret']

twitter_api = TwitterAPI(consumer_key, consumer_secret, token, token_secret)

# gbf
gbf_source = ('<a href="http://granbluefantasy.jp/" '
              'rel="nofollow">グランブルー ファンタジー</a>')


if __name__ == '__main__':
    print(package_dir)
