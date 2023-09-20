# ansible-role-amazon-efs-utils #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-amazon-efs-utils/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-amazon-efs-utils/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-amazon-efs-utils/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-amazon-efs-utils/actions/workflows/codeql-analysis.yml)

This is an Ansible role for installing
[amazon-efs-utils](https://github.com/aws/efs-utils).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| amazon_efs_utils_create_efs_users_group | Whether or not to create a group for EFS share users. | `true` | No |
| amazon_efs_utils_efs_users_gid | The GID to assign the group for EFS share users. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| amazon_efs_utils_efs_users_group | The name of group to be created for EFS share users. | `efs_users` | No |
<!--
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install Amazon EFS utilities
      ansible.builtin.include_role:
        name: amazon_efs_utils
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
