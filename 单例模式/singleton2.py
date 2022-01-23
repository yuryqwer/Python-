class MetaSingleton(type):
    def __call__(cls, *args, **kwds):
        if not hasattr(cls, "instance"):
            cls.instance = super().__call__(*args, **kwds)
        return cls.instance


class Logger(metaclass=MetaSingleton):
    """
    利用类变量在不同实例中的唯一性，将类变量作为全局标志位
    在调用元类的__call__方法创建实例时，访问此标志位
    如果不存在则创建实例，否则直接返回最初创建的实例
    """
    def __init__(self, file_name):
        if not hasattr(self, "file_name"):
            self.file_name = file_name

    def _write_log(self, level, msg):
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)


if __name__ == "__main__":
    logger1 = Logger("filename.log")
    logger2 = Logger("newfilename.log")
    print(logger1.file_name, logger2.file_name)
