## Local Build

```
poetry install
poetry build
```

## CI Build

1. tag the ref with a name staring with `cibuildwheel`
2. Push the tag onto Github. It will trigger `cibuildwheel` workflow building wheels for:

- OS
    - `latest-ubuntu`
    - `macos-13`
    - `macos-latest`
- Python:
    - `ubuntu`: `>= 3.8`
    - `macos`: `>= 3.9`
