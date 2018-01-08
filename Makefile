.PHONE: cython clean test download run

cython:
	python setup.py build_ext --inplace

test:
	pytest

download:
	mkdir -p data
	wget -O data/example-lung-ct.zip https://s3-us-west-1.amazonaws.com/innolitics/example-lung-ct.zip

run:
	python python/process_and_export.py

clean:
	rm -f *.so python/*.so python/*.cpp
	rm -rf exported

cleaner: clean
	rm -rf data
