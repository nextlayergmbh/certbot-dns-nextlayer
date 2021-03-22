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

### Example command

```
certbot certonly --authenticator dns-nextlayer --dns-nextlayer-credentials=~/nldns-credentials.ini -d nextlayer.at
```

### Zone detection method

We've added the configuration parameter `--dns-nextlayer-method` to select the way our certbot plugin determines the correct zone to add the record to. Currently there are 3 options you can choose from.

#### `intelligent`

This is the default method.  
It tries to determine the zone intelligently by extracting the TLD and re-adding the first level.

##### Examples:
```
* dns.nextlayer.at: nextlayer.at
* dns.nextlayer.co.at: nextlayer.co.at
* www.dns.nextlayer.co.at: nextlayer.co.at
```

#### `remove-first`

This method just removes the first level of the requested domain.

##### Examples:
```
* dns.nextlayer.at: nextlayer.at
* dns.nextlayer.co.at: nextlayer.co.at
* www.dns.nextlayer.co.at: dns.nextlayer.co.at
```

#### `none`

This method does what it's called. No magic.

##### Examples:
```
* dns.nextlayer.at: dns.nextlayer.at
* dns.nextlayer.co.at: dns.nextlayer.co.at
* www.dns.nextlayer.co.at: www.dns.nextlayer.co.at
```
