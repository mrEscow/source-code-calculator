COLOR_HEADER=\e[92m
COLOR=\e[93m
END=\033[0m
PROJECT_NAME := SourceCalc

.SILENT: help gui clean build

help:
	printf "$(COLOR_HEADER)$(PROJECT_NAME) management\n\n" && \
	printf "$(COLOR)make help$(END)\t Show this message\n" && \
	printf "$(COLOR)make gui$(END)\t Build GUI\n" && \
	printf "$(COLOR)make build$(END)\t Build application distributive directory\n" && \

gui:
	@pyside2-uic ui/form.ui -o app/form.py

clean:
	@rm -Rf ./build ./dist

build: clean
	@pyinstaller main.spec