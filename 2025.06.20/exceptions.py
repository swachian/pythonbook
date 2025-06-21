import logging

try:
    print(5/0)
except Exception as ex:
    print("Fail to divide by zero!")
    logging.exception("Fail to divide by zero!")
