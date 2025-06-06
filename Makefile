# Makefile
setup:
	python -m venv venv && . venv/bin/activate && pip install -r requirements.txt

build-net:
	. env.sh && python scripts/build_net.py

gen-trips:
	. env.sh && python scripts/gen_trips.py

run:
	. env.sh && python scripts/run_batch.py

clean:
	find data/outputs -type f -name '*.xml' -delete
