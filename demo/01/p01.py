
import wayround_org.toxcorebot.bot


def test(command_name, opts, args, adds):
    print("test worked")
    return 0

cmds = {
    'build': test
    }

bot = wayround_org.toxcorebot.bot.Bot(
    commands=cmds,
    savedata_file='file.dat',
    bootstrap_hosts=[
        (
            b'127.0.0.1',
            33445,
            bytes.fromhex(
                'A0190D5AECEB0A9DAD355BE2C957BA1FBA01B8BE31EB8719D21A23F7B4E0671B'
                #'A0190D5AECEB0A9DAD355BE2C957BA1FBA01B8BE31EB8719D21A23F7B4E0671B94E3318EFD9C'
                )
            )
        ]
    # admin_keys=[
    #    'A0190D5AECEB0A9DAD355BE2C957BA1FBA01B8'
    #    'BE31EB8719D21A23F7B4E0671B94E3318EFD9C'
    #    ]
    )

if bot.start() == 0:

    print("addr: {}".format(bot.get_address().hex()))

    input()

    print("stopping bot")

    bot.stop()

    print("exiting")

    exit(0)
else:
    exit(1)
