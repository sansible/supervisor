# supervisor

Master: [![Build Status](https://travis-ci.org/sansible/supervisor.svg?branch=master)](https://travis-ci.org/sansible/supervisor)
Develop: [![Build Status](https://travis-ci.org/sansible/supervisor.svg?branch=develop)](https://travis-ci.org/sansible/supervisor)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This installs Supervisor and optionally creates a config file with configurable
settings.




## Installation and Dependencies

To install run `ansible-galaxy install sansible.supervisor` or add this to your
`roles.yml`.

```YAML
- name: sansible.supervisor
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses tags: **build** and **configure**

* `build` - Installs ...
* `configure` - Configures ...




## Examples

Simply include role in your playbook:

```YAML
- name: Install and configure supervisor
  hosts: "somehost"

  roles:
    - role: sansible.supervisor
```

To add some config settings (see [http://supervisord.org/configuration.html]()):

```YAML
- name: Install and configure supervisor
  hosts: "somehost"

  roles:
    - role: sansible.supervisor
      sansible_supervisor_conf_settings:
        - name: loglevel
          section: supervisord
          value: debug
        - name: minfds
          section: supervisord
          value: 2048
```
