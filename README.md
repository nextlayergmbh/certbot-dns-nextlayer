certbot-dns-nextlayer
============

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
