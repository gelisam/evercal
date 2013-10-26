#!/usr/bin/python
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
from datetime import date
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
from evernote.edam.notestore import NoteStore

from evernote.api.client import EvernoteClient


def getUserShardId(authToken, userStore):
  """
  Get the User from userStore and return the user's shard ID
  """
  try:
    user = userStore.getUser(authToken)
  except (Types.EDAMUserException, Types.EDAMSystemException), e:
    raise "Exception while getting user's shardId: %s %s" % (type(e), e)
  
  if hasattr(user, 'shardId'):
    return user.shardId
  raise "no shardId found"


# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://sandbox.evernote.com/api/DeveloperToken.action
auth_token = open("dev_token", "r").read().rstrip()


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
if not version_ok:
  raise "Evernote API too old"

note_store = client.get_note_store()
shardId = getUserShardId(auth_token, user_store)

# we are interested in notes tagged as a "post"
filter = NoteStore.NoteFilter()
filter.words = "tag:post"

# we are interested in their titles
spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
spec.includeAttributes = True

# find them notes!
noteList = note_store.findNotesMetadata(auth_token, filter, 0, 40, spec)

print "Content-type: application/json\r\n"
print "["
first = True
for note in noteList.notes:
  date = date.fromtimestamp(note.attributes.reminderTime / 1000)
  url = "https://sandbox.evernote.com/Home.action?#st=p&n=%s" % note.guid
  thumbnail = "https://sandbox.evernote.com/shard/%s/thm/note/%s" % (shardId, note.guid)
  if first:
    first = False
  else:
    print ','
  print '{date: "%s", url: "%s", thumbnail: "%s"}' % (date, url, thumbnail)
print "]"
