.PHONY: build

# Colours
BLUE			=	\033[0;34m
CYAN			=	\033[0;36m
RESET			=	\033[0m

build:
	cd client && ng build
	mv client/dist/client/browser/* templates
	@printf "$(BLUE)==> $(CYAN)Client build complete ✅\n\n$(RESET)"
