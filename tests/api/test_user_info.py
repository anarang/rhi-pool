import json
import logging
import unittest
from insights.session import Session
from insights.configs import settings
from insights.utils.util import Util
from insights.utils.api_resources import me, account_products

LOGGER = logging.getLogger('insights_api')


class UserInfoAPI(unittest.TestCase):
    def setup_class(self):
        session_instance = Session()
        self.session = session_instance.get_session()
        self.base_url = settings.api.url

    def setup_method(self, method):
        Util.print_testname(type(self).__name__, method)

    def test_current_user_info(self):
        """ Request current user information
        """
        self.user_info = self.session.get(self.base_url + me)
        LOGGER.info(self.user_info.json())
        Util.log_assert(self.user_info.status_code == 200,
                        "Response is not 200 OK")
        self.text = self.user_info.text
        response = json.loads(self.text)
        account_number = response['account_number']
        Util.log_assert(account_number == str(477931), "Account number is incorrect")

    def test_product_used_by_account(self):
        """ Test products used by this current user
        """
        self.product = self.session.get(self.base_url + account_products)
        LOGGER.info(self.product.json())
        Util.log_assert(self.product.status_code == 200,
                        "Response is not 200 OK")
        product_info = json.loads(self.product.text)
        product_used = product_info[0]
        Util.log_assert(product_used == 'rhel', "Product used is not RHEL")
