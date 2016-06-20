_rhel = {"tags": {"FROM": "rhel", "RUN": "yum"},
         "instrument": "yum install python-ipdb ltrace gdb vim -y"}
_centos = {"tags": {"FROM": "centos", "RUN": "yum"}, "instrument":
           "yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && yum install python-ipdb ltrace gdb vim -y"}
_fedora = {"tags": {"FROM": "fedora", "RUN": "dnf"},
           "instrument": "dnf install python-ipdb ltrace gdb vim coreutils -y"}
#_debian = { "FROM" : "debian" , "RUN" : "apt-get" }

ids = [_rhel, _centos, _fedora ]

#TODO make the yum install command in the beginning to save rebuild time
