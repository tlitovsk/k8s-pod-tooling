from dockerfile_parse import DockerfileParser
from copy import deepcopy
from .ids import ids
import re


class DebugDockerfile:

    def __init__(self, dfp):
        self._dfp = dfp
        self._install_command = "RUN {}".format(
            DebugDockerfile._getInstallCommand(self._dfp.structure))

    def getDebugDockerFile(self):
        dfp = deepcopy(self._dfp)
        original_cmd = dfp.cmd
        # TODO : actually copy it to script and handle it there
        if re.search('[;&]', original_cmd) is not None:
            raise NotImplementedError(
                'Please use bash script and not complex cmd')

        cmd = '\nCMD ' + original_cmd + ' & sleep infinity \n'
        retVal = dfp.lines
        # TODO : install the cmd as first wge and not last
        retVal.append("\n" + self._install_command + "\n")
        retVal.append(cmd)
        return retVal

    @staticmethod
    def _match(id, cmd_line):
        # TODO : test case matching
        if cmd_line['instruction'] in id.keys():
            cmd = id[cmd_line['instruction']]
            if cmd_line['value'].find(cmd) > -1:
                return True
        return False

    @staticmethod
    def _getInstallCommand(commands):
        for command in commands:
            for id in ids:
                if DebugDockerfile._match(id['tags'], command):
                    return id['instrument']
        raise NotImplementedError('can identify the image src')


_kcp_bash = '''
#!/bin/bash -xe

function help()
{
    echo "Usage:"
    echo "ksp <pod name> <local file> <location in pod>"
}

if [ -z $1 ]
then
    help
    exit 1
fi

cat $2 | kubectl exec -ti $1 -- /bin/bash -c "cat > $3//$2"
'''


def instrument(dockerfile):
    ''' Get a dict in dockerfile parser format
        https://github.com/DBuildService/dockerfile-parse/blob/master/dockerfile_parse/parser.py#L163
    '''
    dfp = DockerfileParser(dockerfile)
    prc = DebugDockerfile(dfp)
    #pprint( prc.getDebugDockerFile() )
    with open("{}.debug".format(dockerfile), 'w') as f:
        f.write("".join(prc.getDebugDockerFile()))

    with open("kcp.sh", 'w') as f:
        f.write(_kcp_bash)
