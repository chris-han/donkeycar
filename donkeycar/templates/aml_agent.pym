#!/usr/bin/env python3

import azureml.core
from azureml.core import Workspace, Datastore

# Check core SDK version number
print("SDK version:", azureml.core.VERSION)

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')

def_file_store = Datastore(ws, "workspacefilestore")
print("Default datastore's name: {}".format(def_file_store.name))

def_file_store.upload ("./tub", target_path = "./tub", overwrite = True, show_progress = True)
