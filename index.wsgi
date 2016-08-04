#utf-8

import sae

import urlparse

import xml.etree.ElementTree as ET

def app(environ, start_response):

    status = '200 OK'

    response_headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, response_headers)

    method=environ['REQUEST_METHOD']

    if method=="GET":

        query=environ['QUERY_STRING']

        echostr=urlparse.parse_qs(query)['echostr']

        return echostr

    elif method=="POST":

        post=environ['wsgi.input']        

        root = ET.parse(post)

        fromUser=root.findtext(".//FromUserName")

        toUser=root.findtext(".//ToUserName")

        CreateTime=root.findtext(".//CreateTime")

        texttpl='''<xml>

        <ToUserName>'''+fromUser+'''</ToUserName>

        <FromUserName>'''+toUser+'''</FromUserName>

        <CreateTime>'''+CreateTime+'''</CreateTime>

        <MsgType><![CDATA[text]]></MsgType>

        <Content><![CDATA[hello]]></Content>

        </xml>'''

        return texttpl

application = sae.create_wsgi_app(app)