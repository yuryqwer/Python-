class Logger:
    """
    利用类的唯一性，将类变量作为全局标志位
    将日志功能实现为类方法，其实不该叫单例模式，而是单类模式
    因为根本就没有产生实例
    """
    file_name = None

    @classmethod
    def _write_log(cls, level, msg):
        with open(cls.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    @classmethod
    def critical(cls, msg):
        cls._write_log("CRITICAL", msg)

    @classmethod
    def error(cls, msg):
        cls._write_log("ERROR", msg)

    @classmethod
    def warn(cls, msg):
        cls._write_log("WARN", msg)

    @classmethod
    def info(cls, msg):
        cls._write_log("INFO", msg)

    @classmethod
    def debug(cls, msg):
        cls._write_log("DEBUG", msg)


if __name__ == "__main__":
    logger1 = Logger
    if not logger1.file_name:
        logger1.file_name = "filename.log"
    logger2 = Logger
    if not logger2.file_name:
        logger2.file_name = "newfilename.log"
    print(logger1.file_name, logger2.file_name)
