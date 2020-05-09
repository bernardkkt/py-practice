#!/usr/bin/env python3
import logging
import base64

#logging.basicConfig(level=logging.INFO)
logging.debug("Patihan")


def log(func):
    def _exec(*args, **kwargs):
        logger = logging.getLogger('decorator-log')
        try:
            logger.info("Running **{}**".format(func.__name__))
            return func(*args, **kwargs)
        except:
            logger.error("Error encountered at function **{}**".format(func.__name__))
            raise

    return _exec


class Hashes:
    def __init__(self):
        self.logger = logging.getLogger('decorator-log')
        self.logger.setLevel(logging.INFO)

    class Base64:
        encoded = ''
        decoded = ''

        @log
        def decode(self):
            if self.encoded:
                # Do text decoding
                return base64.b64decode(self.encoded)
            else:
                raise ValueError("Not expecting self.encoded to be empty")

        @log
        def encode(self):
            if self.decoded:
                # Do text encoding
                return base64.b64encode(self.decoded)
            else:
                raise ValueError("Not expecting self.decoded to be empty")


def main():
    sane = Hashes().Base64()
    sane.encoded = 'dfmsfbjksrhn='
    sane.decode()
    sane.encode()
    return


if __name__ == "__main__":
    main()
