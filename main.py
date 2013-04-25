#!/usr/bin/env python
#
# Copyright 2013 Avleen Vig
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import random

def bdfacts():
    """Random BD Facts generator"""
    random.seed()
    bdstrings = [
        ['Postcode',
         'Zipcode',
         'Gender',
         'Political affiliation',
         'Religion',
         'Web site',
         'Database',
         '.zshrc',
         'Arrest warrant'],
        ['changed?',
         'switched?',
         'replaced?',
         'ruined?',
         'destroyed?',
         'fucked up beyond all recognition?',
         'no longer relevant?'],
        ['Call BD',
         'BD needs a banana',
         'Find BD',
         'BD puts on his robe and wizard hat',
         'It\'s time for BD',
         'BD needs some Punjabi Deli',
         'BD did it',
         'BD entered the room',
         'BD fell asleep',
         'BD orders a MacAllan',
         'BD is about to speak'],
        ['shit\'s going down',
         'government is about to get bailed out',
         'problem solved',
         'laws of physics no longer apply',
         'samosas for everyone',
         'someone order a whiteboard from reception, stat',
         'before we end up in the Bronx']
    ]
    choices = tuple(random.choice(fact) for fact in bdstrings)
    quote = '%s %s <br>- %s, %s.' % choices
    return quote

class MainHandler(webapp.RequestHandler):
    def get(self):
        page = """
<html>
    <head>
        <title>Brown Dynamite Facts Generator</title>
    </head>
    <body>
        <center>
            <h1 style="margin-left: 100px; margin-right: 100px">"%s"</h1>
        </center>
        <p></p>
        <center>
            <p><a href="/">Get a new fact!</a></p>
        </center>
        <p></p>
        <p></p>
        <p style="font-family: sans-serif; font-size: 12px; margin: 50px">
        My friends call me, <b><i>Brown Dynamite</i></b><br><br>
        </p>
    </body>
</html>""" % bdfacts()
        self.response.out.write(page)


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
