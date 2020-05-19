#!/usr/bin/env python

import os

jobs_list = [
"bnxt-roce-pyverbs.xml",
"cxgb4-iw-pyverbs.xml",
"hfi1-opa-pyverbs.xml",
"mlx4-ib-pyverbs.xml",
"mlx4-roce-pyverbs.xml",
"mlx5-ib-pyverbs.xml",
"mlx5-roce-pyverbs.xml",
"qedr-iw-pyverbs.xml"]

for job in jobs_list:
    cmd = "bkr job-submit %s" % job
    os.system(cmd)

