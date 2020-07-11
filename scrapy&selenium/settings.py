ROBOTSTXT_OBEY = False
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
DOWNLOADER_MIDDLEWARES = {
    'bytedance.middlewares.BytedanceDownloaderMiddleware': 543,
}
ITEM_PIPELINES = {
    'bytedance.pipelines.BytedancePipeline': 300,
}
