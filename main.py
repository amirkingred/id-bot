#info bot created by negative
#info bot created by negative
#info bot created by negative
#info bot created by negative
import telebot
from telebot import types
from telebot import util
import sys
import json
import logging
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    cid = m.chat.id
    bot.send_message(cid, "Hello I'm ID bot \n\n Send : \n  /id or /me or /info   \n or all pm text \n\n get your id : \n /idme (just pv)")

@bot.message_handler(commands=['id', 'ids', 'info', 'me'])
def id(m):      # info menu
    cid = m.chat.id
    title = m.chat.title
    usr = m.chat.username
    f = m.chat.first_name
    l = m.chat.last_name
    t = m.chat.type
    d = m.date
    text = m.text
    p = m.pinned_message
    fromm = m.forward_from
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown")

@bot.message_handler(commands=['contact'])
def c(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_contact(uid, phone_number="+989379097344", first_name="Negative")


@bot.message_handler(commands=['about']) # copy right Taylor Team
def p(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_message(uid, "Taylor Team development Telegram bot and web mastering \n\n developers : \n [negative](https://telegram.me/negative_officiall) \n [Parham](https://telegram.me/UnFriendlly)", parse_mode="Markdown")
    bot.send_photo(uid, open('taylor.jpg'), caption="@Taylor_Team")

@bot.message_handler(commands=['idbot'])
def handler(m):
    cid = m.chat.id
    bot.send_message(cid, "My Name is ID bot \n creator and developer : [negative](https://telegram.me/negative_officiall) \n development channel : [Taylor Team](https://telegram.me/taylor_team)\n\n [github](https://github.com/taylor-team/id-bot)", parse_mode="Markdown")
    
@bot.message_handler(commands=['idme'])
def test_handler(m):
    cid = m.chat.id
    fl = m.chat.first_name
    bot.send_message(cid, "*{}*  Your ID = ```{}```".format(fl,cid), parse_mode="Markdown")
    
    
@bot.inline_handler(lambda query: len(query.query.split()) == 0)
def query_text(query):
    try:
        user = query.from_user.username
        name = query.from_user.first_name
        lname = query.from_user.last_name
        uid = query.from_user.id
        info = types.InlineQueryResultArticle('1', '\xE2\x9C\x8F Your Info \xE2\x9C\x8F', types.InputTextMessageContent('*Username : @{}\nYour First Name : {}\nYour Last Name : {}\nYour ID : {}*'.format(user,name,lname,uid), parse_mode="Markdown"))
        pic = types.InlineQueryResultPhoto('2', 'http://vip.opload.ir/vipdl/95/3/negative23/photo-2016-06-09-01-09-41.jpg', 'http://vip.opload.ir/vipdl/95/3/negative23/photo-2016-06-09-01-09-41.jpg', input_message_content=types.InputTextMessageContent('@Taylor_Team'))
        bot.answer_inline_query(query.id, [info], cache_time="5")
    except Exception as user:
        print(user)


@bot.message_handler(func=lambda message: True)  # on pv all pm / group /id /me pm created by negative
def id(m):  # info menu
    cid = m.chat.id #id from
    title = m.chat.title #group title
    usr = m.chat.username #username
    f = m.chat.first_name #First name
    l = m.chat.last_name #last name
    t = m.chat.type #type
    d = m.date #data
    text = m.text #msg text
    p = m.pinned_message #msg pined
    fromm = m.forward_from #from
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown")



bot.polling(True)
#end
