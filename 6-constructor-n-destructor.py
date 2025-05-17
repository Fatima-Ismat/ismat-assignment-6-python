class Logger:
     def __init__(self):
          print("Message Before: Logger object created.") # constructor message

     def __del__(self):
          print("Message After: Logger object destructor.")

log = Logger()
del log
