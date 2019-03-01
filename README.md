# Features

- ansible 2.4 to 2.7 support, ok with junos from 13 up to 15
- flexible port configuration from site-specific yaml file
    - per vlan sections
    - one file for multiple devices
    - support for plain access ports or trunks of several pre-configured
      types (like "phone" or "AP"); default trunk type could be specified
      at vlan level
    - support for interface ranges
- extensive check for configuration file sanity: interface indexes must be
  unique, all device names must be valid etc
- unused ports are disabled by default (configurable), some ports could
  be marked as "protected" and excluded from configuration (e.g uplinks and
  downlinks or aggregate ports)
- support for multiple sites with common configuration + local overrides
- HTML report of configuration data could be uploaded to external web server
  for future reference

Please see included example and scripts themselves for configuration details,
maybe I'll document them here later :)

# What is included

- `conf_juniper` sets up access and trunk ports on Juniper EX switch according to yaml configuration
- `prepare_juniper` is supplementary script to enable netconf on switch and create administrative
  users with key-only auth and restricted set of privileges.

# Operational notes
- VLAN configuration and port configuration parts take from 30 to 60 seconds on ex3300, so
  be patient
- Accessing junos with ansible is still a bit fragile: ex3300 does not like ssh keys > 1024 bits,
  ex2300 sometimes locks up while configurins vlans etc, but usually some work-around could be
  found
- Actually "domains.yaml" is also used to configure DNS, DHCP, AD domain etc, and not all
  parts are used for switch configuration (but e.g. IP address is included in report)