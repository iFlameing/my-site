"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "my_site"

_ = MessageFactory("my_site")

logger = logging.getLogger("my_site")
