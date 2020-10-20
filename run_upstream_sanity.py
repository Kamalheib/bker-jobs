#!/usr/bin/env python

import os

job_list = [
"bnxt-roce-upstream.xml",
"cxgb4-iw-upstream.xml",
"hfi1-opa-upstream.xml",
"mlx4-ib-upstream.xml",
"mlx4-roce-upstream.xml",
"mlx5-ib-upstream.xml",
"mlx5-roce-upstream.xml",
"qedr-iw-upstream.xml"]

for job in job_list:
    os.system("bkr job-submit %s" % (job))
