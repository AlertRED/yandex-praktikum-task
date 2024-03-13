.PHONY: all
all: setup
	make -j 2 bot rss


.PHONY: check-ffmpeg
check-ffmpeg:
	@type ffmpeg >/dev/null 2>&1 || \
		(echo Install ffmpeg first && exit 1);


.PHONY: setup
setup: check-ffmpeg
	python3 -m venv venv
	./venv/bin/pip3 install -r ./requirements.bot.txt
	./venv/bin/pip3 install -r ./requirements.rss.txt


.PHONY: rss # recognition socket server
rss:
	./venv/bin/python3 run_rss.py


.PHONY: bot
bot: 
	./venv/bin/python3 run_bot.py
