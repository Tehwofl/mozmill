#!/usr/bin/env python

# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is MozMill automation code.
#
# The Initial Developer of the Original Code is the Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Henrik Skupin <hskupin@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import optparse
import os
import sys

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_path, 'libs'))

from testrun import BftTestRun, UpdateTestRun

def main():
    """ Main function for all available test-runs. """

    usage = "usage: %prog [options] (binary|folder)"
    parser = optparse.OptionParser(usage=usage, version="%prog 0.1")
    parser.add_option("--channel",
                      choices=[None, "nightly", "betatest", "beta",
                               "releasetest", "release"],
                      default=None,
                      dest="channel",
                      help="Update channel",
                      metavar="CHANNEL")
    parser.add_option("--logfile",
                      dest="logfile",
                      metavar="PATH",
                      help="Path to the log file")
    parser.add_option("--no-fallback",
                      action="store_true",
                      default=False,
                      dest="no_fallback",
                      help="Do not perform a fallback update")
    parser.add_option("--report",
                      dest="report",
                      metavar="URL",
                      help="Send results to the report server")
    (options, binaries) = parser.parse_args()

    # Run software update tests
    update = UpdateTestRun()
    update.binaries = binaries
    update.channel = options.channel
    update.logfile = options.logfile
    update.no_fallback = options.no_fallback
    update.report_url = options.report
    update.run()

    # Run BFT tests
    bft = BftTestRun()
    bft.binaries = binaries
    bft.logfile = options.logfile
    bft.report_url = options.report
    bft.run()

if __name__ == "__main__":
    main()