# coding: utf-8
from __future__ import unicode_literals

import re

from .regexp import build_good_phrase, build_bad_phrase


bad_words = [
    build_bad_phrase('п еиeu з д'),
    build_bad_phrase('хx уy йёуяиюyu'),
    build_bad_phrase('оo хx уy еe втл'),
    build_bad_phrase('п и д оеаoea рp'),
    build_bad_phrase('пn иu д рp'),
    build_bad_phrase('еёe б аa нклт'),
    build_bad_phrase('уy еёe б оаoa нткk'),
    build_bad_phrase('еёe б л аоиao'),
    build_bad_phrase('в ы еёe б'),
    build_bad_phrase('еe б ё т'),
    build_bad_phrase('св ъь еёиeu б6'),
    build_bad_phrase('б6 л я'),
    build_bad_phrase('г аоao в н'),
    build_bad_phrase('м уy д аa к'),
    build_bad_phrase('г аоao н д оo н'),
    build_bad_phrase('ч4 м оыo'),
    build_bad_phrase('д еe рp ь м'),
    build_bad_phrase('ш л ю хx'),
    build_bad_phrase('з3 аоao л уy п'),
    build_bad_phrase('сc уy ч4 аa рp'),
    build_bad_phrase('д аоao л б6 аоao еёe б6'),
    build_bad_phrase('п рp аоao еёe б6'),
    build_bad_phrase('сc уy кk аa'),
    build_bad_phrase('д рp оаoa ч4'),
    build_bad_phrase('хx уy еe сc оo сc'),
    build_bad_phrase('хx уy йя'),
    build_bad_phrase('еe б аa ть'),
    build_bad_phrase('м аa н д аa'),
    build_bad_phrase('м yу д л оoаaеe'),
    build_bad_phrase('ж оo п'),
    build_bad_phrase('eеё б уяy'),
    build_bad_phrase('т в оo ю м аa т ь'),
    build_bad_phrase('м аa т ь т в оo ю'),
    build_bad_phrase('т р а х'),
    build_bad_phrase('еe п т'),
    build_bad_phrase('з3 аa сc рp аa н еe ц'),
    build_bad_phrase('уy б л ю д оo кk'),
    build_bad_phrase('оаoa н аa н иu сc т'),
    build_bad_phrase('п аa д л ауоеayoe'),
]
bad_words_re = re.compile('|'.join(bad_words), re.IGNORECASE | re.UNICODE)

good_words = [
    build_good_phrase('с к и п и д а р'),
    build_good_phrase('к о л е б а н и яей'),
    build_good_phrase('к о м а н д а'),
    build_good_phrase('з ао к оа л е б а лт'),
    build_good_phrase('р у б л я'),
    build_good_phrase('с т е б е л ь'),
    build_good_phrase('с т р а х о в к ауи'),
    build_good_phrase('в с е м у д а ч и'),
    build_good_phrase('к н и г а'),
    build_good_phrase('м а р к с у'),
    build_good_phrase('р а с х о ж д е н'),
    build_good_phrase('н е б л а г о п р и я т'),
    build_good_phrase('н е б л а г о п р и я т'),
    build_good_phrase('б а з у'),
    build_good_phrase('н е ф т е б а з'),
    build_good_phrase('м а н д а р и н'),
    build_good_phrase('т р а х е'),
    build_good_phrase('т е б я'),
    r'([о][с][к][о][Р][б][л][я]([т][ь])*([л])*([е][ш][ь])*)',
    r'([в][л][ю][б][л][я](([т][ь])([с][я])*)*(([е][ш][ь])([с][я])*)*)',
    r'((([п][о][д])*([з][а])*([п][е][р][е])*)*[с][т][р][а][х][у]([й])*([с][я])*([е][ш][ь])*([е][т])*)',
    r'([м][е][б][е][л][ь]([н][ы][й])*)',
    r'([Уу][Пп][Оо][Тт][Рр][Ее][Бб][Лл][Яя]([Тт][Ьь])*([Ее][Шш][Ьь])*([Яя])*([Лл])*)',
    r'([Ии][Сс][Тт][Рр][Ее][Бб][Лл][Яя]([Тт][Ьь])*([Ее][Шш][Ьь])*([Яя])*([Лл])*)',
    r'([Сс][Тт][Рр][Аа][Хх]([Аа])*)',
]
good_words_re = re.compile('|'.join(good_words), re.IGNORECASE | re.UNICODE)
