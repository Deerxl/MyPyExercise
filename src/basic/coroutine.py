

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...'% n)
        r='200 0K'



def produce(producer):
    producer.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...'% n)
        r = producer.send(n)
        print('[PRODUCER] Consumer return:%s'% r)
    producer.close()


# 协程的交互方式
if __name__ == '__main__':
    c = consumer()
    produce(c)