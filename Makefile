.PHONE: cython clean test download run

cython:
	python setup.py build_ext --inplace

test:
	pytest

download:	SHELL:=/bin/bash
download:
	@if [[ -f "data/example-lung-ct.zip" ]]; then																													\
		echo "Data file already exists";																																		\
	else																																																	\
		mkdir -p data;																																											\
		wget -O data/example-lung-ct.zip https://s3-us-west-1.amazonaws.com/innolitics/example-lung-ct.zip;	\
	fi

run:
	python python/process_and_export.py

clean:
	rm -f *.so python/*.so python/*.cpp
	rm -rf exported

cleaner: clean
	rm -rf data
