#!/usr/bin/python
# -*- coding: utf-8 -*-


class hola:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 OK", "<html><body>Hola. " +
               "</body></html>" +
               "\r\n")


class adios:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 OK", "<html><body>Adios. " +
               "</body></html>" +
               "\r\n")
