.PHONY: build

# Colours
BLUE			=	\033[0;34m
CYAN			=	\033[0;36m
RESET			=	\033[0m

build:
	cd client && ng build
	@mkdir -p static/js static/css static/img
	@mv client/dist/client/browser/index.html templates
#	Copy js files
	@i=1; \
	for file in client/dist/client/browser/*.js; do \
		cp "$$file" "static/js/script$$i.js"; \
		i=$$((i+1)); \
	done; \

	@printf "$(BLUE)==> $(CYAN)JS files copied ✅\n\n$(RESET)"

#	Copy CSS files
	@i=1; \
	for file in client/dist/client/browser/*.css; do \
		cp "$$file" "static/css/style$$i.css"; \
		i=$$((i+1)); \
	done; \

	@printf "$(BLUE)==> $(CYAN)CSS files copied ✅\n\n$(RESET)" 

	@mv client/dist/client/browser/favicon.ico static/img
	@git checkout HEAD -- templates/index.html
	@printf "$(BLUE)==> $(CYAN)Client build complete ✅\n\n$(RESET)"