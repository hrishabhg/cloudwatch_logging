from django.conf import settings
import logging

__author__ = 'Hrishabh Gupta<hrishabhg@gmail.com>'
__version__ = '1.0.2'


class CloudWatchHandler(logging.Handler):
    def emit(self, record):
        print record
        print getattr(settings, 'CLOUDWATCH_AWS_ACCESS_KEY', '---')
        pass
