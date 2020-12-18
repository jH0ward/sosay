from stackapi import StackAPI
from datetime import datetime
import pandas as pd
SITE = StackAPI('stackoverflow')
# comments = SITE.fetch('comments')


def sosay(func):
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            err = str(e)
            questions = SITE.fetch('search', intitle=err, fromdate=datetime(2018, 11, 11),
                                   todate=datetime(2020, 12, 17),
                                   min=1, sort='votes')
            try:
                link = questions['items'][0]['link']
                print(f'S.O. says {link}')
            except Exception as e:
                print(err)
            return err
    return inner


@sosay
def a_bad_func():
    df = pd.DataFrame(1)

@sosay
def a_terrible_func():
    df = '9' / '42'


if __name__ == '__main__':
    a_bad_func()
    a_terrible_func()
