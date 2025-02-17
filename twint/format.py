import logging as logme

def Tweet(config, t):
    if config.Format:
        logme.debug(__name__+':Tweet:Format')
        # output = config.Format.replace("{id}", str(t.id_str))
        # output = output.replace("{conversation_id}", str(t.conversation_id))
        # output = output.replace("{date}", str(t.datestamp))
        # output = output.replace("{time}", str(t.timestamp))
        output = output.replace("{user_id}", str(t.user_id_str))
        output = output.replace("{username}", t.username)
        # output = output.replace("{name}", str(t.name))
        # output = output.replace("{place}", t.place)
        # output = output.replace("{timezone}", str(t.timezone))
        # output = output.replace("{urls}", ",".join(str(t.urls)))
        # output = output.replace("{photos}", ",".join(str(t.photos)))
        # output = output.replace("{video}", str(t.video))
        # output = output.replace("{thumbnail}", str(t.thumbnail))
        output = output.replace("{tweet}", t.tweet)
        output = output.replace("{language}", str(t.lang))
        # output = output.replace("{hashtags}", ",".join(str(t.hashtags)))
        # output = output.replace("{cashtags}", ",".join(str(t.cashtags)))
        # output = output.replace("{replies}", str(t.replies_count))
        # output = output.replace("{retweets}", str(t.retweets_count))
        # output = output.replace("{likes}", str(t.likes_count))
        # output = output.replace("{link}", str(t.link))
        # output = output.replace("{is_retweet}", str(t.retweet))
        # output = output.replace("{user_rt_id}", str(t.user_rt_id))
        # output = output.replace("{quote_url}", str(t.quote_url))
        # output = output.replace("{near}", t.near)
        # output = output.replace("{geo}", t.geo)
        # output = output.replace("{mentions}", ",".join(str(t.mentions)))
        output = output.replace("{translate}", t.translate)
        output = output.replace("{trans_src}", t.trans_src)
        output = output.replace("{trans_dest}", t.trans_dest)
    else:
        logme.debug(__name__+':Tweet:notFormat')
        output = f"{t.id_str} {t.datestamp} {t.timestamp} {t.timezone} "

        # TODO: someone who is familiar with this code, needs to take a look at what this is <also see tweet.py>
        # if t.retweet:
        #    output += "RT "

        output += f"<{t.username}> {t.tweet}"

        if config.Show_hashtags:
            hashtags = ",".join(t.hashtags)
            output += f" {hashtags}"
        if config.Show_cashtags:
            cashtags = ",".join(t.cashtags)
            output += f" {cashtags}"
        if config.Stats:
            output += f" | {t.replies_count} replies {t.retweets_count} retweets {t.likes_count} likes"
        if config.Translate:
            output += f" {t.translate} {t.trans_src} {t.trans_dest}"
    return output

def User(_format, u):
    if _format:
        logme.debug(__name__+':User:Format')
        output = _format.replace("{id}", str(u.id))
        # output = output.replace("{name}", u.name)
        output = output.replace("{username}", u.username)
        # output = output.replace("{bio}", u.bio)
        output = output.replace("{location}", u.location)
        # output = output.replace("{url}", u.url)
        # output = output.replace("{join_date}", u.join_date)
        # output = output.replace("{join_time}", u.join_time)
        # output = output.replace("{tweets}", str(u.tweets))
        # output = output.replace("{following}", str(u.following))
        # output = output.replace("{followers}", str(u.followers))
        # output = output.replace("{likes}", str(u.likes))
        # output = output.replace("{media}", str(u.media_count))
        # output = output.replace("{private}", str(u.is_private))
        # output = output.replace("{verified}", str(u.is_verified))
        # output = output.replace("{avatar}", u.avatar)
        # if u.background_image:
        #     output = output.replace("{background_image}", u.background_image)
        # else:
        #     output = output.replace("{background_image}", "")
    else:
        logme.debug(__name__+':User:notFormat')
        output = f"{u.id} | @{u.username}"
        output += f"Location: {u.location}"

    return output
