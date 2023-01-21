from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown drivers. Available drivers are 'local' and 's3' ")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""Backup Postgresql database locally or to ASW S3""")
    parser.add_argument("url", help="URL of the databse to backup")
    parser.add_argument("--driver","-d",help="how and where to store backup",nargs=2,action=DriverAction,metavar=("DRIVER", "DESTINATION"), required=True)
    return parser

def main():
    from pgbackup import pgdump, storage
    import time

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        print("test on s3")
    else:
        outfile = open(args.destination, 'wb')
        print(f"backing up file locally to {outfile.name}")
        storage.local(dump.stdout, outfile)
