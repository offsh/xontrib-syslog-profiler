from xontrib.json_syslog_history_backend import JsonSyslogHistory
from xontrib.comands_cache_predictors import profiler_predictors
import xonsh

__all__ = ()

$XONSH_HISTORY_BACKEND = JsonSyslogHistory
$XONSH_STORE_STDOUT = True

# --- COMMANDS CACHE PREDICTORS ----------------------------------------

xonsh_cc_predictos = __xonsh__.commands_cache.threadable_predictors

__xonsh__.commands_cache.threadable_predictors = profiler_predictors(xonsh_cc_predictos)

