 ![alt text](https://github.com/grg121/xontrib-syslog-profiler/blob/master/logo.png?raw=true)
<p align="center">
A Xonsh plugin to profile and log command execution to a syslog file.
</p>

## Installation

Using pip:
```
pip install xontrib-syslog-shell-profiler
```
## Usage

```bash
xontrib load syslog-shell-profiler
```

It will define `$XONSH_HISTORY_BACKEND = JsonSyslogHistory`, if you overwrite this variable the syslog backend will not work. This history backend used the default JSON one as base and any change on that class will affect to the plugin.