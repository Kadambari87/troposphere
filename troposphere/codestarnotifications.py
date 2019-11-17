# Copyright (c) 2012-2019, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 8.1.0


from . import AWSObject
from . import AWSProperty


class Target(AWSProperty):
    props = {
        'TargetAddress': (basestring, False),
        'TargetType': (basestring, False),
    }


class NotificationRule(AWSObject):
    resource_type = "AWS::CodeStarNotifications::NotificationRule"

    props = {
        'DetailType': (basestring, True),
        'EventTypeIds': ([basestring], True),
        'Name': (basestring, True),
        'Resource': (basestring, True),
        'Status': (basestring, False),
        'Tags': (dict, False),
        'Targets': ([Target], True),
    }