#
# A simple Evernote API demo script that lists all notebooks in the user's
# account and creates a simple test note in the default notebook.
#
# Before running this sample, you must fill in your Evernote developer token.
#
# To run (Unix):
#   export PYTHONPATH=../../lib; python EDAMTest.py
#

import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = open("dev_token", "r").read().rstrip()

if auth_token == "your developer token":
  print "Please fill in your developer token"
  print "To get a developer token, visit " \
    "https://sandbox.evernote.com/api/DeveloperToken.action"
  exit(1)

# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
client = EvernoteClient(token=auth_token, sandbox=True)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
  "Evernote EDAMTest (Python)",
  UserStoreConstants.EDAM_VERSION_MAJOR,
  UserStoreConstants.EDAM_VERSION_MINOR
)
print "Is my Evernote API version up to date? ", str(version_ok)
print ""
if not version_ok:
  exit(1)

note_store = client.get_note_store()

# get the default notebook
default_notebook = None
for notebook in note_store.listNotebooks():
  if notebook.defaultNotebook:
    default_notebook = notebook

if not default_notebook:
  raise "could not find the default notebook"
