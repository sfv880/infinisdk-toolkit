TAG             ?= .infinidat
TOPDIR          ?= /root/rpmbuild
RPMDIR          ?= $(TOPDIR)/RPMS
ARCH            ?= $(shell arch)
SPECDIR         ?= $(shell rpm --eval '%{_specdir}')
OSVERSION       ?= $(shell rpm --eval '%{rhel}')
REPO            ?= $(RPMDIR)/repodata/repomd.xml
COMMON_TARGETS  ?= $(TOPDIR)/TARGETS
PYTHON_VERSION  ?= 3.11
PYTHON_MODULES  ?= pbr colorama sentinels vintage logbook dateutil \
                   arrow api-object-schema capacity confetti flux  \
                   gossip mitba infi-dtypes-iqn infi-dtypes-nqn    \
                   infi-dtypes-wwn waiting pact storage-interfaces \
                   click munch urlobject infinisdk cinder-infinidat
DEV_PACKAGES    ?= createrepo rpm-build rpmdevtools rpmlint yum-utils
DEV_TARGET      ?= $(addprefix $(COMMON_TARGETS)/, dev)
RPMMACRO_TARGET ?= $(addprefix $(COMMON_TARGETS)/, rpmmacros)
PYTHON_PACKAGES ?= $(addprefix python$(PYTHON_VERSION)-, $(PYTHON_MODULES))
PYTHON_TARGETS  ?= $(addprefix $(COMMON_TARGETS)/, $(PYTHON_PACKAGES))
PYTHON_SPECS    ?= $(addprefix $(SPECDIR)/, $(addsuffix .spec, $(PYTHON_MODULES)))
IMAGE           ?= almalinux:9
RPMBUILD        := rpmbuild --clean --undefine '_disable_source_fetch'
SETUPTREE       := rpmdev-setuptree
DNF_BASEDIR     := /etc/yum.repos.d
DNF_OPTIONS     := --assumeyes
DNF_COMMAND     := dnf $(DNF_OPTIONS)
DNF_CLEAN       := $(DNF_COMMAND) --enablerepo='*' clean all
DNF_CONFIG      := $(DNF_COMMAND) config-manager
DNF_INSTALL     := $(DNF_COMMAND) install
DNF_UPDATE      := $(DNF_COMMAND) update
DNF_FIX         := sed -i -e '/^mirrorlist=/d' -e 's|^\#.*baseurl=|baseurl=|g' /etc/yum.repos.d/*.repo
CREATEREPO      := createrepo --simple-md-filenames
BUILDDEP        := dnf builddep $(DNF_OPTIONS)
RPMLINT         := rpmlint --info
MKDIR           := install -v -d
TOUCH           := touch
RPM             := rpm
RM              := rm -rf

all:
	podman system prune -a -f
	podman run --rm --volume $(CURDIR):$(TOPDIR):Z,rw $(IMAGE) \
		sh -c "$(DNF_CLEAN) && $(DNF_FIX) && $(DNF_INSTALL) make && make -C $(TOPDIR) local"

local: $(PYTHON_TARGETS) test

test:
	rpm -qa | grep '$(TAG)' | xargs -rt rpm -e
	$(DNF_CLEAN)
	$(DNF_UPDATE)
	$(DNF_INSTALL) python$(PYTHON_VERSION)-cinder-infinidat python$(PYTHON_VERSION)-pbr
	$(RPM) -qi $(PYTHON_PACKAGES)
	rpm -q --provides $(PYTHON_PACKAGES)
	#$(RPMLINT) $(PYTHON_SPECS) $(PYTHON_PACKAGES)

$(COMMON_TARGETS):
	$(MKDIR) $@

$(DEV_TARGET): $(COMMON_TARGETS)
	$(DNF_INSTALL) dnf-plugins-core
	$(DNF_CONFIG) --enable appstream baseos crb || \
	$(DNF_CONFIG) --enable appstream baseos powertools
	$(DNF_CLEAN)
	$(DNF_UPDATE)
	$(DNF_INSTALL) $(DEV_PACKAGES)
	$(SETUPTREE)
	$(MKDIR) $(RPMDIR)
	$(CREATEREPO) $(RPMDIR)
	printf '[InfiniSDK]\nname=Infinidat InfiniSDK\nbaseurl=file://%s\nenabled=1\ngpgcheck=0\n' $(RPMDIR) | \
		tee $(DNF_BASEDIR)/test.repo
	#$(TOUCH) $@

$(RPMMACRO_TARGET):
	echo '%tag $(TAG)' | tee -a $(HOME)/.rpmmacros
	echo '%python3_pkgversion $(PYTHON_VERSION)' | tee -a $(HOME)/.rpmmacros
	echo '%__python3 /usr/bin/python%{python3_pkgversion}' | tee -a $(HOME)/.rpmmacros

$(COMMON_TARGETS)/python$(PYTHON_VERSION)-%: $(SPECDIR)/%.spec $(DEV_TARGET) $(RPMMACRO_TARGET)
	$(BUILDDEP) $<
	$(RPMBUILD) -ba $<
	$(CREATEREPO) $(RPMDIR)
	$(DNF_CLEAN)
	$(DNF_INSTALL) python$(PYTHON_VERSION)-$*
	rpm -q --provides python$(PYTHON_VERSION)-$*
	$(TOUCH) $@

.PHONY: all clean podman local test
