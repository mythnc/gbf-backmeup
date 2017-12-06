lint: test
	pylint gbf_backmeup
test:
	pytest -v
model:
	rm -vf gbf_backmeup/gbf_backmeup_test.db
	python -c 'from gbf_backmeup import model; model()'
crawl:
	python -c 'from gbf_backmeup import crawl; crawl()'
recrawl: model
	python -c 'from gbf_backmeup import crawl; crawl()'
wipeout:
	python -c 'from gbf_backmeup import wipeout; wipeout()'
