__author__ = 'Deepak Verma <yesdeepakverma@gmail.com>'

import random
import datetime

from hashlib import sha1
from random import randint


class GenerateToken(object):
    @property
    def otp(self, digit=6):
        """
        Generate One time passord
        :return:
        """
        # now = datetime.datetime.now()
        # token = "{}{}{}{}{}".format(str(now.month).rjust(2, '0'),
        #                   str(now.day).rjust(2, '0'),
        #                   str(now.hour).rjust(2, '0'),
        #                   str(now.minute).rjust(2, '0'),
        #                   str(now.second).rjust(2, '0')
        #                   )
        # return token
        return randint(1000, 9999)

    @property
    def auth(self):
        """
        Generate Authentication token
        :return:
        """
        return self.generate_random()

    @property
    def token(self):
        """
        Generate password reset token
        :return:
        """
        return self.generate_random()

    def generate_random(self, data=''):
        salt = str(random.random())
        cur_date = str(datetime.datetime.now())
        data = (str(data) or '')
        token = sha1(str(data+cur_date+salt)).hexdigest()
        return token


if __name__ == '__main__':
    print(GenerateToken().otp)
    print(GenerateToken().auth)
    print(GenerateToken().token)
