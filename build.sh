pipenv sync
pushd aoc-pyo3 || exit
pipenv run maturin develop
popd || exit
ccd