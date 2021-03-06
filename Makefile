# Build

.PHONY: FORCE

clean: py-clean
.PHONY: clean

dist: py-dist
.PHONY: dist

install: py-install
.PHONY: install

lint: py-lint
.PHONY: lint

proto: py-proto
.PHONY: proto

test: py-test
.PHONY: test


# Non-PHONY targets (real files)

py-clean: FORCE
	./script/clean.sh

py-dist: FORCE
	./script/dist.sh

py-install: FORCE
	./script/install.sh

py-lint: FORCE
	./script/lint.sh

py-proto: FORCE
	./script/proto.sh

py-test: FORCE
	./script/test.sh
