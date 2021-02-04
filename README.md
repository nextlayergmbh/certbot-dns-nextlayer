certbot-dns-nextlayer
============

![Tests](https://github.com/nextlayergmbh/certbot-dns-nextlayer/workflows/Tests/badge.svg)
![Upload Python Package](https://github.com/nextlayergmbh/certbot-dns-nextlayer/workflows/Upload%20Python%20Package/badge.svg)
[![Python Version](https://img.shields.io/pypi/pyversions/certbot-dns-nextlayer)](https://pypi.org/project/certbot-dns-nextlayer/)
[![PyPi Status](https://img.shields.io/pypi/status/certbot-dns-nextlayer)](https://pypi.org/project/certbot-dns-nextlayer/)
[![Version](https://img.shields.io/github/v/release/nextlayergmbh/certbot-dns-nextlayer)](https://pypi.org/project/certbot-dns-nextlayer/)

next layer DNS Authenticator plugin for [Certbot](https://certbot.eff.org/).

This plugin is built from the ground up and follows the development style and life-cycle
of other `certbot-dns-*` plugins found in the
[Official Certbot Repository](https://github.com/certbot/certbot).

Installation
------------

```
pip install --upgrade certbot # optional
pip install certbot-dns-nextlayer
```

Verify:

```
$ certbot plugins --text

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
* dns-nextlayer
Description: Obtain certificates using a DNS TXT record by using the nextlayer
dns api.
Interfaces: IAuthenticator, IPlugin
Entry point: dns-nextlayer = certbot_dns_nextlayer.dns_nextlayer:Authenticator

...
...
```

Configuration
-------------

The credentials file e.g. `~/nldns-credentials.ini` should look like this:

```
dns_nextlayer_token=put_your_token_here
```

Usage
-----


```
certbot certonly --authenticator dns-nextlayer --dns-nextlayer-credentials=~/nldns-credentials.ini -d nextlayer.at
```
