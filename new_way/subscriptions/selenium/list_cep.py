# -*- coding: utf-8 -*-
import random


def get_cep():
    list_cep = [
        '40230605',
        '02675060',
        '79065230',
        '50060060',
        '74884080',
        '29120014',
        '12220600',
        '36047240',
        '78156318',
        '70675723',
        '09131160',
        '18404400',
        '07054100',
        '14801137',
        '07050020',
        '06757120',
        '13238502',
        '13270210',
        '12327704',
        '12410340',
        '05171240',
        '20511330',
        '20521110',
        '20511170',
        '13034640',
        '02755090',
        '05442030',
        '06246090',
        '04517100',
        '11712020',
        '13566600',
        '13904525',
        '13735078',
        '14784033',
        '03121040',
        '14875702',
        '02970040',
        '03880120',
        '06293090',
        '05523000',
    ]
    cep = random.choice(list_cep)
    return cep