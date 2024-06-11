from main.threads import ctrl, threads


def main():
    for thread in threads:
        thread.setDaemon(True)
        thread.start()

    ctrl.run_forever(10)
