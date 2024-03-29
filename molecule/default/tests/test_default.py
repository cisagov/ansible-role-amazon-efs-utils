"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_packages(host):
    """Test that the appropriate packages were installed."""
    distribution = host.system_info.distribution
    if distribution == "fedora":
        pkgs = ["make", "rpm-build", "amazon-efs-utils"]
    elif distribution == "debian" or distribution == "ubuntu" or distribution == "kali":
        pkgs = ["make", "binutils", "amazon-efs-utils"]
    elif distribution == "amzn":
        pkgs = ["amazon-efs-utils"]
    else:
        # We don't support this distribution
        assert False
    packages = [host.package(pkg) for pkg in pkgs]
    installed = [package.is_installed for package in packages]
    assert len(pkgs) != 0
    assert all(installed)


@pytest.mark.parametrize("service", ["amazon-efs-mount-watchdog"])
def test_services(host, service):
    """Test that the expected services were enabled."""
    assert host.service(service).is_enabled


def test_efs_users_group(host):
    """Test that the expected group was created."""
    assert host.group("efs_users").exists
