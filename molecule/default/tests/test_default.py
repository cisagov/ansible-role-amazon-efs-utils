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
    codename = host.system_info.codename
    release = host.system_info.release
    if distribution in ["fedora"]:
        if any(release.startswith(version) for version in ["39", "40"]):
            pkgs = [
                "amazon-efs-utils",
                "cargo",
                "make",
                "openssl-devel",
                "rpm-build",
            ]
        else:
            pkgs = [
                "amazon-efs-utils",
                "cargo",
                "make",
                "openssl-devel",
                "openssl-devel-engine",
                "rpm-build",
            ]
    elif distribution in ["ubuntu"]:
        pkgs = ["amazon-efs-utils"]
    elif distribution in ["debian", "kali"]:
        if codename in [
            "buster",
            "bullseye",
            "bookworm",
            "focal",
        ]:
            pkgs = ["amazon-efs-utils", "binutils", "make"]
        else:
            pkgs = [
                "amazon-efs-utils",
                "binutils",
                "cargo",
                "libssl-dev",
                "make",
                "pkgconf",
            ]
    elif distribution in ["amzn"]:
        pkgs = ["amazon-efs-utils"]
    else:
        # We don't support this distribution
        raise ValueError(f"Unsupported distribution {distribution}")
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
