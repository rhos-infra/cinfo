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
from html.entities import entitydefs
import numbers
from cinfo.entities.ci.job import Job
from cinfo.system import System


class OSP_ELK():

    def query(entity):

        # ELK implementation
        if entity.jobs == ...:
          query = query + {jobs: ...}
        if entity.pipelines == ...:
            query = query + {pipelines: ...}

        entity.system.jobs.append(Job(..))


console_output:
- logstash: job -> x, build_number-> 2, line: "started by timer" -> {'job': x, "builder_number": 2, "trigger": "timer"}
- logstash: job -> x, build_number-> 2, line: "TASK NAME: ..." -> {'job': x, "builder_number": 2, "task_name": "..."}
-
-

trigger: time + task_name: ...

{trigger: time}

map = { 'jobx': {trigger: time}}

{task_name: ...}

map = {'jobx': {trigger, task_name}}

entity.system.jobs.append(Job(..))

class Query(object):

    def __init__(self):
        data = {}
        self.entities = entities
        for entity in entities:
            sources = collect_sources(entity)
            sort_by_priority(self.sources)
            for source in self.sources:
                data[source] = source.query(entitiy)
        for entity in entities:
            aggreagte_data(data)

class JenkinsSystem():
     self.jobs = ListValue(name='jobs', type=Job, expose=False)
     self.sources = [OSP_ELK(...), JJB(...), self]

     def print():
         for job in self.jobs:
             job.print()

class JenkinsJob():
     self.name = Value(name='jobs', type=str, expose=True, exposed_name='jobs')

     def print():
         for test in self.tests:
             test.print()

class Zuul():
    self.pipelines = ListValue(name='pipelines', type=Pipeline, expose=True)

class Pipeline():
    self.jobs = ListValue(name='pipelines', type=Job, expose=True, exposed_name='--zuul-pipeline')
     
class Environment(CiEntity):
    systems = System

    def __init__(self, name: str, 
        # e.g "OSP Component Pipeline", "TripleO CI", "OSP Phase 3"
        
        self.name = Value(name='name', type=str, nargs=1, expose=True)
        self.systems = ListValue(name='systems', type=System, nargs=*)
        self.some_dict_attribute = DictValue(name='systems', key_type=System,
                                             value_type=str, nargs=*)

        # def set_args(self, parser):
        #     parser.add_argument('name', type=str, nargs=1)
        #     parser.add_argument('systems', type=str, nargs=*)

        #     1. Environment().Systems - scan per entity
        #     2. Get parser from each file in specific directory

        #     for e in entities: 
        #         e.set_args(parser)

# Main Workflow
# ========
# cinfo query

parser = Parser()
config = load_configuration
entities = [Environment(systems=[System(...), System(...)]), Environment()]
update_parser(Parser, entities)

def update_parser(parser, entities):
    for entity in entities:
        for attribute in entity.attributes:
            set_arguments(parser, entity)

def set_arguments(parser, entity):
       if entity isinstance of Value and entity.expose=True:
       for attribute in entity:
           set_arguments(attribute)    

Environment. 
    name -> Value? Value.expose? add --environment-name to parser
    systems -> Value? Value.expose? add --systems to parser
      name -> Value? Value.expose? add --system-name to parser
      


              |   |
              |   |
              |   v
              |   self.name -> Value? -> Value.expose? -> is argument exists already in parser ? no? -> parser.set_argument(type, nargs, ...)
              |     |
              |     v 
              |     X
              |
              self.system -> Value? -> Value.expose? -> is argument exists already in parser? no? -> parser.set_argument(type)
              |
              v
              self.name  -> Value? ...


Parser.update(entities)

def update(entities=[]):
    for entity in entities:


def set_arguments(entity):
   if entity isinstance of Value and entity.expose=True:
       for attribute in entity:
           set_arguments(attribute)    


Environment -> Zuul System -> Pipeline -> Jobs -> Roles
Environment -> Jenkins System -> Jobs -> Stages