from testinfra.host import Host


def test_default_packages(host: Host) -> None:
    p = host.package("git")
    assert p.is_installed


def test_default_command(host: Host) -> None:
    f = host.file("/usr/bin/git")
    assert f.is_file
