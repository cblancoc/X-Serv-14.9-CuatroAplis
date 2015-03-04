#!/usr/bin/python
# -*- coding: utf-8 -*-


class suma:

    def __init__(self):
        self.saved = None

    def parse(self, request, rest):
        try:
            print rest
            numero = int(rest[1:])
        except ValueError:
            return None
        return numero

    def process(self, parsedRequest):
        if not parsedRequest:
            return ("400 Bad Request", "Error 404. Page not found")

        if self.saved:  # Atributo para q siga exstiendo si acaba la funcion
            result = self.saved + parsedRequest
            self.saved = 0
        else:
            result = "Dame otro número"
            self.saved = parsedRequest

        return("200 OK", "<html><body>" + str(result) +
               "</body></html>" +
               "\r\n")
