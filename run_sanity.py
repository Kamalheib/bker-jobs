#!/usr/bin/env python

import os

job_list = [
"bnxt-roce.xml",
"cxgb4-iw.xml",
"hfi1-opa.xml",
"mlx4-ib.xml",
"mlx4-roce.xml",
"mlx5-ib.xml",
"mlx5-roce.xml",
"qedr-iw.xml"]


whit_board = ""
kernel_rpm = ""
core_rpm = ""
modules_rpm = ""
distro_name = "RHEL-8.4.0-20210331.d.2"

for job in job_list:
    os.system("sed -i 's,| RDMA sanity <,| RDMA sanity | %s<,g' %s" % (whit_board, job))
    os.system("sed -i 's,URL_K=\"\",URL_K=\"%s\",g' %s" % (kernel_rpm, job))
    os.system("sed -i 's,URL_C=\"\",URL_C=\"%s\",g' %s" % (core_rpm, job))
    os.system("sed -i 's,URL_M=\"\",URL_M=\"%s\",g' %s" % (modules_rpm, job))
    os.system("sed -i 's,<distro_name op=\"=\" value=\"\"/>,<distro_name op=\"=\" value=\"%s\"/>,g' %s" % (distro_name, job))
    os.system("bkr job-submit %s" % (job))
