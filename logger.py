import logging
import functools

def create_log():
    logger = logging.getLogger('__name__')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(r'logging.log')

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def log_exception(func):
    @functools.wraps(func)
    def logwork(*args,**kwargs):
        logger = create_log()
        try:
            func(*args,**kwargs)
        except:
            
            err = 'Exception at ' + func.__name__
            logger.exception(err)

            raise
    return log


@log_exception
def test_func():
    print(i)

if __name__ == "__main__":
    test_func()
        
