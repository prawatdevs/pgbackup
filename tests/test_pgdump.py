import pytest
import subprocess

from pgbackup import pgdump 

url = "postgres://pawan:pawan123@65.0.93.138:80/sample"

def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprcess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump return a valid error if pg_dump is not installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file")
    with pytest.raises(SystemExit):
        pgdump.dump(url)

def test_dump_file_name_without_timestamp():
    """
    pgdump.db_file_name return the name of db
    """

    assert pgdump.dump_file_name(url) == "db_one.sql"

def test_dump_file_name_with_timestamp():
    """
    pgdump.dump_file_name returns the name of the database
    """

    timestamp = "2023-01-22T02:16:10"
    assert pgdump.dump_file_name(url, timestamp) == "db_one-2023-01-22T02:16:10.sql"


