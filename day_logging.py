import logging

logging.basicConfig(filename="my_basic_3.log", level=logging.INFO)
logging.info("hey hi logging")
logging.warning("hey logging this is a warning!")
logging.error("this is a system error")

l = [1,2,3,4,5,6]
for i in l:
    if(i%2==0):
        logging.warning("the list has the even numbr and it is printred")
        logging.info(f'this an evn number {i}')

logging.shutdown()


