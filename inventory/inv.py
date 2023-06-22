#!/usr/bin/env python
import json
import argparse
'''
run with:
`ansible-playbook all -i ./inventory/inv.py <command>`
For example:
`ansible-playbook all -i ./inventory/inv.py -m ping`
'''
class Inventory(object):
    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        if self.args.list:
            self.inventory = self.default_inventory()
        elif self.args.host:
            # not implemented, since we return _meta info `--list`
            self.inventory = self.empty_inventory()
        else:
            # If no groups or vars are present, return an empty inventory.
            self.inventory = self.empty_inventory()
        print(json.dumps(self.inventory))

    def default_inventory(self):
        return {
            'prodgeek': {
                'hosts': [
                    '10.100.10.21',
                ],
                'vars': {
                    'ansible_ssh_user' : 'user'
                }
            },
            '_meta' : {
                'hostvars': {}
            }
        }

    def empty_inventory(self):
        return { '_meta': {'hostvars': {}}}

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

Inventory()