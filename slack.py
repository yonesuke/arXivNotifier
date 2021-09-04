import slackweb
import feedparser
import html2text
import sys

args = sys.argv
slack_url = args[1]
slack = slackweb.Slack(url=slack_url)
rssurl = "http://arxiv.org/rss/nlin"

d = feedparser.parse(rssurl)
for entry in d.entries:
    if "UPDATED" in entry["title"]:
        continue
    attachment = {
        "pretext": entry["links"][0]["href"],
        "title": entry["title"],
        "text": html2text.html2text(entry["summary_detail"]["value"]).replace('\n', ' '),
        "mrkdwn_in": ["pretext", "title", "text"]
    }
    slack.notify(attachments=[attachment])
