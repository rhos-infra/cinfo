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

class Job(object):

    def __init__(self, builds = [], configuration=None):

        self.builds = builds
        self.configuration = configuration


class JobList(list):

    def __init__(self, iterable=None):
        super(JobList, self).__init__()
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, item):

        if isinstance(item, Job):
            super(JobList, self).append(item)
        else:
            raise ValueError('Jobs allowed only')
