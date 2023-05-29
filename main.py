import win32api as win32
import pymem
import time

CONFIG_FILE = "config.ini"


def load_config():
    config = {}
    with open(CONFIG_FILE) as f:
        for line in f:
            key, value = line.strip().split("=")
            if '.' in value:
                config[key.strip()] = float(value.strip())
            else:
                config[key.strip()] = int(value.strip(), 0)
    return config


def bhop(config):
    try:
        pm = pymem.Pymem('csgo.exe')

        for module in pm.list_modules():
            if module.name == 'client.dll':
                client = module.lpBaseOfDll
                break
        else:
            raise Exception("client.dll not found")
        a = 1
        while True:
            time.sleep(0.01)

            if win32.GetAsyncKeyState(config['BIND_KEY']) & 0x8000:
                local_player = pm.read_int(client + config['LOCAL_PLAYER'])

                if local_player:
                    flags = pm.read_int(local_player + config['FLAGS'])

                    if flags and flags & (1 << 0):
                        pm.write_int(client + config['FORCE_JUMP'], 6)
                        time.sleep(config['JUMP_DELAY'])
                        pm.write_int(client + config['FORCE_JUMP'], 4)

                        print("jump", a)
                        a += 1

    except pymem.exception.ProcessNotFound:
        print("CS:GO process not found")
    except Exception as e:
        print("An error occurred:", str(e))


def main():
    config = load_config()
    bhop(config)


if __name__ == '__main__':
    main()
