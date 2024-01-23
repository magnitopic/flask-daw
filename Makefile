.PHONY: build

# Colours
BLUE			=	\033[0;34m
CYAN			=	\033[0;36m
RESET			=	\033[0m

build:
	cd client && ng build
	mkdir -p templates
    mv -p client/dist/client/browser/index.html templates
    mkdir -p static/js
    mv -p client/dist/client/browser/*.js static/js
    mkdir -p static/css
    mv -p client/dist/client/browser/*.css static/css
    mkdir -p static/img
    mv -p client/dist/client/browser/*.ico static/img
	@printf "$(BLUE)==> $(CYAN)Client build complete ✅\n\n$(RESET)"
