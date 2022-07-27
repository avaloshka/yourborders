from __future__ import absolute_import, unicode_literals
from celery import shared_task

import requests
from bs4 import BeautifulSoup as bs
from .models import Borders
import time
import random


@shared_task
def get_border_info():

    BASE_URL = 'https://gpk.gov.by/situation-at-the-border/punkty-propuska/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    pages = ['grigorov/',
             'urbana/',
             'vidzy/',
             'kotlovka/',
             'losha/',
             'stone_log/',
             'benekainys/',
             'privalka/',
             'bruzgi/',
             'berestovitsa/',
             'peschatka/',
             'kozlovichi/',
             'brest/',
             'domachevo/',
             'tomashovka/',
             'oltush/',
             'mokrany/',
             'mohr/',
             'nevel/',
             'up_terebezhov/',
             'glushkevichi/',
             'new_rudnia/',
             'oleksandrivka/',
             'komarin/',
             'nova_huta/',
             'veselivka/'
             ]

    for page in pages:
        response = requests.get(BASE_URL + page, headers=headers)
        if response.status_code != 200:
            response.raise_for_status()
        soup = bs(response.content, 'html.parser')

        rows = soup.select('table.queuesTable tr')

        # Get punkt_propuska into list
        punkt_propuska = soup.find('h1', attrs={'class': 'ppr_title'}).text.strip()
        # Create punkt_propuska into list so I can concatinate 2 simple lists later
        list_punkt_propuska = []
        punkt_propuska = punkt_propuska[15:]
        list_punkt_propuska.append(punkt_propuska)

        # get values of the table that correspond to that index
        values = []
        for row in rows[1:]:  # The top row is rubbish so we will ignore it
            value = row.select('td')[1].text.strip()
            values.append(value)

        # Get bottom text
        bottom_text = soup.find('div', attrs={'class': 'ochered_bottom_text'}).text.strip()

        # Concatinate 2 lists
        initial_row = list_punkt_propuska + values
        t = []
        t.append(bottom_text)
        full_row = initial_row + t

        # CHECK IF RECORD EXISTS IN DATABASE

        try:
            # if record exists- replace it
            obj = Borders.objects.get(location=full_row[0])
            obj.location = full_row[0]
            obj.cars = full_row[1]
            obj.buses = full_row[2]
            obj.lorries = full_row[3]
            obj.text = full_row[4]

            obj.save()

        except:
            # add record
            b = Borders(location=full_row[0],
                        cars=full_row[1],
                        buses=full_row[2],
                        lorries=full_row[3],
                        text=full_row[4],
                        time=int(time.time()))
            b.save()