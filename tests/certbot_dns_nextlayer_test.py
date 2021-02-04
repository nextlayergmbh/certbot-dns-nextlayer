import unittest

try:
    import mock
except ImportError:  # pragma: no cover
    from unittest import mock  # type: ignore

from certbot.compat import os
from certbot.plugins import dns_test_common, dns_test_common_lexicon
from certbot.tests import util as test_util
from requests.exceptions import HTTPError

TOKEN = "not42charslong"


class AuthenticatorTest(
    test_util.TempDirTestCase, dns_test_common_lexicon.BaseLexiconAuthenticatorTest
):
    def setUp(self):
        super(AuthenticatorTest, self).setUp()

        from certbot_dns_nextlayer.dns_nextlayer import Authenticator

        path = os.path.join(self.tempdir, "file.ini")
        dns_test_common.write({"nextlayer_token": TOKEN}, path)

        self.config = mock.MagicMock(
            nextlayer_credentials=path, nextlayer_propagation_seconds=0
        )  # don't wait during tests

        self.auth = Authenticator(self.config, "nextlayer")

        self.mock_client = mock.MagicMock()
        self.auth._get_nldns_client = mock.MagicMock(return_value=self.mock_client)


class NextlayerLexiconClientTest(
    unittest.TestCase, dns_test_common_lexicon.BaseLexiconClientTest
):

    LOGIN_ERROR = HTTPError("401 Client Error: Unauthorized for url: ...")

    def setUp(self):
        from certbot_dns_nextlayer.dns_nextlayer import _NLDNSLexiconClient

        self.client = _NLDNSLexiconClient(TOKEN)

        self.provider_mock = mock.MagicMock()
        self.client.provider = self.provider_mock


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
