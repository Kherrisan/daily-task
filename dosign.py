#coding=utf-8

import requests
import json

COOKIES = "bsource=seo_google; PVID=1; _dfcaptcha=01e1ec4881472119a4bfdec45bb01803; bp_t_offset_13288240=386224586205337954; CURRENT_FNVAL=16; _uuid=F90648EB-CA4F-50E1-13A1-CE8AACBA65BB49950infoc; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1588424548; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1587729910,1588072783,1588136048,1588418390; CURRENT_QUALITY=80; GIFT_BLOCK_COOKIE=GIFT_BLOCK_COOKIE; DedeUserID=13288240; DedeUserID__ckMd5=457dfe15498f3982; SESSDATA=928f6980%2C1600417530%2C57da0*31; bili_jct=2b64ca41491b5f41cb68a06342a90688; rpdid=|(umk~lk~uu~0J'ul)kk~uRll; LIVE_BUVID=AUTO8015822710667924; sid=ajhtqjem; buvid3=1D2FA7FE-769A-43E3-9F03-C7644C9EF21853945infoc"

def read_cookie(cookiepath):
	with open(cookiepath, 'r') as fid:
		cookies = fid.readlines()
	return cookies

def do_sign(headers):
	url_live = "https://api.live.bilibili.com/sign/doSign"
	r = requests.get(url_live, headers=headers)
	print('doSign: ' + str(r.text))

def silver2coin(headers):
	url_coin = "https://api.live.bilibili.com/pay/v1/Exchange/silver2coin"
	r = requests.get(url_coin, headers=headers)
	print('silver2coin: ' + json.loads(r.text)['msg'])

if __name__=='__main__':
	cookies = COOKIES
	headers = {
	    'accept-encoding': 'gzip, deflate, sdch',
	    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.16 Safari/537.36',
	    'authority': 'live.bilibili.com',
	    'cookie': cookies,
	}
	do_sign(headers)
	# silver2coin(headers)
