# Main Workflow
# ========
# cinfo query --jobs DFG-network-1

from re import X
from unicodedata import name

========================================== 1 =============================================================================
# cinfo query -> main.py(arguments_from_cli) -> user_arguments = [{key: value}, {key: value}]
config = load_configuration # cinfo.yaml
hierarchy_of_entities = []
for each supported Driver create an instance so that the 

supported_drivers = []
for driver in drivers:
      supported_drivers.append(Driver(environments=[Environment, Environment, ...]
========================================== 2 =============================================================================
for env in config['environments']:
      hierarchy_of_entities.append(Environment(env))
# We have hirerachy of entity types built in such a manner that reflects relations between entities:
# Environment -> 
#                System ->
#                          Sources = [Driver(), Driver(), Driver()]
#                          Jobs    = ListValue()
# We are assinging entity attributes with Value(populate=False, env=Environment...)
========================================== 3 =============================================================================
# traverse the hirerachy, during the traversal each entity in the hierarchy is adding supported arguments to argparser 
# Value.populate=True
# Return Argument(Value.exposed_name, ...) 
parser = Parser() # empty parser
update_parser_with_arguments(parser, hierarchy_of_entities)
# Parser = [
#  {name=argument1, dest=exposed_name},
#  {name=argument2, dest=exposed_name}
# ]
========================================== 4 =============================================================================
# Match arguments delivered from the user with those that were collected 
# in case of error (e.g. user passed non existing argument) raise exception
# in case of math contunue to the execution 
arguments = parser.parse_arguments(user_arguments) # agrparser function
# arguments = {'system-name': 'jenkins',
#              'jobs': ['a', 'b', 'c']
#             }

========================================== 4 =============================================================================
Query traversal 

Environment -> 
                
                System ->
                          Sources = ...
                              JenkinsDriver(Credentails(conffile))
                          Jobs    = ListValue()
                               -> [
                                    Job
                                    Job
                                    Job
                                       -> Tests
                                  ]
# Option 1 
# ========

class DriverFactory():
      
      def get(arrribue: Attribute):
            

traversal_on_all_entities():
   if entity.attribute != populated:
         # driver is a class of the driver according to the prrio from configuration file that is suited to retrive attribute related info
         driver = DriverFactory.get(entity.attribute) 
         driver_instance = driver(Crendentails)
            
            

Argument(arg: string, entity: CiEntitry)
    
JenknsDriver(Crendentails)
     jobs_list = issueQuesry(Argument(jobsRegex), Job)



# Option 2
# ========
# arguments = {...}
for env in entities:
      for source in env.sources: # env.sources is a list of sources listed by priority
            updated_env = source.update_entities(env) # update current environment with its sources
            if is_all_arguments_populated(entities):
                  break
      
class OpenStackJenkinsSource():
      
      def update_entities(env):
            for attribute in env:
                  if not attribute.populated:
                        attribute_method = getattr(foo, 'bar')
                        if attribute_method:
                              attribute.value = attriubte_method(env) # The reason we pass env 
                        else:
                              pass
            return env

      def jobs(env):
            jobs = []
            jobs_data = self.make_API_call_to_get_jobs()
            for job in jobs_data:
                  jobs.append(Job(...))
            return jobs

populate_arguments(arguments, hierarchy_of_entities): # works the same way update_parser
# set Value.populate = True

query = Query(entities=entities)
query.start_query()

==========
def start_query():
      # Traverse entities
      entity.value.populate == True? -> Obtain information -> How?
      
--system-name = OSPJenkins
--test-name x

Class System

    name = Value(data/value="OSPJenkins", type=str)

Class Test
    __init__(self, name ): #shrink
       self.name
       seld.status = call_driver(class Test, )
       self.exc_time
    name = Value(data/value=Test(name='x', ..., ...), type=Test)

Value(type=Job, value/data)
class Value():
    data
    Type
    instancees 
    value
    populate = False 

    addInstance()




    
# ===============
# What to do when it's a simple type value (str) and not CI entity (Job, JenkinsSystem, ...)
for entity in entities:
      populate_arguments()
def populate_arguments(arguments, attributes):
    for attribute in attributes(entity):
          if attribute instance of Value and attribute.expose_name in arguments:
                entity.attribute.value = AttributeValueCreator(class_type=entity.attribute.type,value=arguments[attribute.expose_name])
          # Note: check performance regarding recursion. Specifically number of levels
          populate_arguments(attribute.attributes)

def AttributeValueCreator():
    

# =============
Environment.name.argument_name = arguments[Environment.name.argument_name].value

Environment
      name != package-version 
      systems
          jenkins != package-version 
             name != package-version
             url != package-version
      

# =============================================

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