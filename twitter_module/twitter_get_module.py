import twitter
import pymysql 
import datetime

# execute code log
d = datetime.datetime.now() 

#setting
twitter_consumer_key = ""
twitter_consumer_secret = ""
twitter_access_token = ""
twitter_access_secret = ""

accounts = ["@sample"]

#crontab log
print(d)

# db connect 
conn = pymysql.connect(
		user="",
		passwd="",
		host="",
		db=""
		)
cursor = conn.cursor()


# twitter connect
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

#output_file_name = "twitter_get_timeline.txt"


for account in accounts:
# twitter crolling setting 
	try:
		statuses = twitter_api.GetUserTimeline(screen_name=account, count=1, include_rts=True, exclude_replies=False)
	except Exception as e:
		print(e,"ERROR")

# logfile & status setting
	for status in statuses:
		print(account,d)

# insert db
	date=status.created_at.replace('+0000','')
	cursor.execute(f"INSERT IGNORE INTO coin_t VALUES(\"{date}\",\"{account}\",\"{status.text}\",\"{d}\")")
conn.commit()
conn.close()
