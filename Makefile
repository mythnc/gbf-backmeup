lint: test
	pylint gbf_backmeup
test:
	pytest -v
model:
	rm -vf gbf_backmeup/gbf_backmeup_test.db
	python -m gbf_backmeup.models
crawl:
	python -c 'from gbf_backmeup.crawler import start; start()'
recrawl: model
	python -c 'from gbf_backmeup.crawler import start; start()'
