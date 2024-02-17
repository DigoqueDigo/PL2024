import re as regex


class Parser:

    def __init__(self):
        self.functions = list()


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