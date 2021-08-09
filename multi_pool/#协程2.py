import asyncio
import time


async def request(url):
    print('正在下载', url)
    # 在异步协程中如果出现同步模块则无法使用异步
    # time.sleep(2)
    await asyncio.sleep(2)
    print('下载完成', url)


urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
    'www.sougou.com',
    'www.renren.com',
]
start = time.time()
# 任务列表 存放多个任务对象
tasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start)
