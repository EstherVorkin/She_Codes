#!/usr/bin/env python3

import os
import sys
import re
import time
import PyPDF2
import csv


def getPageCount(pdf_file):
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    pages = pdfReader.numPages
    return pages


def extractData(pdf_file, page):
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data


def getWordCount(data):
    data = data.split()
    return len(data)


def main1():
    pdfFile = open('meetingminutes.pdf', 'rb')
    totalWords = 0
    numPages = getPageCount(pdfFile)
    for i in range(numPages):
        text = extractData(pdfFile, i)
        totalWords += getWordCount(text)
    time.sleep(1)

    print(totalWords)

def main2():
    with open('example3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_counter = 0
        for row in csv_reader:
            if line_counter == 0:
                print(f'Column names are {",".join(row)}')
                line_counter += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department and was born in {row[2]}.')
                line_counter += 1
        print(f'Proccessed {line_counter} lines.')

if __name__ == '__main__':
    os.chdir('C:\\Users\\Esther\\Desktop\\example')
    #main1()
    main2()