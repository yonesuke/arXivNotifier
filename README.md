# arXivNotifier

This repository notifies newly published papers from arXiv using GitHub Actions.

## SetUp
1. Create incoming webhook of a channel.
2. Add the URL to repository secrets.
![secrets_screenshots](https://user-images.githubusercontent.com/12659790/132085796-094ce1c6-349a-4eb4-a7af-3a9a624709b7.png)
3. Default division is [Nonlinear science](https://arxiv.org/list/nlin/recent). If you want to change it to another division, let's say [Computer science](https://arxiv.org/list/cs/recent), change [slack.py](slack.py) to the following.
    ```python
    rssurl = "http://arxiv.org/rss/cs"
    ```
  

## How it looks like
![secrets_slack](https://user-images.githubusercontent.com/12659790/132085827-cadbbef7-03d9-435e-9385-901cc8d50271.png)

