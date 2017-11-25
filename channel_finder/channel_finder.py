#!/usr/bin/env python

import sys
from fuzzywuzzy import process

HOST = 'https://mobiltv.quickline.com'

# The first element in the sublists must be the display id:
CHANNEL_LIST = [
    ["itv-1-london", "itv-1-london", "ITV 1"],
    ["itv-2", "itv-2", "ITV 2"],
    ["itv-3", "itv-3", "ITV 3"],
    ["itv-4", "itv-4", "ITV 4"],
    ["itvbe", "itvbe", "ITVBe"],
    ["bbc-one", "bbc-one", "BBC One"],
    ["bbc2", "bbc2", "BBC Two"],
    ["bbc-four", "bbc-four", "BBC Four"],
    ["bbc-parliament", "bbc-parliament", "BBC Parliament"],
    ["cbeebies", "cbeebies", "CBeebies"],
    ["channel-4", "channel-4", "Channel 4"],
    ["five", "five", "Channel 5"],
    ["bbc-arabic", "bbc-arabic", "BBC Arabic"],
    ["e4", "e4", "E4"],
    ["film4", "film4", "Film 4"],
    ["more4", "more4", "More 4"],
    ["s4c", "s4c", "S4C"],
    ["srf1", "sf-1", "SRF 1"],
    ["srf_zwei", "sf-2", "SRF zwei"],
    ["srf_info", "sf-info", "SRF info"],
    ["3plus", "3plus", "3Plus"],
    ["4plus", "4plus", "4Plus"],
    ["daserste", "ard", "Das Erste"],
    ["zdf", "zdf", "ZDF"],
    ["tv24", "tv24", "TV24"],
    ["rtl", "rtl", "RTL"],
    ["prosieben", "prosieben", "Pro7 Schweiz"],
    ["sat1", "sat1", "Sat.1 Schweiz"],
    ["vox", "vox", "VOX"],
    ["rtl-2", "rtl-2", "RTL II"],
    ["kabel-eins", "kabel-eins", "kabel eins"],
    ["telezueri", "telezueri", "Telez\u00fcri"],
    ["s1", "s1", "S1"],
    ["startv", "startv", "Star TV"],
    ["orf-1", "orf-1", "ORF1"],
    ["orf-2", "orf-2", "ORF2"],
    ["dmax", "dmax", "DMAX"],
    ["rtlnitro", "rtlnitro", "NITRO"],
    ["weltderwunder", "weltderwunder", "Welt der Wunder"],
    ["sat1gold", "sat1gold", "SAT.1 Gold"],
    ["de_sixx", "de_sixx", "Sixx"],
    ["tele-5", "tele-5", "TELE 5"],
    ["anixe_hd", "anixe_hd", "Anixe"],
    ["servus_tv_deutschland", "servus_tv", "Servus TV"],
    ["super-rtl", "super-rtl", "Super RTL Schweiz"],
    ["disney", "disney", "Disney Channel"],
    ["nick", "nick", "Nickelodeon"],
    ["kika", "kika", "Kika"],
    ["ric", "ric", "RiC"],
    ["DE_arte", "DE_arte", "ARTE"],
    ["3sat", "3sat", "3Sat"],
    ["phoenix", "phoenix", "Phoenix"],
    ["br", "br", "BR Fernsehen S\u00fcd"],
    ["hr", "hr", "HR"],
    ["mdr-sachsen", "mdr-sachsen", "MDR SACHSEN"],
    ["ndr-niedersachsen", "ndr-niedersachsen", "NDR Niedersachsen"],
    ["rbb", "rbb", "rbb Berlin"],
    ["sr-fernsehen", "sr-fernsehen", "SR Fernsehen"],
    ["swr-fernsehen-bw", "swr-fernsehen-bw", "SWR BW"],
    ["wdr-koeln", "wdr-koeln", "WDR K\u00f6ln"],
    ["radio-bremen-tv", "radio-bremen-tv", "Radio Bremen TV"],
    ["tagesschau24", "einsextra", "tagesschau24"],
    ["one", "einsfestival", "ONE"],
    ["br-alpha", "br-alpha", "ARD-alpha"],
    ["zdf-info", "zdf-info", "ZDFinfo"],
    ["zdfneo", "zdfneo", "ZDFneo"],
    ["tele_top", "tele_top", "Tele Top"],
    ["telebaern", "telebaern", "TeleB\u00e4rn"],
    ["telebasel", "telebasel", "TeleBasel"],
    ["telebielingue", "telebielingue", "TeleBielingue"],
    ["telem1", "telem1", "Tele M1"],
    ["tele1", "tele1", "Tele 1"],
    ["latele", "latele", "LaTele"],
    ["lemanbleu", "lemanbleu", "Leman Bleu"],
    ["canalalpha", "canalalpha", "Canal Alpha NE"],
    ["tvo", "teleostschweiz", "TVO"],
    ["telesuedostschweiz", "telesuedostschweiz", "TeleS\u00fcdostschweiz"],
    ["teleticino", "teleticino", "TeleTicino"],
    ["sport1", "dsf", "Sport1"],
    ["eurosport1", "eurosport", "Eurosport 1"],
    ["al-jazeera", "al-jazeera", "Al Jazeera English"],
    ["bloomberg-europe", "bloomberg-europe", "Bloomberg TV"],
    ["cnn-international", "cnn-international", "CNN International"],
    ["bbc-world-service", "bbc-world-service", "BBC World News"],
    ["skynews-intl", "skynews-intl", "Sky News"],
    ["cnbceurope_b2c", "cnbceurope_b2c", "CNBC Europe"],
    ["euronews-en", "euronews-en", "EuroNews [en]"],
    ["france-24-en", "france-24-en", "France 24 [en]"],
    ["france-24-fr", "france-24-fr", "France 24 [fr]"],
    ["n24", "n24", "N24"],
    ["n-tv", "n-tv", "n-tv"],
    ["deraktionaertv", "daf", "Der Aktion\u00e4r TV"],
    ["deutsche-welle", "deutsche-welle", "Deutsche Welle"],
    ["mtv", "mtv", "MTV"],
    ["viva", "viva", "comedy"],
    ["deluxe-music", "deluxe-music", "DELUXE MUSIC"],
    ["bibeltv", "bibeltv", "Bibel TV"],
    ["god-channel-tv", "god-channel-tv", "GOD Channel"],
    ["sonlife", "sonlife", "SONLife"],
    ["rt_doc", "rt_doc", "RT Doc"],
    ["24_tv", "24_tv", "24-TV"],
    ["rts_un", "tsr1", "RTS un"],
    ["rts_deux", "tsr2", "RTS deux"],
    ["tf1", "tf1", "TF1"],
    ["m6-suisse", "m6-suisse", "M6 Suisse"],
    ["france-2", "france-2", "France 2"],
    ["france-3", "france-3", "France 3"],
    ["france-4", "france-4", "France 4"],
    ["france-5", "france-5", "France 5"],
    ["tmc", "tmc", "TMC"],
    ["direct-8", "direct-8", "C8 Suisse"],
    ["w9suisse", "w9suisse", "W9 Suisse"],
    ["arte-france", "arte-france", "ARTE [fr]"],
    ["gulli", "gulli", "Gulli"],
    ["nrj-12", "nrj-12", "NRJ 12"],
    ["tv5-monde", "tv5-monde", "TV5 Monde"],
    ["france-o", "france-o", "France \u00d4"],
    ["euronews-fr", "euronews-fr", "Euronews [fr]"],
    ["la1", "rsi-la1", "RSI La1"],
    ["la2", "rsi-la2", "RSI La2"],
    ["rai-uno", "rai-uno", "Rai Uno"],
    ["rai-due", "rai-due", "Rai Due"],
    ["rai_sport", "rai_sport", "Rai Sport"],
    ["rai_sport_plus", "rai_sport_plus", "Rai Sport +"],
    ["rainews", "rainews", "RAI News"],
    ["la-7", "la-7", "La 7"],
    ["rtl102_5", "rtl102_5", "RTL 102.5"],
    ["mtvitalia", "mtvitalia", "TV8"],
    ["dmaxitalia", "dmaxitalia", "DMAX Italia"],
    ["tve", "tve", "TVE"],
    ["24h", "canal24horas", "24H"],
]


def generate_url(display_id):
    return HOST + "/watch/%s" % display_id


def get_display_id(elem):
    for l in CHANNEL_LIST:
        display_id = l[0]
        for el in l:
            if el == elem:
                return display_id


def get_channel_url(name):
    flat_list = [item for sublist in CHANNEL_LIST for item in sublist]
    result = process.extractOne(name, flat_list)[0]
    display_id = get_display_id(result)
    return generate_url(display_id)


def main():
    if len(sys.argv) <= 1:
        sys.exit(0)
    name = " ".join(sys.argv[1:])
    url = get_channel_url(name)
    print(url)


if __name__ == "__main__":
    main()
