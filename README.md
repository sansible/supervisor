# supervisor

Master: [![Build Status](https://travis-ci.org/sansible/supervisor.svg?branch=master)](https://travis-ci.org/sansible/supervisor)
Develop: [![Build Status](https://travis-ci.org/sansible/supervisor.svg?branch=develop)](https://travis-ci.org/sansible/supervisor)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This installs Supervisor and optionally creates a config file with configurable
settings. Installs using Pip so a large range of versions are available, sets up
in a similar fashion to OS packages with a default config file, symlinks to
/usr/bin, SysVinit scripts and log directories.

Init scripts are taken from (https://github.com/Supervisor/initscripts)[].




## Installation and Dependencies

To install run `ansible-galaxy install sansible.supervisor` or add this to your
`roles.yml`.

```YAML
- name: sansible.supervisor
  version: v1.2.x
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses tags: **build** and **configure**

* `build` - Installs supervisor
* `configure` - Configures supervisor




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

To stop this role from starting Supervisor at all the
sansible_supervisor_start_on_boot flag is available, useful if you want to start
once a service has been added:

```YAML
- name: Install and configure supervisor with a service
  hosts: "somehost"

  roles:
    - role: sansible.supervisor
      sansible_supervisor_start_on_boot: no

  post_tasks:
    - name: Add my_app service definition
      become: yes
      file:
        dest: "{{ sansible_supervisor_conf_dir }}/my_app.conf"
        src: service.conf

    - name: Ensure supervisor service is started
      become: yes
      service:
        name: supervisor
        state: started

    - name: Ensure my_app is present
      become: yes
      supervisorctl:
        name: my_app
        state: present

    - name: Ensure my_app is started
      become: yes
      supervisorctl:
        name: my_app
        state: started
```
