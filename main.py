import pandas as pd
from pybatfish.client.commands import *
from pybatfish.datamodel import *
from pybatfish.datamodel.answer import *
from pybatfish.datamodel.flow import *
from pybatfish.question import *
from pybatfish.question import bfq


bf_set_network('optimity')

SNAPSHOT_DIR = '~/mnt/c/Users/sazzo/OneDrive\ -\ Optimity\ Ltd/configs/oxidized/'
bf_init_snapshot(SNAPSHOT_DIR, name='snapshot-2021-02-07', overwrite=True)

load_questions()

bfq.initIssues().answer()