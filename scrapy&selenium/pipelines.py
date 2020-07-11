import json

class BytedancePipeline:
    def __init__(self):
        self.f = open("bytedance.json", "w",encoding = 'utf-8')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii = False) + '\n'
        self.f.write(content)
        return item
    def close_spider(self, spider):
        self.f.close()
