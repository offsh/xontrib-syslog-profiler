from xonsh.history.json import JsonHistory
from datetime import datetime
import collections
import builtins
import socket
import os
import re


class JsonSyslogHistory(JsonHistory):

    def __init__(self, json_filename=None, syslog_filename=None, sessionid=None, gc=True, **meta):
        super().__init__(json_filename=json_filename, sessionid=sessionid, gc=gc, **meta)

        """Represents a xonsh session's history based on JSON backend
        that also logs to a syslog file.

        Parameters
        ----------
        sessionid : int, uuid, str, optional
          Current session identifier, will generate a new sessionid if not set.
        json_filename : String, log_file, optional
          File to write JSON logs to. If not set, it takes a default value.
        syslog_filename : String, log_file, optional
          File to write Syslog logs to. If not set, it takes a default value based on date.
        gc: boolean, optional
          Is garbage collector enabled?
        """

        self.ansi_scape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

        self.hostname = socket.gethostname()

        def get_syslog_filename():
            # pylint: disable=no-member
            data_dir = builtins.__xonsh__.env.get("XONSH_DATA_DIR")
            data_dir = os.path.join(os.path.expanduser(data_dir), "syslog")
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            return os.path.join(
                data_dir, "shell_profiler.log"
            )

        if syslog_filename is None:
            self.syslog_filename = get_syslog_filename()
        else:
            self.syslog_filename = syslog_filename

    # ---------------------------------------------------------------------------------

    def append(self, cmd):
        """Append a command item into history.

        Parameters
        ----------
        cmd: dict
            This dict contains information about the command that is to be
            added to the history list. It should contain the keys ``inp``,
            ``rtn`` and ``ts``. These key names mirror the same names defined
            as instance variables in the ``HistoryEntry`` class.
        """

        self._register_cmd(cmd)
        super().append(cmd)

    # ---------------------------------------------------------------------------------

    def _register_cmd(self, cmd):

        now_date = datetime.today()
        datestamp = now_date.strftime('%b %d')
        timestamp = now_date.strftime('%H:%M:%S')

        if 'out' in cmd:
            command_output = self.ansi_scape.sub('', cmd['out']).replace("\n", " ").replace("\t", " ")
        else:
            command_output = 'Not available'

        command_input = cmd['inp'].strip()
        command_timing = cmd['ts'][1] - cmd['ts'][0]
        return_value = cmd['rtn']

        pwd = data_dir = builtins.__xonsh__.env.get("PWD")
        user = data_dir = builtins.__xonsh__.env.get("USER")

        # crop long outputs
        command_output = (command_output[:1200] + '..') if len(command_output) > 1200 else command_output

        log_line = f"{datestamp} {timestamp} {self.hostname} xonsh_profiler: {command_input} executed at {pwd} by {user} with output: "
        log_line += f" {command_output} [{return_value}][{command_timing} seconds]"
        self.write_logs(log_line)

    # ---------------------------------------------------------------------------------

    def write_logs(self, log_string):
        """
        Write log_string to the log file
        """
        fd = open(self.syslog_filename, 'a+')
        fd.write(' '.join(log_string.split())+"\n")
        fd.flush()
        fd.close()

    # ---------------------------------------------------------------------------------

    def info(self):
        """A collection of information about the shell history.

        Returns
        -------
        dict or collections.OrderedDict
            Contains history information as str key pairs.
        """
        data = collections.OrderedDict(super().info())
        data['syslog_filename'] = self.syslog_filename
        return data
