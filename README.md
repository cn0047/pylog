PyLog
-

[![Build Status](https://travis-ci.org/cn007b/log.svg?branch=master)](https://travis-ci.org/cn007b/log)
[![Maintainability](https://api.codeclimate.com/v1/badges/3c0a922e2eb162a3ff4e/maintainability)](https://codeclimate.com/github/cn007b/pylog/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/cn007b/pylog/badge.svg?branch=master)](https://coveralls.io/github/cn007b/pylog?branch=master)

Python package for [REAL-TIME log](https://realtimelog.herokuapp.com/) ([cn007b/log](https://github.com/cn007b/log)).

## Installation

`pip3 install realtimelog`

## Usage

````py
from realtimelog import Client

c = Client()
# Please open provided link in browser.
print('Open: ', c.get_url())
# Now you can post log and see it immediately in dashboard.
c.msg({'code': 200, 'message': 'It works!'})
````
