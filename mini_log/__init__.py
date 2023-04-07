# Log levels
OFF = 5
DEBUG = 4
INFO = 3
WARNING = 2
ERROR = 1
CRITICAL = 0

_level_num_to_name = {
    DEBUG: "DEBUG",
    INFO: "INFO",
    WARNING: "WARNING",
    ERROR: "ERROR",
    CRITICAL: "CRITICAL",
}


class MiniLog:
    def __init__(self, name, level=INFO) -> None:
        self._name = name
        self._level = level

    def log(self, level, message):
        if level >= self._level and self._level < OFF:
            print(f"{self._name} [{_level_num_to_name[level]}] '{message}'")

    def debug(self, message):
        self.log(DEBUG, message)

    def info(self, message):
        self.log(INFO, message)

    def warning(self, message):
        self.log(WARNING, message)

    def error(self, message):
        self.log(ERROR, message)

    def critical(self, message):
        self.log(CRITICAL, message)

    def get_level(self):
        return self._level

    def set_level(self, level):
        self._level = level

# type: dict[str, MiniLog]
loggers = {}


def get_logger(name):
    if name not in loggers:
        loggers[name] = MiniLog(name)
    return loggers[name]
