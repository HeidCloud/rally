# Copyright 2013: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally.deploy import engine
from rally import objects


class DummyEngine(engine.EngineFactory):
    """DummyEngine doesn't deploy OpenStack it just use existing.

       To use DummyEngine you should put in a config endpoint key, e.g:

            {
                "name": "DummyEngine",
                "endpoint": {
                    "auth_url": "http://localhost:5000/v2.0/",
                    "username": "admin",
                    "password": "password",
                    "tenant_name": "demo"
                }
            }

    """

    CONFIG_SCHEMA = {
        'type': 'object',
        'properties': {
            'endpoint': {
                'type': 'object',
                'properties': {
                    'auth_url': {'type': 'string'},
                    'username': {'type': 'string'},
                    'password': {'type': 'string'},
                    'tenant_name': {'type': 'string'},
                },
                'required': ['auth_url', 'username', 'password',
                             'tenant_name'],
            },
        },
        'required': ['endpoint'],
    }

    def deploy(self):
        endpoint = self.deployment['config']['endpoint']
        return objects.Endpoint(auth_url=endpoint['auth_url'],
                                username=endpoint['username'],
                                password=endpoint['password'],
                                tenant_name=endpoint['tenant_name'])

    def cleanup(self):
        pass
