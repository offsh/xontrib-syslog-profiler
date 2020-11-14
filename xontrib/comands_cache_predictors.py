def predict_sudo(args):
    sudo_executed_command = args
    commands_cache = __xonsh__.commands_cache  # pylint: disable=undefined-variable
    return commands_cache.predict_threadable(sudo_executed_command)


def profiler_predictors(default_predictors):
    """
    Generates a new map with command cache predictors
    with some improvements to capture special commands
    output such as "sudo" or "ssh"

    Parameters
    ----------
    default_predictors: dict
        This dict contain command cache predictor for some
        special commands, you usually want to define it as
        __xonsh__.commands_cache.threadable_predictors which
        is the one used by the current xonsh session.
    """

    xonsh_cc_predictors = default_predictors
    xonsh_cc_predictors['sudo'] = predict_sudo
    return xonsh_cc_predictors
