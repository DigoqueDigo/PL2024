import re as regex


class Parser:

    def __init__(self):
        self.buffer = str()
        self.functions = list()


    def setParser(self):
        self.functions.append(self.parseParagraph)
        self.functions.append(self.parseHeader)
        self.functions.append(self.parseBold)
        self.functions.append(self.parseItalic)
        self.functions.append(self.parseImage)
        self.functions.append(self.parseLink)
        self.functions.append(self.parseItem)


    def parseHeader(self,text):
        return regex.sub(
            r'^(#{1,6})\s(.+)',
            lambda match: fr'<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>',
            text)


    def parseBold(self,text):
        return regex.sub(
            r'\*{2}((?=\w)[^\*]*\w)\*{2}',
            lambda match: fr'<b>{match.group(1)}</b>',
            text)


    def parseItalic(self,text):
        return regex.sub(
            r'\*((?=\w)[^\*]*\w)\*',
            lambda match: fr'<i>{match.group(1)}</i>',
            text)


    def parseLink(self,text):
        return regex.sub(
            r'\[([^\]]+)\]\(([^\)\s]+)\)',
            lambda match: fr'<a href="{match.group(2)}">{match.group(1)}</a>',
            text)


    def parseImage(self,text):
        return regex.sub(
            r'!\[([^\[]*)]\(([^\)\s]+)\)',
            lambda match: fr'<img src="{match.group(2)}" alt="{match.group(1)}"/>',
            text)


    def parseItem(self,text):
        return regex.sub(
            r'^\d+\.\s(.+)',
            lambda match: fr'<li>{match.group(1)}</li>',
            text)


    def parseParagraph(self,text):
        if text == self.parseHeader(text) and text == self.parseItem(text):
            text = '<p>' + text + '</p>'
        return text


    def parseLine(self,text):
        for function in self.functions:
            text = function(text)
        self.buffer += text + '\n'


    def refactoryHTML(self):
        return regex.sub(
            r'(<li>.*<\/li>[\n\s]*)+',
            lambda match: fr'<ol>{match.group(0)}</ol>',
            self.buffer).strip("\n ")