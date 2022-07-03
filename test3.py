import logging
logging.basicConfig(filename="test_3.log",level=logging.WARNING,format='%(levelname)s : %(name)s : %(asctime)s : %(message)s ')

def divide_two_numbers(a,b):
    logging.info(f"this code divides the two integers {a} / {b} and return the float value of it")
    try:
        logging.info("we aee in info")
        div =  a/b
        logging.info("end the div")
        logging.info("this is a value of division {}".format(div))
        return div
    except Exception as e:
        logging.exception(e)
divide_two_numbers(3,0)