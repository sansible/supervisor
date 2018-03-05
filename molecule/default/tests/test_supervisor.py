import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config(host):
    super_config = host.file('/etc/supervisor/conf.d/supervisord.conf')
    assert super_config.exists
    assert super_config.contains('^\s*loglevel\s*=\s*debug\s*$')
    assert super_config.contains('^\s*minfds\s*=\s*2048\s*$')
