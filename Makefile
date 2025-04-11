TOPDIR          ?= /root/rpmbuild
RPMDIR          ?= $(TOPDIR)/RPMS
ARCH            ?= $(shell arch)
SPECDIR         ?= $(shell rpm --eval '%{_specdir}')
OSVERSION       ?= $(shell rpm --eval '%{rhel}')
RHOSPVERSION    ?= 16
REPO            ?= $(RPMDIR)/repodata/repomd.xml
COMMON_TARGETS  ?= $(TOPDIR)/TARGETS
PYTHON_MODULES  ?= api-object-schema capacity confetti flux gossip \
                   infi-dtypes-iqn infi-dtypes-nqn infi-dtypes-wwn \
                   infinisdk logbook mitba pact storage-interfaces \
                   click munch urlobject vintage waiting
EPEL_PACKAGE    ?= https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(OSVERSION).noarch.rpm
DEV_PACKAGES    ?= createrepo epel-rpm-macros rpm-build rpmdevtools rpmlint yum-utils
DEV_TARGET      ?= $(addprefix $(COMMON_TARGETS)/, dev)
PYTHON_PACKAGES ?= $(addprefix python3-, $(PYTHON_MODULES))
PYTHON_TARGETS  ?= $(addprefix $(COMMON_TARGETS)/, $(PYTHON_PACKAGES))
PYTHON_SPECS    ?= $(addprefix $(SPECDIR)/, $(addsuffix .spec, $(PYTHON_MODULES)))
IMAGE           ?= redhat/ubi8
RPMBUILD        := rpmbuild --clean --undefine '_disable_source_fetch'
SETUPTREE       := rpmdev-setuptree
YUM_BASEDIR     := /etc/yum.repos.d
YUM_OPTIONS     := --assumeyes
YUM_COMMAND     := yum $(YUM_OPTIONS)
YUM_CLEAN       := $(YUM_COMMAND) --enablerepo='*' clean all
YUM_INSTALL     := $(YUM_COMMAND) install
YUM_UPDATE      := $(YUM_COMMAND) update

CREATEREPO      := createrepo
BUILDDEP        := yum-builddep $(YUM_OPTIONS)
RPMLINT         := rpmlint --info
MKDIR           := install -v -d
TOUCH           := touch
RPM             := rpm
RM              := rm -rf

all: 
	@echo 'Run $(MAKE) USER=email PASSWORD=passwd docker => to build inside a container'
	@echo 'Run $(MAKE) USER=email PASSWORD=passwd local  => to local build'

docker:
	@docker run --rm --volume $(CURDIR):$(TOPDIR):rw $(IMAGE) \
		sh -c '$(YUM_INSTALL) make && make -C $(TOPDIR) USER=$(USER) PASSWORD=$(PASSWORD) local'

local: $(DEV_TARGET) $(COMMON_TARGETS) $(PYTHON_TARGETS) $(REPO) test clean

clean:
	subscription-manager remove --all
	subscription-manager unregister
	subscription-manager clean
	$(RM) $(COMMON_TARGETS)

test:
	$(YUM_CLEAN)
	printf '[test]\nname=test\nbaseurl=file://%s\nenabled=1\ngpgcheck=0\n' $(RPMDIR) | tee $(YUM_BASEDIR)/test.repo
	$(YUM_UPDATE)
	$(YUM_INSTALL) python3-infinisdk
	$(RPM) -qi $(PYTHON_PACKAGES)
	$(RPMLINT) $(PYTHON_SPECS) $(PYTHON_PACKAGES)

$(COMMON_TARGETS):
	$(MKDIR) $@

$(DEV_TARGET): $(COMMON_TARGETS)
	@subscription-manager register --force --username=$(USER) --password=$(PASSWORD)
	subscription-manager list --available
	subscription-manager refresh
	subscription-manager attach --auto
	subscription-manager repos --enable codeready-builder-for-rhel-$(OSVERSION)-$(ARCH)-rpms
	echo SKIP subscription-manager repos --enable openstack-$(RHOSPVERSION)-tools-for-rhel-$(OSVERSION)-$(ARCH)-rpms
	echo SKIP subscription-manager repos --enable openstack-$(RHOSPVERSION)-for-rhel-$(OSVERSION)-$(ARCH)-rpms
	$(YUM_INSTALL) $(EPEL_PACKAGE)
	$(YUM_CLEAN)
	$(YUM_UPDATE)
	$(YUM_INSTALL) $(DEV_PACKAGES)
	$(SETUPTREE)
	$(TOUCH) $@

$(COMMON_TARGETS)/python3-%: $(SPECDIR)/%.spec $(DEV_TARGET)
	$(BUILDDEP) $<
	$(RPMBUILD) -ba $<
	$(TOUCH) $@

$(REPO): $(PYTHON_TARGETS)
	$(CREATEREPO) $(RPMDIR)

.PHONY: all clean docker local test
