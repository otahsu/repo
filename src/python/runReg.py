#!/usr/bin/env python2.7

import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
if __name__ == "__main__":
    if os.getenv("REG_ROOT"):
        from gripy.regression import Regression, default_runtime
        if default_runtime.yaml_list:
            for i in default_runtime.yaml_list:
                reg = Regression(i)
                reg.run()
            default_runtime.status_report()
        elif default_runtime.yaml_list == []:
            default_runtime.echo("No match yaml file.\n")
    else:
        import sys
        sys.stdout.write('Please set environment variable REG_ROOT =\
        */reg_griffey\n')

# vim: set ft=python ff=unix fenc=utf8 ai et nu sw=4 ts=4 tw=79:
