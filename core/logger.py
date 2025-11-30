def get_logger(name="qhybrid"):
    def log(msg):
        print(f"[{name}] {msg}")
    return log
