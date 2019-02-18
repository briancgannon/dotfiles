#!/usr/bin/env python

# Horribly overblown profile switcher for manually managing multiple AWS profiles

import argparse
import glob
import os
import sys
from pathlib2 import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description="Does some awesome things.")
parser.add_argument('message', type=str, help="pass a message into the script")

def file_mover(profile):
    if profile == "profile_01":

        config_src = "/Users/username/.aws/bak/config.profile_01"
        config_dest = "/Users/username/.aws/config"

        creds_src = "/Users/username/.aws/bak/credentials.profile_01"
        creds_dest = "/Users/username/.aws/credentials"

        copyfile(config_src, config_dest)
        copyfile(creds_src, creds_dest)

    elif profile == "profile_02":

        config_src = "/Users/username/.aws/bak/config.profile_02"
        config_dest = "/Users/username/.aws/config"

        creds_src = "/Users/username/.aws/bak/credentials.profile_02"
        creds_dest = "/Users/username/.aws/credentials"

        copyfile(config_src, config_dest)
        copyfile(creds_src, creds_dest)

    elif profile == "blank":

        config_src = "/Users/username/.aws/bak/config.blank"
        config_dest = "/Users/username/.aws/config"

        creds_src = "/Users/username/.aws/bak/credentials.blank"
        creds_dest = "/Users/username/.aws/credentials"

        copyfile(config_src, config_dest)
        copyfile(creds_src, creds_dest)

    else:

        config_src = "/Users/username/.aws/bak/config.profile_default"
        config_dest = "/Users/username/.aws/config"

        creds_src = "/Users/username/.aws/bak/credentials.profile_default"
        creds_dest = "/Users/username/.aws/credentials"

        copyfile(config_src, config_dest)
        copyfile(creds_src, creds_dest)


if __name__ == '__main__':
    # Get args 
    args = parser.parse_args(sys.argv[1:])
    active_profile = args.message
    
    # move cred files into place
    file_mover(active_profile)
    print("Active AWS Profile:  %s" % (active_profile))

    # write active profile to file
    file_list = glob.glob('/Users/username/.aws/aws.active.profile.*')
    for profile in file_list:
        try:
            os.remove(profile)
        except:
            print("Error while deleting file : ", profile)
    
    Path('/Users/username/.aws/aws.active.profile.%s' % (active_profile)).touch()

    
    

