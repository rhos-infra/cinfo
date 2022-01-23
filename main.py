1. User runs cinfo command
2. Load configuration file

{"environments": [{}, {}] }

3. Creates environments instances based on data in configuration file

envs = []
for env in config["enviroments"]:
    envs.append(Environment(**env))

Result:
[
Environment(name="TripleO CI", systems=[System(type=zuul)]),
Environment(name="OSP Phase 3" systems=[System(type=jenkins, jobs="DFG-*")])
Environment(name="OSP Component Pipeline" systems=[System(type=jenkins), System(type=zuul)])
]

4. Create ArgAggregator

# Parser vs. ArgAggregator
# option1 (ArgAggregator) - generated from configuration context: in memory objects are created empty. and holing an information about 
#           flags the parser gets the information through an implemented ParserInterface (not feasible at this point)
# option2 (Parser) - generated from the code (static scan) (less prefferable)
# option3 - an intermidiate approach: arguments are defined at the entities class level (SD principle)
# we are not aiming to catch cross correlation between the parmaters, but the ooutpur will reflect whch params were found relevant 
# in case of each system 
# cinfo query --stage x --role y
# Environments:
#  OSP Component Pipeline:
#     Jenkins:
#       - job1
#            Stage: x
#       - job2
#            Stage: x
#     Zuul:
#       - jobX 
#            Role: y
#       - jobY
#            Role: y


# We craete ArgAggerator instance which is all the relevant args based on the created environments
# Each environment composed out of CI entities and each entity implements ArgInterface

argAgragator = ArgAgregator()


Environment(stage=x, role=y)
  Jenkins(stage=x, role=y)
    JenkinsDriver(stage=x)
  Zuul(stage=x, role=y)
    ZuulDriver(role=y)


5. Validate user input

cinfo query --domain tripleo_ci --jobs job1,job2 --test-name x --build-number x

build-number=x


# Parser output is a list of (key, value)  (e.g. --flag=Value)
# AgrAgregator contains a map of (key, value) arguments based on the ArgInterface
# Environment.System.Job.Build.build_number 
# class Build
#    ArgInterface
#      build-number
#      int 

 of entities calssed parser = Parser (tripleo_ci_env, osp_phase_3_env)the


cinfo --help 
Usage cinfo --config [https| filename]

config -config filen-name

cinfo --config http://... -v 
connesting
getting
validating

Scope:
  Phase 1 implementation:
    * Generate parser based on used environments (and their systems)
  Phase 2 implementation:
    * hanlde cross system arg validation (e.g. Jenkins vs. Zuul - using --stages and --roles at the same command invocation)

Next:
  - Finish parser design (steps 4 & 5)
    - Creating the objects and passing the data to them
