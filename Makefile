.PHONY: build

# Colours
BLUE			=	\033[0;34m
CYAN			=	\033[0;36m
RESET			=	\033[0m

build:
	cd client && ng build
	@mkdir -p static/js static/css static/img
	@rm static/js/main-*.js
	@rm static/css/styles-*.css
	@mv client/dist/client/browser/index.html templates
	@mv client/dist/client/browser/*.js static/js/
	@mv client/dist/client/browser/*.css static/css/
	@mv client/dist/client/browser/*.ico static/img/
	@printf "$(BLUE)==> $(CYAN)Client build complete ✅\n\n$(RESET)"