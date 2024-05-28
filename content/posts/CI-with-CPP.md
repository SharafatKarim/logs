+++
title = "CI-with-CPP"
description = "A simple one with makefile,"
+++

# CI - GitHub Actions with C++

A simple one with makefile,

```yml
name: C/C++ CI - MAKEFILE

on: 
  - push 
  - pull_request

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    
    - name: make all
      run: make all
    
    - name: Run the built binary
      run: |
        if [[ -f bin/Debug/entropy-calculator ]]; then
          ./bin/Debug/entropy-calculator & sleep 0.1; kill $!;
        elif [[ -f bin/Release/entropy-calculator ]]; then
          ./bin/Release/entropy-calculator & sleep 0.1; kill $!;
        elif [[ -f bin/Debug/entropy-calculator.exe ]]; then
          ./bin/Debug/entropy-calculator.exe & sleep 0.1; kill $!;
        elif [[ -f bin/Release/entropy-calculator.exe ]]; then
          ./bin/Release/entropy-calculator.exe & sleep 0.1; kill $!;
        else
          echo "Binary not found!";
          exit 1;
        fi
    
    - name: make clean
      run: make clean
```
Probably you can explore it [here.](https://github.com/SharafatKarim/entropy-calculator)
