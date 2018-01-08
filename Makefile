.PHONE: cython clean test

cython:
	python setup.py build_ext --inplace

test:
	pytest

clean:
	rm -f *.so python/*.so python/*.cpp
	rm -rf exported
