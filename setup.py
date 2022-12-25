import shutil

from setuptools import find_packages, setup

cbindgen_toml = '''
language = "C"
style = "type"
header = "/* Licensed under Apache-2.0 */"
include_guard = "CRYPTO_PAIR_FFI_H_"
include_version = true
autogen_warning = "/* Warning, this file is autogenerated by cbindgen. Don't modify this manually. */"
tab_width = 2
line_length = 80

[parse]
parse_deps = true
include = ["crypto-market-type"]
'''


def build_native(spec):
    build = spec.add_external_build(cmd=['cargo', 'build', '--release'],
                                    path='./crypto-pair-ffi')
    spec.add_cffi_module(module_path='crypto_pair._lowlevel',
                         dylib=lambda: build.find_dylib(
                             'crypto_pair_ffi', in_path='target/release'),
                         header_filename=lambda: build.find_header(
                             'crypto_pair_ffi.h', in_path='include'),
                         rtld_flags=['NOW', 'NODELETE'])


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# backup files
shutil.move('crypto-pair-ffi/include/crypto_pair_ffi.h',
            'crypto-pair-ffi/include/crypto_pair_ffi.h.bak')
shutil.move('crypto-pair-ffi/cbindgen.toml',
            'crypto-pair-ffi/cbindgen.toml.bak')
with open("crypto-pair-ffi/cbindgen.toml", "w", encoding="utf-8") as f_out:
    f_out.write(cbindgen_toml)

setup(
    name='crypto_pair',
    version="2.3.10",
    author="soulmachine",
    description="Normalize cryptocurrency trading pairs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soulmachine/crypto-pair-py",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['milksnake'],
    install_requires=['milksnake'],
    milksnake_tasks=[build_native],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['blockchain', 'cryptocurrency', 'trading'],
)

# restore files
shutil.move('crypto-pair-ffi/include/crypto_pair_ffi.h.bak',
            'crypto-pair-ffi/include/crypto_pair_ffi.h')
shutil.move('crypto-pair-ffi/cbindgen.toml.bak',
            'crypto-pair-ffi/cbindgen.toml')
