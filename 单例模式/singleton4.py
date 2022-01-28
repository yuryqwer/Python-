----Logger.py-----
file_name = None


def _write_log(level, msg):
    with open(file_name, "a") as log_file:
        log_file.write(f"[{level}] {msg}\n")


def critical(msg):
    _write_log("CRITICAL", msg)


def error(msg):
    _write_log("ERROR", msg)


def warn(msg):
    _write_log("WARN", msg)


def info(msg):
    _write_log("INFO", msg)


def debug(msg):
    _write_log("DEBUG", msg)

----a.py----
import Logger

if not Logger.file_name:
    Logger.file_name = "newfilename.log"
Logger.info("hello from a.py")

----main.py----
import Logger

if not Logger.file_name:
    Logger.file_name = "filename.log"
Logger.info("hello from main.py")
import a
