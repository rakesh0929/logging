import logging
logging.basicConfig(filename="test4.log",level=logging.CRITICAL,format='%(levelname)s : %(name)s : %(asctime)s : %(message)s ')

try:
    logging.info("i am reading the file :")
    with open("rakesh_1.txt","r"):
        logging.info("Rakesh file is read successfully")
except Exception as e:
    logging.critical("this is critical situation")
    logging.error(e)


