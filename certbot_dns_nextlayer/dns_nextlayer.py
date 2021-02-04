"""DNS Authenticator for nextlayer."""

import logging

import tldextract
import zope.interface
from certbot import interfaces
from certbot.plugins import dns_common, dns_common_lexicon
from lexicon.config import ConfigResolver
from lexicon.providers import powerdns
from requests.api import request

logger = logging.getLogger(__name__)
logging.getLogger(tldextract.__name__).setLevel(logging.WARNING)
logging.getLogger("filelock").setLevel(logging.WARNING)


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """
    DNS Authenticator for nextlayer dns api.
    This Authenticator uses the nextlayer dns api to fulfill a dns-01 challenge.
    """

    description = (
        "Obtain certificates using a DNS TXT record by using the nextlayer dns api."
    )

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):
        super(Authenticator, cls).add_parser_arguments(
            add, default_propagation_seconds=60
        )
        add("credentials", help="nextlayer dns credentials ini file.")

    def more_info(self):
        return """
            This plugin configures a DNS TXT record to respond to a dns-01 challenge using
            the nextlayer DNS API
            """

    def _setup_credentials(self):
        dns_common.validate_file_permissions(self.conf("credentials"))
        self.credentials = self._configure_credentials(
            "credentials",
            "nextlayer dns credentials ini file",
            {"token": "nextlayer dns api key"},
        )

    def _extract_domain(self, domain, validation_name):
        ext = tldextract.extract(domain)
        zone = ".".join(ext[-2:])
        return {"domain": zone, "validation_name": validation_name}

    def _get_nldns_client(self):
        return _NLDNSLexiconClient(token=self.credentials.conf("token"))

    def _perform(self, domain, validation_name, validation):
        res = self._extract_domain(domain, validation_name)
        self._get_nldns_client().add_txt_record(
            res["domain"], res["validation_name"], validation
        )

    def _cleanup(self, domain, validation_name, validation):
        res = self._extract_domain(domain, validation_name)
        self._get_nldns_client().del_txt_record(
            res["domain"], res["validation_name"], validation
        )


class _NLDNSLexiconClient(dns_common_lexicon.LexiconClient):
    def __init__(self, token):
        config = {
            "provider_name": "powerdns",
            "ttl": 60,
            "powerdns": {
                "pdns_server": "https://dns.nextlayer.at/",
                "pdns_server_id": "localhost",
                "auth_token": token,
            },
        }

        lexicon_config = ConfigResolver().with_dict(config)
        self.provider = powerdns.Provider(lexicon_config)
