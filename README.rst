pgbackup
========

CLI for backup up remote Postgres SQL database locally or to AWS s3.

Preparing for Development
-------------------------


1. Ensure ''pip'' and ''pipenv'' are installed
2. Clone repository: ''git clone git@github.com:sample/pgbackup''
3. ''cd'' into repository
4. Fetch development dependencies ''make install''
5. Activate virtualenv: ''pipenv shell''

Usage
-----

Pass in full database URL, storage driver and destination.

S3 example with bucket name:

::

    $pgbackup postgres://user#example.com:5432/db_one --driver s3 backups

Local example with local path:

::

    $pgbackup postgres://user@example.com:5432/db_one --driver local /var/local/db_one/backups

Running Tests
-------------

Run tests locally using ''make'' if virtualenv is active:

::

    $ make

If virtualenv is not active then use:

::

    $pipenv run make



