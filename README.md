# Ansible role: Git

![Molecule Test](https://github.com/crgwilson/ansible-role-git/workflows/Molecule%20Test/badge.svg?branch=master)

Install [git](https://git-scm.com/)

## Variables

This role is really simple (theres only one package module), all variables are
super-duper straight forward and [can be found here](defaults/main.yml)

## Testing

Testing for this project is setup using
[Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
