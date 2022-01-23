class Logger:
    """
    利用类变量在不同实例中的唯一性，将类变量作为全局标志位
    在调用类的__new__方法创建实例时，访问此标志位
    如果不存在则创建实例，否则直接返回最初创建的实例
    """
    def __new__(cls, *args):
        if not hasattr(cls, "instance"):
            # 调用object的__new__方法创建一个cls类的实例
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, file_name):
        """保证后续实例不再对日志路径进行修改"""
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
