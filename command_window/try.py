from scripttest import TestFileEnvironment

env = TestFileEnvironment('./qs')

def test_script():
    env.reset()
    result = env.run('cat coding-challenge/example-files_payroll-2016.csv | qs + %s' % filename)
    # or use a list like ['do_awesome_thing', 'testfile', ...]
    assert result.stdout.startswith('Creating awesome file')
    assert filename in result.files_created