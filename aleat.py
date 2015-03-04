#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class aleat:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        rand_num = random.randrange(1000000)
        return ('200 OK',
                "<html><body>Hola. " +
                "<a href='/aleat/" + str(rand_num) +
                "'>Dame otra</a>" +
                "</body></html>" +
                "\r\n")
