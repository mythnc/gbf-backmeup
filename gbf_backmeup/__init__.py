import configparser
import os
from os.path import dirname, join


__all__ = []

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
