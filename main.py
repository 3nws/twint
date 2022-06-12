import twint
import asyncio
import async_google_trans_new

from datetime import datetime


def get_real_time():
    now = datetime.utcnow()

    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    if hour < 10:
        hour = "0"+str(hour)
    minute = now.minute
    if minute < 10:
        minute = "0"+str(minute)
    second = now.second

    date_format = str(year)+"-"+str(month)+"-"+str(day)+" " + \
        str(hour)+":"+str(minute)+":"+str(second)

    return date_format

async def main():
    c = twint.Config()
    g = async_google_trans_new.AsyncTranslator()

    keywords = """ukraine OR kiev OR kyiv OR chernobyl OR ukrainian forces OR disinformation OR bomb OR shell OR missile OR assault OR airstrikes OR incursion OR artillery OR war OR warheads OR sanction OR 
    ukraine OR russia OR russian invasion OR ukraine war OR russian war OR zelensky OR putin OR vladimir putin OR volodymyr zelensky OR ukraine russia OR defence of ukraine"""

    # c.Search = keywords
    # c.Since = "2022-2-24"
    # c.Store_csv = True
    # c.Output = "war2.csv"

    # keywords_ru = " OR ".join([translator.translate(text=word, dest="ru").text for word in keywords.split(' OR ')])
    # print(keywords_ru)
    # c.Search = keywords_ru
    # c.Since = "2022-2-24"
    # c.Lang = "ru"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Count = True
    # c.Store_csv = True
    # c.Store_object = True
    # c.Output = "war-russian.csv"

    # keywords_de = " OR ".join([translator.translate(text=word, dest="de").text for word in keywords.split(' OR ')])
    # print(keywords_de)
    # c.Search = keywords_de
    # c.Since = "2022-2-24"
    # c.Lang = "de"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Count = True
    # c.Store_csv = True
    # c.Store_object = True
    # c.Output = "war-german.csv"

    # keywords_tr = " OR ".join([translator.translate(text=word, dest="tr").text for word in keywords.split(' OR ')])
    # print(keywords_tr)
    # c.Search = keywords_tr
    # c.Since = "2022-2-24"
    # c.Lang = "tr"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Count = True
    # c.Store_csv = True
    # c.Store_object = True
    # c.Output = "war-turkish.csv"

    # keywords_uk = " OR ".join([translator.translate(text=word, dest="uk").text for word in keywords.split(' OR ')])
    # print(keywords_uk)
    # c.Search = keywords_uk
    # c.Since = "2022-2-24"
    # c.Lang = "uk"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-ukrainian.csv"

    # keywords_it = " OR ".join([translator.translate(text=word, dest="it").text for word in keywords.split(' OR ')])
    # print(keywords_it)
    # c.Search = keywords_it
    # c.Since = "2022-2-24"
    # c.Lang = "it"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-italian.csv"

    # keywords_pt = " OR ".join([translator.translate(text=word, dest="pt").text for word in keywords.split(' OR ')])
    # print(keywords_pt)
    # c.Search = keywords_pt
    # c.Since = "2022-2-24"
    # c.Lang = "pt"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-portuguese.csv"

    # keywords_es = " OR ".join([translator.translate(text=word, dest="es").text for word in keywords.split(' OR ')])
    # print(keywords_es)
    # c.Search = keywords_es
    # c.Since = "2022-2-24"
    # c.Lang = "es"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-spanish.csv"

    # keywords_sv = " OR ".join([translator.translate(text=word, dest="sv").text for word in keywords.split(' OR ')])
    # print(keywords_sv)
    # c.Search = keywords_sv
    # c.Since = "2022-2-24"
    # c.Lang = "sv"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-swedish.csv"


    # keywords_de = " OR ".join([translator.translate(text=word, dest="de").text for word in keywords.split(' OR ')])
    # print(keywords_de)
    # c.Search = keywords_de
    # c.Since = "2022-2-24"
    # c.Lang = "de"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Count = True
    # c.Store_csv = True
    # c.Store_object = True
    # c.Output = "war-german.csv"

    # keywords_ar = " OR ".join([translator.translate(text=word, dest="ar").text for word in keywords.split(' OR ')])
    # print(keywords_ar)
    # c.Search = keywords_ar
    # c.Since = "2022-2-24"
    # c.Lang = "ar"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-arabic.csv"

    # keywords_fr = " OR ".join([translator.translate(text=word, dest="fr").text for word in keywords.split(' OR ')])
    # print(keywords_fr)
    # c.Search = keywords_fr
    # c.Since = "2022-2-24"
    # c.Lang = "fr"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-french.csv"

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "ga"))
    # keywords_ga = " OR ".join(tls)
    # print(keywords_ga)
    # c.Search = keywords_ga
    # c.Since = "2022-2-24"
    # c.Lang = "ga"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-irish.csv"
    
    # keywords_it = " OR ".join([translator.translate(text=word, dest="it").text for word in keywords.split(' OR ')])
    # print(keywords_it)
    # c.Search = keywords_it
    # c.Since = "2022-2-24"
    # c.Lang = "it"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-italian.csv"
    
    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "it"))
    # print(tls)
    # keywords_it = " OR ".join(tl[0] for tl in tls if isinstance(tl,list))
    # print(keywords_it)
    # c.Search = keywords_it
    # c.Since = "2022-2-24"
    # c.Lang = "it"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-italian.csv"

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "no"))
    # keywords_no = " OR ".join(tls)
    # print(keywords_no)
    # c.Search = keywords_no
    # c.Since = "2022-2-24"
    # c.Lang = "no"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-norwegian.csv"

    # keywords_pl = " OR ".join([translator.translate(text=word, dest="pl").text for word in keywords.split(' OR ')])
    # print(keywords_pl)
    # c.Search = keywords_pl
    # c.Since = "2022-2-24"
    # c.Lang = "pl"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-polish.csv"

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "ro"))
    # keywords_ro = " OR ".join(tls)
    # print(keywords_ro)
    # c.Search = keywords_ro
    # c.Since = "2022-2-24"
    # c.Lang = "ro"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-romanian.csv"

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "hu"))
    # keywords_hu = " OR ".join(tls)
    # print(keywords_hu)
    # c.Search = keywords_hu
    # c.Since = "2022-2-24"
    # c.Lang = "hu"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-hungarian.csv"

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "et"))
    # keywords_et = " OR ".join(tls)
    # print(keywords_et)
    # c.Search = keywords_et
    # c.Since = "2022-2-24"
    # c.Lang = "et"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-estonian.csv"

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "cs"))
    # keywords_cs = " OR ".join(tls)
    # print(keywords_cs)
    # c.Search = keywords_cs
    # c.Since = "2022-2-24"
    # c.Lang = "cs"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-czech.csv"

    # for word in keywords.split(' OR '):
    #     print(await g.translate(word, "be"))

    # tls = []
    # for word in keywords.split(' OR '):
    #     tls.append(await g.translate(word, "be"))
    # keywords_be = " OR ".join(tls)
    # print(keywords_be)
    # c.Search = keywords_be
    # c.Since = "2022-2-24"
    # c.Lang = "be"
    # c.Translate = True
    # c.TranslateDest = "en"
    # c.Store_csv = True
    # c.Output = "war-belarusian.csv"

    
    twint.run.Search(c)
    
asyncio.run(main())