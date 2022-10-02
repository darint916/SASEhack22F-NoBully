import enum
import json
import re
from typing import List
from mitmproxy import ctx
from mitmproxy.http import HTTPFlow

def match_url(patterns: List[re.Pattern], string):
    # ctx.log.error(patterns)
    for pattern in patterns:
        if (pattern.search(string)):
            return True
    return False
    # return any([i.match(string) for i in patterns])

def match_word(words, string):
    string = string.lower()
    return any([i in string for i in words])

def process_twitter(twitter, blocked, flow: HTTPFlow):
    blocked = []
    j = json.loads(twitter)
    ctx.log.error(bool(j.get('conversation_timeline')))

    if (j.get('conversation_timeline')):
        for idx, entry in enumerate(j['conversation_timeline']['entries']):
            ctx.log.error(entry)
            try:
                if (entry['message']):
                    msg_text = entry['message']['message_data']['text']

                    for word in blocked:
                        if (word in msg_text):
                            blocked.append(msg_text)
                            break
            except:
                pass

        # delete_entry = [i for i in j['conversation_timeline']['entries'] if i['message']['message_data']['text'] in blocked]
        j['conversation_timeline']['entries'] = [i for i in j['conversation_timeline']['entries'] if i['message']['message_data']['text'] not in blocked]

        ctx.log.error([i['message']['message_data']['text'] for i in j['conversation_timeline']['entries']])

        flow.response.text = json.dumps(j)
        return (blocked, )

    if (j.get('user_events')):
        return (j['user_events']['entries'][0]['message']['message_data']['text'])

def extract_twitter(twitter):
    # ctx.log.error(twitter)
    try:
        j = json.loads(twitter)
        return j['user_events']['entries'][0]['message']['message_data']['text']
    except:
        return twitter

def extract_insta(insta):
    j = json.loads(insta)
    jd = json.loads(j[0]["data"][0]["value"])
    return jd['text']
