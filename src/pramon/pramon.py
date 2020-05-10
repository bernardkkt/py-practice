#!/usr/bin/env python3
import pradec
import hashlib

@log
def createHash(self):
    if self.decoded:
        return hashlib.md5(self.decoded).hexdigest()
    else:
        raise ValueError("Not expecting self.decoded to be empty")