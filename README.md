# 0x00. AirBnB clone - The console
A command interpreter to manage your AirBnB objects.

## Table of Content
- [Project Description](#project-description)
- [Command Interpreter Description](#command-interpreter-description)
- [Progress](#progress)
- [Resources](#resources)
- [Tasks](#tasks)
 - [Mandatory Tasks](#mandatory-tasks)
 - [Advanced Tasks](#advanced-tasks)
- [Author](#author)

## Project Description
This project is regarded as the first step towards building a full web applications to which other following projects: HTML/CSS templating, database storage, API, front-end integration are added to.

Each task is linked and will help to:
- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Command Interpreter Description
The command interpreter is a simple shell with a specific use-case; which is to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
### How to start it
The command interpreter can be started with:
`./console.py`
### How to use it
The interpreter can be used both in an interactive and non-interactive mode

For the interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

For the non-interactive mode:
```
$ echo help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
### Examples

## Progress
- [ ] Mandatory Tasks
 - [ ] Task 0
 - [ ] Task 1
 - [ ] Task 2
 - [ ] Task 3
 - [ ] Task 4
 - [ ] Task 5
 - [ ] Task 6
 - [ ] Task 7
 - [ ] Task 8
 - [ ] Task 9
 - [ ] Task 10
- [ ] Advanced Tasks
 - [ ] Task 100
 - [ ] Task 101
 - [ ] Task 102
 - [ ] Task 103
 - [ ] Task 104
 - [ ] Task 105
 - [ ] Task 106

## Resources
> - [cmd module](https://docs.python.org/3.8/library/cmd.html)
> - [cmd module in depth](http://pymotw.com/2/cmd/)
> - packages
> - [uuid module](https://docs.python.org/3.8/library/uuid.html)
> - [datetime module](https://docs.python.org/3.8/library/datetime.html)
> - [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
> - [args/kwargs](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)
> - [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
> - [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
> - [python unittest](https://realpython.com/python-testing/)

## Tasks
### Mandatory Tasks
0. #### REAME, AUTHORS
- &emsp; Write a README.md:
> - &emsp;&emsp; description of the project
> - &emsp;&emsp; description of the command interpreter:
> - &emsp;&emsp;&emsp;&emsp; how to start it
> - &emsp;&emsp;&emsp;&emsp; how to use it
> - &emsp;&emsp;&emsp;&emsp; examples
- &emsp; You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page(https://github.com/moby/moby/blob/master/AUTHORS)
- &emsp; You should use branches and pull requests on GitHub - it will help you as team to organize your work

&emsp;File(s):
- &emsp;&emsp;&emsp;[file]() - file description
2. #### Test
> Task description

&emsp;File(s):
- &emsp;&emsp;&emsp;[file]() - file description

### Advanced Tasks
1. #### Test
> Task description

&emsp;File(s):
- &emsp;&emsp;&emsp;[file]() - file description
2. #### Test
> Task description

&emsp;File(s):
- &emsp;&emsp;&emsp;[file]() - file description

## Authors
- Github - [omitogunjesufemi](https://github.com/omitogunjesufemi)
- Twitter - [@omixcreative](https://twitter.com/omixcreative)
- Linkedin - [@omitogunjesufemi](https://www.linkedin.com/in/omitogunjesufemi)
