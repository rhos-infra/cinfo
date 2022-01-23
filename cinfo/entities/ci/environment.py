# Copyright 2022 Red Hat
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
import numbers
from cinfo.system import System


# encapsulates 
#    1. system objects. examples of system objects are Jenkins and Zuul 
#    2. provides interface to add/get the system by system name 

# attributes
#    1. name 

class Environment(object):

    def __init__(self, name: str, 
        # e.g "OSP Component Pipeline", "TripleO CI", "OSP Phase 3"
        self.name = name

        self.system = System.get_system(system)
        self.url = url

        self.name = 
        self.driversMap = {'jobs': Jenkins,
                           'builds': Jenkins,
                           'stages': Jenkins}
                           
        backend: netapp
        image: glance over cinder 

--backend netapp --image glance_over_cinder

Jenkins -> jobs, stages, ...
Zuul -> ...
Build -> number
Stage -> status, name

cinfo --stages --domain tripleo_ci

   
    def AddDriver(driverDunctionalityName: str:, driver: Driver) -> bool

   